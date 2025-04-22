running `run_viirs4SILEX.sh` creates in `dir_data` define in `config-SILEX.yaml` the following tree directory
```
├── FRP-HotSpot
│   ├── VIIRS_NOAA20_NRT
│   ├── VIIRS_NOAA21_NRT
│   └── VIIRS_SNPP_NRT
```
where in each directory you have the hourly hotspot data for the domain defined in `config-SILEX.yaml`.
For the SILEX campaign the config file lools like this:
```
# config-SILEX.yaml
general:
  domain: -10,35,20,52
  crs: 3035
hs:
  dir_data: /mnt/data3/SILEX/VIIRS-HotSpot
  sats: ['VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT', 'VIIRS_SNPP_NRT']
event:
  dir_data: /mnt/data3/SILEX/VIIRS-HotSpot/FireEvents
```
The downloaded csv files look like this:
```
latitude,longitude,bright_ti4,scan,track,acq_date,acq_time,satellite,instrument,confidence,version,bright_ti5,frp,daynight
44.01191,19.88847,301.34,0.39,0.36,2025-03-19,41,N,VIIRS,n,2.0NRT,268.57,0.95,N
44.07902,12.57333,299.04,0.57,0.43,2025-03-19,41,N,VIIRS,n,2.0NRT,278.34,1.9,N
44.2982,12.03841,307.8,0.4,0.44,2025-03-19,41,N,VIIRS,n,2.0NRT,271.38,0.8,N
44.44404,12.04109,296.6,0.4,0.45,2025-03-19,41,N,VIIRS,n,2.0NRT,271.68,0.73,N
44.55219,18.50483,317.56,0.39,0.36,2025-03-19,41,N,VIIRS,n,2.0NRT,270.26,1.24,N
44.85358,11.59002,296.15,0.43,0.46,2025-03-19,41,N,VIIRS,n,2.0NRT,273.48,0.61,N
44.85782,11.59075,305.17,0.43,0.46,2025-03-19,41,N,VIIRS,n,2.0NRT,274.65,1.09,N
45.14436,9.94362,336.99,0.52,0.5,2025-03-19,41,N,VIIRS,n,2.0NRT,277.1,5.29,N
45.14597,9.94478,336.63,0.52,0.5,2025-03-19,41,N,VIIRS,n,2.0NRT,278.92,4.4,N
```
set `run_viirs4SILEX.sh` in cron to run every hour. If there wasn't any sat obs in the zone area during this hour, then nothing happens.
