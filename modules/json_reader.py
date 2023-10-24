import pandas as pd
import gzip
import json 

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def get_df(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

# Load meta data 
# https://colab.research.google.com/drive/1Zv6MARGQcrBbLHyjPVVMZVnRWsRnVMpV#scrollTo=7igYuRaV4bF7
def metadata_loader(path):
  data = []
  with gzip.open(path) as f:
      for l in f:
          data.append(json.loads(l.strip()))
  df = pd.DataFrame.from_dict(data)
  return df 

