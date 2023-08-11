import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "YOUR OPENAI API KEY"

    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=2000,  # 4000 is max
                temperature=0.5  # 0-more acurate but less diverse, 1-less acuracy more diversity
            ).choices[0].text
            return response
        except:
            return "Switch to a paid billing plan or enter valid API key"


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
