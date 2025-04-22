#!/bin/bash
#
#export MAP_KEY_FIRMS=
source $HOME/.myKey.sh
export logDir=/mnt/data3/SILEX/FRP-HotSpot/log
export srcDir=/home/paugam/Src/Hs-FIRMS
source ~/Venv/firms/bin/activate

python $srcDir/3-get-VIIRS4SILEX.py VIIRS_NOAA20_NRT >& $logDir/viirs_noaa20_nrt.log
python $srcDir/3-get-VIIRS4SILEX.py VIIRS_NOAA21_NRT >& $logDir/viirs_noaa21_nrt.log
python $srcDir/3-get-VIIRS4SILEX.py VIIRS_SNPP_NRT   >& $logDir/viirs_snpp_nrt.log
