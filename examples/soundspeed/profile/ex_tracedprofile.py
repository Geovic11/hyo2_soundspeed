import pyximport
pyximport.install()
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

import logging

from datetime import datetime
import numpy as np

from hyo2.soundspeed.profile.profile import Profile
from hyo2.soundspeed.profile.dicts import Dicts
from hyo2.soundspeed.profile.profilelist import ProfileList
from hyo2.soundspeed.profile.ray_tracing.tracedprofile import TracedProfile

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# create an example profile for testing
def make_fake_ssp(bias=0.0):
    ssp = Profile()
    d = np.arange(0.0, 100.0, 0.5)
    vs = np.arange(1450.0 + bias, 1550.0 + bias, 0.5)
    t = np.arange(0.0, 100.0, 0.5)
    s = np.arange(0.0, 100.0, 0.5)
    ssp.init_proc(d.size)
    ssp.proc.depth = d
    ssp.proc.speed = vs
    ssp.proc.temp = t
    ssp.proc.sal = s
    ssp.proc.flag[40:50] = Dicts.flags['user']
    ssp.proc.flag[50:70] = Dicts.flags['filtered']
    ssp.meta.latitude = 43.13555
    ssp.meta.longitude = -70.9395
    ssp.meta.utc_time = datetime.utcnow()
    return ssp


tss_depth = 5.0
tss_value = 1500.0
avg_depth = 1000.0
half_swath_angle = 70.0
ssp = make_fake_ssp(bias=0.0)
ssp_list = ProfileList()
ssp_list.append_profile(ssp)

start_time = datetime.now()
profile = TracedProfile(tss_depth=tss_depth, tss_value=tss_value,
                        avg_depth=avg_depth, half_swath=half_swath_angle,
                        ssp=ssp_list.cur)
end_time = datetime.now()
logger.debug("timing: %s" % (end_time - start_time))

logger.debug("traced profile:\n%s" % profile)
# logger.debug("api:\n%s" % dir(profile))
