import openai
import datetime 
class Chat(object):
    url = ""
    def __init__(self, api_key):
         openai.api_key = api_key

    def ask(self, keywords):
    # GPT-3 keywords
    #keywords = "workout home, home gym, fitness, good shape, health"

    # Generate article using GPT-3
        question = "Write an article about {keywords}. Include at least one related image."
        now_time = int(datetime.datetime.now().timestamp())
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"Write an article about {keywords}. Include at least one related image."),
            max_tokens=3000
        )
        result = (question, response["choices"][0]["text"], now_time, 0) 

        return result
