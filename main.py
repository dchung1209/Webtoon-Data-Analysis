import openai
from clean_utils import Cleaner
from query_utils import Queries
from chatGPT import HashtagGenerator

if __name__ == "__main__":
    df = Queries().df_query()
    df = Cleaner(df).get_df()
    print("Create a webtoon CSV file? [y/n]")
    answer = str(input())

    if (answer == "y"):
        print("Successfully created a CSV file")
        Queries().csv_query(df)

    print("Create hashtags? [y/n]")
    answer = str(input())
    guess = False

    if (answer == "y"):
       print("Enter the API key")
       openai.api_key = str(input())
       guess = True
  
    while (guess):
      random_target = df.sample(n = 1)
      print("Webtoon Info : ")
      print(random_target)
      description = Queries().description_query(random_target['URL'].iloc[0])
      print(f"Webtoon Title : {random_target['Title'].iloc[0]}")
      output = HashtagGenerator(random_target, description).guess_genre()
      print(f"Three Unique Hashtags : ")
      print(output)

      print("Stop? [y/n]")
      stop = str(input())
      if (stop == "y"):
         guess = False

