import pandas as pd
import os 

# let's create a simple function that tells us how many transactions we have used.
# We will use this in later examples
# Let's set your map key that was emailed to you. It should look something like 'abcdef1234567890abcdef1234567890'

MAP_KEY = os.getenv("MAP_KEY_FIRMS")
#MAP_KEY = 'abcdef1234567890abcdef1234567890'

# now let's check how many transactions we have
import pandas as pd
url = 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY

def get_transaction_count() :
  count = 0
  try:
    df = pd.read_json(url,  typ='series')
    count = df['current_transactions']
  except:
    print ("Error in our call.")
  return count

tcount = get_transaction_count()
print ('Our current transaction count is %i' % tcount)
