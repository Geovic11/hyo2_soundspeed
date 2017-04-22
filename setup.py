import osimport sys# Always prefer setuptools over distutilsfrom setuptools import setup, find_packages# ---------------------------------------------------------------------------#                             Some helper stuff# ---------------------------------------------------------------------------here = os.path.abspath(os.path.dirname(__file__))def is_windows():    """ Check if the current OS is Windows """    return (sys.platform == 'win32') or (os.name is "nt")def txt_read(*paths):    """ Build a file path from *paths* and return the textual contents """    with open(os.path.join(here, *paths), encoding='utf-8') as f:        return f.read()# ---------------------------------------------------------------------------#                      Populate dictionary with settings# ---------------------------------------------------------------------------# create a dict with the basic information that is passed to setup after keys are added.setup_args = dict()setup_args['name'] = 'hyo.soundspeed'setup_args['version'] = '2017.3.0'setup_args['url'] = 'https://bitbucket.org/ccomjhc/hyo_soundspeed/'setup_args['license'] = 'LGPLv2.1 or CCOM-UNH Industrial Associate license'setup_args['author'] = 'Giuseppe Masetti(UNH,CCOM); Barry Gallagher(NOAA, OCS); Brian Calder(UNH,CCOM); ' \                       'Chen Zhang(NOAA,OCS); Matt Wilson(NOAA,OCS);  Jack Riley(NOAA,OCS)'setup_args['author_email'] = 'gmasetti@ccom.unh.edu; barry.gallagher@noaa.gov; brc@ccom.unh.edu; ' \                             'chen.zhang@noaa.gov; matthew.wilson@noaa.gov; jack.riley@noaa.gov'## descriptive stuff#description = 'A library and an application to manage sound speed profiles.'setup_args['description'] = descriptionsetup_args['long_description'] = (txt_read('README.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +                                  txt_read('HISTORY.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +                                  txt_read('AUTHORS.rst') + '\n\n\"\"\"\"\"\"\"\n\n' +                                  txt_read(os.path.join('docs', 'developer_guide_how_to_contribute.rst')))setup_args['classifiers'] = \    [  # https://pypi.python.org/pypi?%3Aaction=list_classifiers        'Development Status :: 4 - Beta',        'Intended Audience :: Science/Research',        'Natural Language :: English',        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',        'Operating System :: OS Independent',        'Programming Language :: Python',        'Programming Language :: Python :: 3',        'Programming Language :: Python :: 3.6',        'Topic :: Scientific/Engineering :: GIS',        'Topic :: Office/Business :: Office Suites',    ]setup_args['keywords'] = "hydrography ocean mapping survey sound speed profiles"## code stuff## requirementssetup_args['setup_requires'] =\    [        "setuptools",        "wheel",    ]setup_args['install_requires'] =\    [        "numpy",        "matplotlib",        "pillow",        "netCDF4",        "gdal",        "pyproj",        #"gsw",  # install it from github without scipy dependency        "pyserial",        #"pyside",        "basemap"    ]# hydroffice namespace, packages and other filessetup_args['namespace_packages'] = ['hyo']setup_args['packages'] = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "*.test*",                                                ])setup_args['package_data'] =\    {        '': ['soundspeedmanager/media/*.png', 'soundspeedmanager/widgets/media/*.png',             'soundspeedmanager/widgets/pdf/*.pdf',],    }setup_args['test_suite'] = "tests"setup_args['entry_points'] =\    {        'gui_scripts':        [            'sound_speed_manager = hyo.soundspeedmanager.gui:gui',            'sound_speed_settings = hyo.soundspeedsettings.gui:gui',        ],    }# ---------------------------------------------------------------------------#                            Do the actual setup now# ---------------------------------------------------------------------------setup(**setup_args)