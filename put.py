from flask import Flask, request, jsonify

app = Flask(__name__)

# A dictionary to hold a message for demo purposes
data_store = {
    "message": "Hello World"
}

@app.route('/', methods=['PUT'])
def update_message():
    # Get the JSON data sent in the PUT request
    data = request.get_json()
    
    # If data is missing or doesn't have 'message', return a 400 error
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid data, 'message' key missing"}), 400
    
    # Update the message in the data store
    data_store['message'] = data['message']
    
    # Create a response containing the updated message
    response = {
        "updated_message": data_store['message'],
        "status": "success"
    }
    
    # Return the response as JSON with a 200 status code
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True,port=5003)
