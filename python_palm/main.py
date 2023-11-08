import google.generativeai as palm
import os

palm.configure(api_key='YOUR_API_KEY')
while True:
    prompt = input("Write dude: ")
    if prompt == "exit":
        break
    else:
        response = palm.generate_text(prompt=prompt)
        print(response.result)
