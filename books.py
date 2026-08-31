from flask import Flask, request

app = Flask(__name__)

books = [
    
    {"id" :  1 ,
    "title" :  "The forty rules of love",
    "author" : "elif shafak",
    "price" : 500000,
    "published_year" : 2000  
    },
    
    {
    "id" :  2,
    "title" :  "hello",
    "author" : "micle mg",
    "price" : 500000,
    "published_year" : 2000  
    },
    
    {
    "id" : 3,
    "title" :  "mkfbm",
    "author" : "vkofkb",
    "price" : 500000,
    "published_year" : 2000  
    },
]

@app.route("/books", methods=["GET"])
def get_books():
    return books

@app.route("/books/<int:id>",  methods=["GET"])
def get_bookid(id):
    for i in books:
        if i["id"] == id:
            return i
        
@app.route("/books", methods=["POST"])
def add_books():
    data = request.json
    books.append(data)
    return data

@app.route("/books/<int:id>", methods=["PUT"])
def edit_books(id):
    data = request.json
    
    for i in books:   
       if i["id"] == id:
           i.update(data)
           return i 
       
@app.route("/books/<int:id>", methods=["DELETE"])
def del_books(id):
    for i in books:
        if i["id"] == id :
            books.remove(i)
            return i 
        
        
if __name__ == "__main__":
    app.run(debug=True)