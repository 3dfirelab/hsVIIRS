import pandas as pd
import glob 
import sys

data_dir = '/mnt/data3/SILEX/VIIRS-HotSpot-202504/'

satnames = ['VIIRS_SNPP_NRT', 'VIIRS_NOAA20_NRT', 'VIIRS_NOAA21_NRT']

for satname in satnames: 
    dirIn = '{:s}/{:s}/'.format(data_dir,satname)
    fileIn = glob.glob(dirIn+'*.csv')[0]
    # Load the CSV file
    df = pd.read_csv(fileIn)

    # Ensure acq_time is zero-padded to 4 digits
    df['acq_time'] = df['acq_time'].apply(lambda x: f"{int(x):04d}")

    # Extract the hour part and zero out minutes
    df['acq_hour'] = df['acq_time'].str[:2] + '00'

    # Group by acquisition date and save each group as a separate CSV
    for (date, hour), group in df.groupby(['acq_date', 'acq_hour']):
    #for date, group in df.groupby('acq_date'):
        filename = '{:s}/{:s}_{:s}-{:s}.csv'.format(dirIn,satname.lower(),date,hour)
        group.to_csv(filename, index=False)
        print(f'Saved {filename} with {len(group)} records.')

