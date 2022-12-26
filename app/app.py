#doc: https://www.youtube.com/watch?v=hDNxHiybF8Q&t=784s&ab_channel=PitoneProgrammatore
#doc mysql: https://pynative.com/python-mysql-database-connection/

from flask import *
import random
import mysql.connector

app = Flask(__name__)

email = " "
passw = " "

#connection to db
def db_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='smartlibrary',
                                         user='root',
                                         password='rootroot')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        return connection

#select query
def select_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    cursor.close()
    return record

#delete query
def delete_query(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

#insert query
def insert_query(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

#main page
@app.route("/") #http://127.0.0.1:5000
def index():
    sittingPerson = str(random.randint(0,100))
    connection = db_connection()
    record = select_query(connection,"SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory);")
    connection.close()
    return render_template("index.html", random=sittingPerson, record=record)

#login page
@app.route("/personal.html", methods=["POST","GET"])
def login_page():
    global email
    global passw
    try:
        if ((email == " " and passw == " ") or (email == None and passw == None)):
            email = request.form.get('email')
            passw = request.form.get('passw')
        connection = db_connection()
        record = select_query(connection,"SELECT * FROM smartlibrary.person WHERE (email = '" + email + "') AND (password = '" + passw + "');")
        recordMyInterest = select_query(connection,"SELECT person.id,category.idcategory,person.name,category.name FROM smartlibrary.interest, smartlibrary.category, smartlibrary.person WHERE ('"+ str(record[0][0]) + "' = interest.personID) AND (category.idcategory = interest.categoryID) AND (person.id = "+ str(record[0][0]) +");")
        allCategory = select_query(connection,"SELECT * FROM smartlibrary.category;")

        bookCat = []
        for r in recordMyInterest:
            bookCatTMP = select_query(connection,"SELECT * FROM (SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory)) myTable WHERE (myTable.name = '" + r[3] +"');")
            bookCat = bookCat + bookCatTMP
        connection.close()
    except:
        email = " "
        passw = " "
        record = []
        recordMyInterest = []
        allCategory = []
        bookCat = []
    return render_template("personal.html",record=record,lenrecord=len(record), recordMyInterest=recordMyInterest, allCategory=allCategory, bookCat=bookCat)

#logout
@app.route("/logout")
def logout():
    global email
    global passw
    email = " "
    passw = " "
    return redirect("/personal.html")
    
#delete preferences
@app.route("/<int:id>/<string:cat>/removepref", methods=["GET"])
def remove_pref(id,cat):
    connection = db_connection()
    record = select_query(connection,"SELECT interest.personID,category.name,category.idcategory FROM smartlibrary.interest, smartlibrary.category WHERE (interest.personID = '" + str(id) + "') AND (category.name = '" + cat + "') GROUP BY category.idcategory;")
    print(record)
    check = select_query(connection,"SELECT interest.personID, interest.categoryID FROM smartlibrary.interest WHERE (interest.personID = '"+ str(id) +"')")
    print(check)
    if (len(check) != 1):
        delete_query(connection,"DELETE FROM smartlibrary.interest WHERE (interest.personID = '" + str(record[0][0]) + "') AND (interest.categoryID = '" + str(record[0][2]) + "');")
    return redirect("/personal.html")

#add preferences
@app.route("/<int:id>/<string:cat>/addpref", methods=["GET"])
def add_pref(id,cat):
    connection = db_connection()
    record = select_query(connection,"SELECT interest.personID,category.name,category.idcategory FROM smartlibrary.interest, smartlibrary.category WHERE (interest.personID = '" + str(id) + "') AND (category.name = '" + cat + "') GROUP BY category.idcategory;")
    recordMyInterest = select_query(connection,"SELECT person.id,category.idcategory,person.name,category.name FROM smartlibrary.interest, smartlibrary.category, smartlibrary.person WHERE ('"+ str(record[0][0]) + "' = interest.personID) AND (category.idcategory = interest.categoryID) AND (person.id = "+ str(record[0][0]) +");")
    tmp = 0
    for i in recordMyInterest:
        if(i[3] == record[0][1]):
            tmp = 1 #elemento già presente
    if tmp == 0:
        insert_query(connection, "INSERT INTO smartlibrary.interest (personID,categoryID) VALUES ('" + str(id) + "','" + str(record[0][2]) + "');")
    return redirect("/personal.html")
    
#register page
@app.route("/register.html", methods=["GET"])
def register_page():
    return render_template("register.html")

#register
@app.route("/register.html/register", methods=["POST"])
def register():
    connection = db_connection()
    email1 = request.form.get('email')
    passw1 = request.form.get('passw')
    name = request.form.get('name')
    surname = request.form.get('surname')
    select = request.form.get('select')
    insert_query(connection, "INSERT INTO smartlibrary.person (name,surname,email,password,codiceCorso) VALUES ('" + str(name) + "','" + str(surname) + "','" + str(email1) + "','" + str(passw1) + "','" + str(select) + "');")
    id = select_query(connection,"SELECT person.id FROM smartlibrary.person WHERE (person.name = '"+ str(name) +"') AND (person.surname = '"+ str(surname) +"') AND (person.password = '"+ str(passw1) +"') AND (person.email = '"+ str(email1) +"');")
    idCat = select_query(connection,"SELECT category.idcategory FROM smartlibrary.category WHERE (category.name = '"+ str(select) +"');")
    insert_query(connection,"INSERT INTO smartlibrary.interest (personID,categoryID) VALUES ('" + str(id[0][0]) + "','" + str(idCat[0][0]) + "');")
    return redirect("/")


#check available books
@app.route("/books_available")
def books_available():
    connection = db_connection()
    record = select_query(connection,"SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory) AND (books.available = 0);")
    recordCategory = select_query(connection,"SELECT name FROM smartlibrary.category;")
    connection.close()
    return render_template("books.html",record=record, recordCategory=recordCategory)

#check not available books
@app.route("/books_notavailable")
def books_notavailable():
    connection = db_connection()
    record = select_query(connection,"SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory) AND (books.available = 1);")
    recordCategory = select_query(connection,"SELECT name FROM smartlibrary.category;")
    connection.close()
    return render_template("books.html",record=record, recordCategory=recordCategory)

#books page
@app.route("/books.html")
def books():
    connection = db_connection()
    record = select_query(connection,"SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory);")
    recordCategory = select_query(connection,"SELECT name FROM smartlibrary.category;")
    connection.close()
    return render_template("books.html",record=record, recordCategory=recordCategory)

#search books
@app.route("/search", methods=["POST"])
def search():
    search = request.form.get('src_title')
    connection = db_connection()
    record = select_query(connection,"SELECT * FROM (SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory)) myTable WHERE (myTable.title = '" + search +"');")
    if (len(record) == 0):
        record = select_query(connection,"SELECT * FROM (SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory)) myTable WHERE (myTable.autor = '" + search +"');")
    if (len(record) == 0):
        record = select_query(connection,"SELECT * FROM (SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory)) myTable WHERE (myTable.isbn = '" + search +"');")
    recordCategory = select_query(connection,"SELECT name FROM smartlibrary.category;")
    connection.close()
    return render_template("books.html",record=record, recordCategory=recordCategory)
    
#libri filtrati per categorie
@app.route("/<string:cat>/category")
def category(cat):
    connection = db_connection()
    record = select_query(connection,"SELECT * FROM (SELECT books.isbn,books.title,books.description,books.autor,category.name,books.pathimg,books.available FROM smartlibrary.books,smartlibrary.category WHERE (books.idcategory = category.idcategory)) myTable WHERE (myTable.name = '" + cat +"');")
    recordCategory = select_query(connection,"SELECT name FROM smartlibrary.category;")
    connection.close()
    return render_template("books.html",record=record, recordCategory=recordCategory)

#sistema il problema del concatenamento dei path per le categorie
@app.route("/<string:cat1>/<string:cat2>/category")
def control_category(cat1,cat2):
    return redirect("/" + cat2 + "/category")


# ------- html block ---------

#navbar menu
@app.route("/nav.html")
def nav():
    return render_template("nav.html")