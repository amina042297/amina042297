

import openai

# OpenAI API key
openai.api_key = 'enter you api here'

def check_statement_with_gpt(statement):
    prompt = f"Check if the following statement is true or false:\n\n{statement}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=50,
        temperature=0.0,
    )
    return response['choices'][0]['message']['content'].strip()


