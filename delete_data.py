from flask import Flask, request, jsonify

app = Flask(__name__)

# A dictionary to simulate stored data
data_store = {
    "message": "Hello World",
    "status": "active"
}

@app.route('/', methods=['DELETE'])
def delete_message():
    # Check if the message exists in the data_store
    if "message" in data_store:
        # Remove the message from the data_store
        deleted_message = data_store.pop("message")
        
        # Create a response confirming the deletion
        response = {
            "deleted_message": deleted_message,
            "status": "success"
        }
        return jsonify(response), 200
    else:
        # If the message doesn't exist, return an error
        return jsonify({"error": "No message found to delete"}), 404
    
@app.route("/")
def show():
    return jsonify(data_store);    

if __name__ == '__main__':
    app.run(debug=True,port=5005)
