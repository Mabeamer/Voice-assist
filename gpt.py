from openai import OpenAI
import requests

client = OpenAI(api_key="")
def userDirection(userQuestion):
    clientResponse = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant who helps the user with their day to day requets"},
            {"role": "user", "content": userQuestion}
        ]
    )

    print(clientResponse.choices[0].message)

#userDirection('hi')

