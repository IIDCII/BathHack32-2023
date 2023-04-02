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
    input = "hello"
    askGPT(input)

main()