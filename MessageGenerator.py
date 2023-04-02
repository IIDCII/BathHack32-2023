import openai

def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = text,
    temperature = 0.6,
    max_tokens = 150,
    )
    return print(response.choices[0].text)

def main():
    input = "make a message that's insulting and rude like kevin hart"
    askGPT(input)

main()