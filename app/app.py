#doc: https://www.youtube.com/watch?v=hDNxHiybF8Q&t=784s&ab_channel=PitoneProgrammatore
#doc mysql: https://pynative.com/python-mysql-database-connection/

from mongo import *
from flask import *

app = Flask(__name__)

email = " "
passw = " "

#main page
@app.route("/") #http://127.0.0.1:5000
def index():
    libraryCollection = mongo_connection_library()
    record = libraryCollection.find_one({},{"_id":0, "seats":1})
    seats = record.get("seats")
    return render_template("index.html", random=seats)

#login page
@app.route("/personal.html", methods=["POST","GET"])
def login_page():
    global email
    global passw
    try:
        if ((email == " " and passw == " ") or (email == None and passw == None)):
            email = request.form.get('email')
            passw = request.form.get('passw')

        personCollection = mongo_connection_person()
        record = personCollection.find({"email":email, "password":passw},{"_id":0, "name":1, "surname":1, "email":1, "password":1, "courseCode":1, "preferences":1 })
        recordMyInterest = []
        recordPerson = []
        for rec in record:
            recordMyInterest = rec.get("preferences")
            recordPerson.append(rec)
        print(recordPerson)
        
        categoryCollection = mongo_connection_category()
        resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
        resultListcategory = []
        for res in resultcategory:
            resultListcategory.append(res)
            allCategory = res.get("name")

        booksCollection = mongo_connection_books()
        bookCat = []
        for cat in recordMyInterest:
            resultbooks = booksCollection.find({"category":cat},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
            for res in resultbooks:
                bookCat.append(res)

    except:
        email = " "
        passw = " "
        recordPerson = []
        recordMyInterest = []
        allCategory = []
        bookCat = []
    return render_template("personal.html",record=recordPerson,lenrecord=len(recordPerson), recordMyInterest=recordMyInterest, allCategory=allCategory, bookCat=bookCat)

#logout
@app.route("/logout")
def logout():
    global email
    global passw
    email = " "
    passw = " "
    return redirect("/personal.html")
    
#delete preferences
@app.route("/<string:id>/<string:cat>/removepref", methods=["GET"])
def remove_pref(id,cat):
    personCollection = mongo_connection_person()
    record = personCollection.find({"email":email, "password":passw},{"_id":0, "name":1, "surname":1, "email":1, "password":1, "courseCode":1, "preferences":1 })
    recordMyInterest = []
    recordPerson = []
    for rec in record:
        recordMyInterest = rec.get("preferences")
        recordPerson.append(rec)

    if (len(recordMyInterest) > 1):
        recordMyInterest.remove(cat)
        myquery = {"email": email, "password": passw}
        newvalues = { "$set": { "preferences": recordMyInterest } }
        personCollection.update_one(myquery, newvalues)

    return redirect("/personal.html")

#add preferences
@app.route("/<string:id>/<string:cat>/addpref", methods=["GET"])
def add_pref(id,cat):
    personCollection = mongo_connection_person()
    record = personCollection.find({"email":email, "password":passw},{"_id":0, "name":1, "surname":1, "email":1, "password":1, "courseCode":1, "preferences":1 })
    recordMyInterest = []
    recordPerson = []
    for rec in record:
        recordMyInterest = rec.get("preferences")
        recordPerson.append(rec)

    if (cat not in recordMyInterest):
        recordMyInterest.append(cat)
        myquery = {"email": email, "password": passw}
        newvalues = { "$set": { "preferences": recordMyInterest } }
        personCollection.update_one(myquery, newvalues)

    return redirect("/personal.html")
    
#register page
@app.route("/register.html", methods=["GET"])
def register_page():
    return render_template("register.html")

#register
@app.route("/register.html/register", methods=["POST"])
def register():
    personCollection = mongo_connection_person()

    email1 = request.form.get('email')
    passw1 = request.form.get('passw')
    name = request.form.get('name')
    surname = request.form.get('surname')
    select = request.form.get('select')
    user = {"name":name, "surname":surname, "email":email1, "password": passw1, "courseCode": select, "preferences": [select]}
    personCollection.insert_one(user)

    global email
    global passw
    email = " "
    passw = " "

    return redirect("/")


#check available books
@app.route("/books_available")
def books_available():
    booksCollection = mongo_connection_books()

    resultbooks = booksCollection.find({"available":0},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
    resultListbooks = []
    for res in resultbooks:
        resultListbooks.append(res)

    categoryCollection = mongo_connection_category()
    resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
    resultListcategory = []
    for res in resultcategory:
        resultListcategory.append(res)
        category = res.get("name")
    
    return render_template("books.html",resultBooks=resultListbooks, resultCategory=category)

#check not available books
@app.route("/books_notavailable")
def books_notavailable():

    booksCollection = mongo_connection_books()

    resultbooks = booksCollection.find({"available":1},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
    resultListbooks = []
    for res in resultbooks:
        resultListbooks.append(res)

    categoryCollection = mongo_connection_category()
    resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
    resultListcategory = []
    for res in resultcategory:
        resultListcategory.append(res)
        category = res.get("name")

    return render_template("books.html",resultBooks=resultListbooks, resultCategory=category)

#books page
@app.route("/books.html")
def books():

    booksCollection = mongo_connection_books()

    resultbooks = booksCollection.find({},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
    resultListbooks = []
    for res in resultbooks:
        resultListbooks.append(res)

    categoryCollection = mongo_connection_category()
    resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
    resultListcategory = []
    for res in resultcategory:
        resultListcategory.append(res)
        category = res.get("name")

    return render_template("books.html",resultBooks=resultListbooks, resultCategory=category)

#search books
@app.route("/search", methods=["POST"])
def search():
    search = request.form.get('src_title')

    booksCollection = mongo_connection_books()

    resultbooks = booksCollection.find({"title":search},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
    resultListbooks = []
    for res in resultbooks:
        resultListbooks.append(res)

    if len(resultListbooks) == 0:
        resultbooks = booksCollection.find({"autor":search},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
        resultListbooks = []
        for res in resultbooks:
            resultListbooks.append(res)
    if len(resultListbooks) == 0:
        resultbooks = booksCollection.find({"isbn":search},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
        resultListbooks = []
        for res in resultbooks:
            resultListbooks.append(res)

    categoryCollection = mongo_connection_category()
    resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
    resultListcategory = []
    for res in resultcategory:
        resultListcategory.append(res)
        category = res.get("name")

    return render_template("books.html",resultBooks=resultListbooks, resultCategory=category)
    
#libri filtrati per categorie
@app.route("/<string:cat>/category")
def category(cat):

    booksCollection = mongo_connection_books()

    resultbooks = booksCollection.find({"category":cat},{"_id":0, "isbn":1, "title":1, "description":1, "autor":1, "pathimg":1, "available":1, "category":1 })
    resultListbooks = []
    for res in resultbooks:
        resultListbooks.append(res)

    categoryCollection = mongo_connection_category()
    resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
    resultListcategory = []
    for res in resultcategory:
        resultListcategory.append(res)
        category = res.get("name")
    return render_template("books.html",resultBooks=resultListbooks, resultCategory=category)

#sistema il problema del concatenamento dei path per le categorie
@app.route("/<string:cat1>/<string:cat2>/category")
def control_category(cat1,cat2):
    return redirect("/" + cat2 + "/category")

#staff
@app.route("/staff.html", methods=["POST","GET"])
def staff():
    user = request.form.get('user')
    passw = request.form.get('passw')
    if (user == "staff" and passw == "staff"):
        categoryCollection = mongo_connection_category()
        resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
        resultListcategory = []
        for res in resultcategory:
            resultListcategory.append(res)
            category = res.get("name")
        return render_template("staffpage.html",resultCategory=category)
    return render_template("staff.html")

#insert one book
@app.route("/insert_book", methods=["POST"])
def insert_book():

    if(request.form.get('action') == "savebook"):
        isbn = request.form.get('ISBN')
        title = request.form.get('Title')
        description = request.form.get('Description')
        autor = request.form.get('Autor')
        category = request.form.get('select')

        booksCollection = mongo_connection_books()
        book = {"isbn":isbn, "title":title, "description":description, "autor": autor, "pathimg":"static/standardbook.jpeg", "available":0, "category":category}
        booksCollection.insert_one(book)
    else:
        isbn = request.form.get('ISBN')
        booksCollection = mongo_connection_books()
        booksCollection.delete_one({"isbn":str(isbn)})
    return redirect("/books.html")

#insert one category
@app.route("/insert_category", methods=["POST"])
def insert_category():
    
    if(request.form.get('action') == "savecat"):
        categoryName = request.form.get('CategoryName')

        categoryCollection = mongo_connection_category()
        resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
        resultListcategory = []
        for res in resultcategory:
            resultListcategory.append(res)
            category = res.get("name")
        
        resultcategoryID = categoryCollection.find_one({},{"_id":1, "name":0 })

        if (categoryName not in category):
            myquery = {"_id": resultcategoryID.get("_id")}
            category.append(categoryName)
            print(category)
            newvalues = { "$set": { "name": category } }
            categoryCollection.update_one(myquery, newvalues)
    else:
        categoryName = request.form.get('CategoryName')
        categoryCollection = mongo_connection_category()
        resultcategory = categoryCollection.find({},{"_id":0, "name":1 })
        resultListcategory = []
        for res in resultcategory:
            resultListcategory.append(res)
            category = res.get("name")
        category.remove(categoryName)
        resultcategoryID = categoryCollection.find_one({},{"_id":1, "name":0 })
        myquery = {"_id": resultcategoryID.get("_id")}
        newvalues = { "$set": { "name": category } }
        categoryCollection.update_one(myquery, newvalues)
        
    return redirect("/books.html")

# ------- html block ---------

#navbar menu
@app.route("/nav.html")
def nav():
    return render_template("nav.html")


# ------- test -------------

# MONGO: https://www.youtube.com/watch?v=agCkXvBQirA
@app.route("/test")
def test():
    client = MongoClient("mongodb://localhost:27017")
    db = client.bigdata
    personCollection = db.person
    result = personCollection.find({},{"_id":0, "name":1, "surname":1, "email":1, "password":1, "courseCode":1, "preferences":1 })
    return render_template("nav.html")
    