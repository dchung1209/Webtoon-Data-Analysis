import re

class Cleaner():
  def __init__(self, df):
      self.df = df
    
  def convert(self, s):
    if "M" in s:
      return 1000000 * float(re.sub("[^0-9.\-]","", s))
    elif "," in s:
      return float(re.sub("[^0-9.\-]","", s))
  
  def clean(self):
     self.df = self.df.drop_duplicates()
     if isinstance(self.df['Like'][0], str):
        self.df['Like'] = self.df['Like'].apply(lambda x: self.convert(x))
  
  def get_df(self):
     self.clean()
     return self.df