from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    print("data")
    
    return '', 200
 
if __name__ == '__main__':
    app.run(port=5000)