import openai

openai.api_key = "Your API"

def get_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).get("choices", [])[0].text
    return response

while True:
    input_text = input("You: ")
    response = get_response(input_text)
    print("Chatbot:", response)
