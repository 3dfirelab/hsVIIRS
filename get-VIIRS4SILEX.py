import pandas as pd
import os 
import matplotlib.pyplot as plt 
import sys
from pathlib import Path
import importlib 
from datetime import datetime, timezone

#home brewed
import hstools

def get_transaction_count(url) :
  count = 0
  try:
    df = pd.read_json(url,  typ='series')
    count = df['current_transactions']
  except:
    print ("Error in our call.")
  return count

#############################
if __name__ == '__main__':
#############################

    importlib.reload(hstools)
    
    script_dir = Path(__file__).resolve().parent
    params = hstools.load_config(str(script_dir)+'/config-SILEX.yaml')
    satname = sys.argv[1] # need to be either 'VIIRS_NOAA20_NRT'  'VIIRS_NOAA21_NRT'  or  'VIIRS_SNPP_NRT'
    
# Let's set your map key that was emailed to you. It should look something like 'abcdef1234567890abcdef1234567890'
    MAP_KEY = os.getenv("MAP_KEY_FIRMS")

    SILEX_Domain= params['general']['domain']

    dirout = '{:s}/{:s}/'.format(params['hs']['dir_data'],satname)
    os.makedirs(dirout, exist_ok=True)

# in this example let's look at VIIRS NOAA-20, entire world and the most recent day
    area_url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/{:s}/{:s}/{:s}/1'.format(MAP_KEY,satname,SILEX_Domain)
    
    url = 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY
    start_count = get_transaction_count(url)
    df_area = pd.read_csv(area_url)
    end_count = get_transaction_count(url)
    print ('We used %i transactions.' % (end_count-start_count))

    if len(df_area) == 0: 
        print('no fire detected yet')
        sys.exit()

    #remove from df all previous hs of the same day
    day = df_area['acq_date'].iloc[0]
    df_aera_prev = hstools.load_hs4oneday(day,satname,params)
    df_aera_prev = df_aera_prev.drop(columns=['geometry', 'timestamp'])
    if len(df_aera_prev)!= 0: 
        df_complement = pd.concat([df_area, df_aera_prev, df_aera_prev,]).drop_duplicates(keep=False)
    else: 
        df_complement = df_area
    if len(df_complement) == 0: 
        print('no new fire detected yet')
        sys.exit()
    
    print('save {:d} new hot spot'.format(len(df_complement)))
    df_complement.to_csv('{:s}/{:s}-{:s}.csv'.format(dirout,satname.lower(),datetime.now(timezone.utc).strftime('%Y-%m-%d-%H%M')), index=False)

    sys.exit(19) 

