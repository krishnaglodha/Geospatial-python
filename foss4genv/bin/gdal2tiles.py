#!/Users/krishnaglodha/Documents/foss4g-geospatial/foss4genv/bin/python3

import sys
# import osgeo_utils.gdal2tiles as a convenience to use as a script
from osgeo_utils.gdal2tiles import *  # noqa
from osgeo_utils.gdal2tiles import main
from osgeo.gdal import deprecation_warn


deprecation_warn('gdal2tiles')
sys.exit(main(sys.argv))
