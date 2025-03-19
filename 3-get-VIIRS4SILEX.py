import pandas as pd
import os 
import matplotlib.pyplot as plt 
from datetime import datetime
import sys

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


# Let's set your map key that was emailed to you. It should look something like 'abcdef1234567890abcdef1234567890'
    MAP_KEY = os.getenv("MAP_KEY_FIRMS")

    SILEX_Domain='-10,35,20,46'
    Sensor = sys.argv[1] # need to be either 'VIIRS_NOAA20_NRT'  'VIIRS_NOAA21_NRT'  or  'VIIRS_SNPP_NRT'

    dirout = '/mnt/data3/SILEX/FRP-HotSpot/{:s}/'.format(Sensor)
    os.makedirs(dirout, exist_ok=True)

# in this example let's look at VIIRS NOAA-20, entire world and the most recent day
    area_url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/{:s}/{:s}/{:s}/1'.format(MAP_KEY,Sensor,SILEX_Domain)
    
    url = 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY
    start_count = get_transaction_count(url)
    df_area = pd.read_csv(area_url)
    end_count = get_transaction_count(url)
    print ('We used %i transactions.' % (end_count-start_count))


    df_area.to_csv('{:s}/{:s}-{:s}.csv'.format(dirout,Sensor.lower(),datetime.now().strftime('%Y-%m-%d-%H%M')), index=False)



