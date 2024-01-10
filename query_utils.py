import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from datetime import datetime

class Queries():
  def __init__(self):
    self.target = "https://www.webtoons.com/en/dailySchedule"
    self.r = requests.get(self.target)
    self.raw = BeautifulSoup(self.r.content, 'html.parser')

  def raw_query(self):
    return self.raw

  # Query the titles
  def title_query(self):
    title = [p.text for p in self.raw.find_all('p', {'class': 'subj'})]
    return title

  # Query the authors
  def author_query(self):
    author = [p.text for p in self.raw.find_all('p', {'class': 'author'})]
    return author

  # Query the genres
  def genre_query(self):
    genre = [p.text for p in self.raw.find_all('p', {'class': 'genre'})]
    return genre

  # Query # of likes
  def likes_query(self):
    likes = [p.text for p in self.raw.find_all('em', {'class': 'grade_num'})]
    return likes

  def days_query(self):
    days = [p.text for p in self.raw.find_all('em', {'class': 'grade_num'})]
    return days

  def urls_query(self):
    urls = [p['href'] for p in self.raw.find_all('a', {'class': 'daily_card_item'})]
    return urls
  
  def description_query(self, url):
    r = requests.get(url)
    raw = BeautifulSoup(r.content, 'html.parser')
    description = raw.find('meta', {'property': 'og:description'})['content']
    return description

  def dict_query(self):
    dict = {'Title': self.title_query(), 'Author': self.author_query(), 'Genre': self.genre_query(), 'Like': self.likes_query(), 'URL' : self.urls_query()}
    return dict

  def df_query(self):
    df = pd.DataFrame(self.dict_query())
    return df

  def csv_query(self, df):
    df.to_csv(f"naver_webtoon_{datetime.today().strftime('%Y%m%d')}.csv")
    # return df
