import time
from PySide import QtGui
from datetime import datetime as dt

from hyo.soundspeed.logging import test_logging

import logging
logger = logging.getLogger()

from hyo.soundspeed.soundspeed import SoundSpeedLibrary
from hyo.soundspeedmanager.qt_callbacks import QtCallbacks
from hyo.soundspeedmanager.qt_progress import QtProgress


def main():
    app = QtGui.QApplication([])  # PySide stuff (start)
    mw = QtGui.QMainWindow()
    mw.show()

    lib = SoundSpeedLibrary(progress=QtProgress(parent=mw), callbacks=QtCallbacks(parent=mw))

    tests = [
        (43.026480, -70.318824, dt.utcnow()),  # offshore Portsmouth
        # (-19.1, 74.16, dt.utcnow()),  # Indian Ocean
        # (18.2648113, 16.1761115, dt.utcnow()),  # in land -> middle of Africa
    ]

    # download the woa09 if not present
    if not lib.has_woa09():
        success = lib.download_woa09()
        if not success:
            raise RuntimeError("unable to download")
    logger.info("has woa09: %s" % lib.has_woa09())

    # logger.info("load woa09: %s" % lib.atlases.woa09.load_grids())

    # test for a few locations
    for test in tests:
        start_time = time.time()
        # just the ssp (there are also ssp_min and ssp_max)
        logger.info("woa09 profiles:\n%s" % lib.atlases.woa09.query(lat=test[0], lon=test[1], datestamp=test[2]))
        logger.info("execution time: %.3f s" % (time.time() - start_time))

    # app.exec_()  # PySide stuff (end)

if __name__ == "__main__":
    main()
