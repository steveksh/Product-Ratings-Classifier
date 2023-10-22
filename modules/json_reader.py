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
