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
    input = "write a rude message to gaslight people into being eco friendly"
    askGPT(input)

main()