import openai

class HashtagGenerator():
    def __init__(self, target, desc):
        self.target = target
        self.title = self.target['Title']
        self.genre = self.target['Genre']
        self.url = self.target['URL']
        self.desc = desc

    def guess_genre(self):
        prompt = f"Generate three catchy hashtags for the webtoon {self.title}. For some information, its genre is {self.genre} and its short description is : {self.desc}. All I need is three hashtags without any explanation added. Each hashtag length should be no longer than 10 words"
        completion = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a social media content generator. Generate hashtags based on the given context",
            },
            {
                "role": "user",
                "content": prompt,
            },
            ],
        )   
  
        return completion.choices[0].message.content


