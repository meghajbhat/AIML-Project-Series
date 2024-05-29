from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests

conversation_history = []

class ProxyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global conversation_history
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        input_text = json.loads(post_data.decode('utf-8'))['text']
        conversation_history.append({'role': 'user', 'content': input_text})
        response_text = self.query_chatgpt(conversation_history)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'response': response_text}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def query_chatgpt(self, messages):
        openai_api_key = 'YOUR_OPEN_API_KEY_HERE'
        headers = {
            'Authorization': f'Bearer {openai_api_key}',
            'Content-Type': 'application/json',
        }
        payload = {
            'model': 'gpt-3.5-turbo-1106',  
            'messages': messages,
        }
        try:
            response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            response_json = response.json()
            conversation_history.append({'role': 'assistant', 'content': response_json.get('choices', [{}])[0].get('message', {'content': ''}).get('content', '').strip()})
            return conversation_history[-1]['content']
        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP error: {e}, response: {e.response.content.decode()}"
            print(error_msg)
            return "An error occurred while communicating with the ChatGPT API."
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
            return "An error occurred during the request to the ChatGPT API."

def run(server_class=HTTPServer, handler_class=ProxyHandler, port=65432):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is stopping...")
        httpd.server_close()
        print("Server stopped successfully.")

if __name__ == "__main__":
    run()
