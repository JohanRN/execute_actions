from flask import Flask, request
import requests

app = Flask(__name__)
url = "https://api.github.com/repos/JohanRN/execute_actions/dispatches"
headers = {
    "Authorization": "token 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",
    "Accept": "application/vnd.github.everest-preview+json",
}
data = {
    "event_type": "hello",
    # Optionally, you can include a payload
    # "client_payload": {
    #     "key1": "value1",
    #     "key2": "value2",
    # },
}

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    print("data")
    response = requests.post(url, headers=headers, json=data)
    print(response)
    # Check the response
    if response.status_code == 204:
        print("Event dispatched successfully.")
    else:
        print(f"Failed to dispatch event: {response.content}")
    return '', 200
 
if __name__ == '__main__':
    app.run(port=5000)