from flask import Flask, request, jsonify
import pytest

app = Flask(__name__)

# A dictionary to simulate stored data
data_store = {
    "message": "Hello World",
    "status": "active"
}

@app.route('/', methods=['PATCH'])
def patch_message():
    # Get the JSON data sent in the PATCH request
    data = request.get_json()
    
    # If there's no data or it's not a dictionary, return a 400 error
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid data"}), 400

    # Update the data_store dictionary only for the keys that exist in the request
    for key, value in data.items():
        if key in data_store:
            data_store[key] = value

    # Create a response containing the updated message
    response = {
        "updated_data": data_store,
        "status": "success"
    }
    
    # Return the updated dictionary as JSON with a 200 status code
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True,port=5004)
