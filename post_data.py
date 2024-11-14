from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_post():
    # Get the JSON data sent in the POST request
    data = request.get_json()
    
    # If data is missing or malformed, return a 400 error
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid data, 'message' key missing"}), 400
    
    # Extract the 'message' field from the incoming data
    message = data['message']
    
    # Create a response containing the received message
    response = {
        "message_received": message,
        "status": "success"
    }
    
    # Return the response as JSON with a 200 status code
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True,port=5002)
