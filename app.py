from flask import Flask


#create flask
app = Flask(__name__)


#GET method
@app.route("/", methods=["GET"])
def home():
    return {
        "message": "Hello Flask"
    }
    
    
#GET /about method   
@app.route("/about", methods=["GET"])
def about():
    return {
        "message" : "my secsnd flask task "
    }
    
#GET /hello/<name> method   
@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return {
        "message" : f"hello {name}"
    }
    
    
if __name__ == "__main__":
    app.run(debug=True)