
import re
from query_utils import Queries
from chatGPT import guess_genre

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
    

if __name__ == "__main__":
    print("Create a webtoon CSV file? [y/n]")
    answer = str(input())

    if (answer == "y"):
        df = Queries().df_query()
        df = Cleaner(df).get_df()
    
        print("Successfully created a CSV file")
        Queries().csv_query(df)

