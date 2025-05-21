#!/bin/bash
#
#export MAP_KEY_FIRMS=
source $HOME/.myKey.sh
export logDir=/mnt/data3/SILEX/VIIRS-HotSpot/log
export srcDir=/home/paugam/Src/Hs-FIRMS
source ~/Venv/firms/bin/activate
if [ ! -d "$logDir" ]; then
    mkdir -p "$logDir"
fi
export RUN_FE="False"

#NOAA20
python $srcDir/get-VIIRS4SILEX.py VIIRS_NOAA20_NRT >& $logDir/viirs_noaa20_nrt.log
exit_code=$?
if [ $exit_code -eq 19 ] && [ "$RUN_FE" != "True" ]; then
    export RUN_FE=True
fi

#NOAA21
python $srcDir/get-VIIRS4SILEX.py VIIRS_NOAA21_NRT >& $logDir/viirs_noaa21_nrt.log
exit_code=$?
if [ $exit_code -eq 19 ] && [ "$RUN_FE" != "True" ]; then
    export RUN_FE=True
fi

#SNPP
python $srcDir/get-VIIRS4SILEX.py VIIRS_SNPP_NRT   >& $logDir/viirs_snpp_nrt.log
exit_code=$?
if [ $exit_code -eq 19 ] && [ "$RUN_FE" != "True" ]; then
    export RUN_FE=True
fi

if [ "$RUN_FE" = "True" ]; then
    touch $logDir/../runFireEvent.txt
fi

