from flask import Flask,request,jsonify
 
app=Flask(__name__)
 
@app.route("/")
def home():
    return "hello World"
 
@app.route("/<string:name>",methods=['POST'])
def printname(name):
    return "Hi "+name
 
if __name__=="__main__":
    app.run(debug=True)