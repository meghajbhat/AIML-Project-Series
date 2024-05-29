#NAME : MEGHA BHAT
#EMAIL : meghajbhat@gmail.com

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def query_proxy_server(text, proxy_url='http://127.0.0.1:65432'):
    headers = {'Content-type': 'application/json'}
    data = json.dumps({'text': text})
    response = requests.post(proxy_url, headers=headers, data=data, verify=False)
    return response.json()

if __name__ == "__main__":
    while True:
        user_input = input("What do you want to ask ChatGPT? Type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break
        response = query_proxy_server(user_input)
        print("ChatGPT:", response.get('response', 'No response from server'))
