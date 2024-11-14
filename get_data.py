from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load the JSON data from the file
def load_data():
    with open('data.json') as json_file:
        return json.load(json_file)

@app.route('/data', methods=['POST'])
def get_data():
    data = load_data()  # Load the JSON data
    return jsonify(data)  # Return the data as JSON response

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run on port 5000
