#doc: https://www.youtube.com/watch?v=hDNxHiybF8Q&t=784s&ab_channel=PitoneProgrammatore
#doc mysql: https://pynative.com/python-mysql-database-connection/

from mongo import *
from flask import *
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

email = " "
passw = " "
seatsControl = 30 #notify changing seats
booksControl = 0 #notify changin availability

#fw: main page
@app.route("/") #http://127.0.0.1:5000
def index():
    entitiesCollection = mongo_connection_entities()
    #check if seats number change
    seats = get_seats(entitiesCollection)
    seatsID = checkSeats(seatsControl,int(seats))
    return render_template("index.html", seats = seats, seatsID = seatsID)

#fw: login page
@app.route("/personal.html", methods=["POST","GET"])
def login_page():
    global email
    global passw
    try:
        if ((email == " " and passw == " ") or (email == None and passw == None)):
            email = request.form.get('email')
            passw = request.form.get('passw')

        entitiesCollection = mongo_connection_entities()
        
        listPerson,listPersonInterest = login(entitiesCollection,email,passw)
            
        listCategory = list_all_category(entitiesCollection)

        listBook = []
        for cat in listPersonInterest:
            for elem in list_all_books_filtered_by_category(entitiesCollection,cat):
                listBook.append(elem)

    except:
        email = " "
        passw = " "
        listPerson = []
        listPersonInterest = []
        listCategory = []
        listBook = []
    return render_template("personal.html",record=listPerson,lenrecord=len(listPerson), recordMyInterest=listPersonInterest, allCategory=listCategory, bookCat=listBook)

#fw: logout
@app.route("/logout")
def logout():
    global email
    global passw
    email = " "
    passw = " "
    return redirect("/personal.html")
    
#fw: delete preferences
@app.route("/<string:id>/<string:cat>/removepref", methods=["GET"])
def remove_pref(id,cat):
    entitiesCollection = mongo_connection_entities()
    listPerson,listPersonInterest = login(entitiesCollection,email,passw)

    if (len(listPersonInterest) > 1):
        listPersonInterest.remove(cat)
        myquery = {"attrs.https://schema=org/email.value":email}
        newvalues = { "$set": { "attrs.https://schema=org/knowsAbout.value": listPersonInterest } }
        entitiesCollection.update_one(myquery, newvalues)

    return redirect("/personal.html")

#fw: add preferences
@app.route("/<string:id>/<string:cat>/addpref", methods=["GET"])
def add_pref(id,cat):
    entitiesCollection = mongo_connection_entities()
    listPerson,listPersonInterest = login(entitiesCollection,email,passw)
    
    if (cat not in listPersonInterest):
        listPersonInterest.append(cat)
        myquery = {"attrs.https://schema=org/email.value":email}
        newvalues = { "$set": { "attrs.https://schema=org/knowsAbout.value": listPersonInterest } }
        entitiesCollection.update_one(myquery, newvalues)

    return redirect("/personal.html")
    
#register page
@app.route("/register.html", methods=["GET"])
def register_page():
    return render_template("register.html")

#fw: register
@app.route("/register.html/register", methods=["POST"])
def register():
     
    entitiesCollection = mongo_connection_entities()

    email1 = request.form.get('email')
    passw1 = request.form.get('passw')
    name = request.form.get('name')
    surname = request.form.get('surname')
    faculty = request.form.get('select')

    insert_new_person(entitiesCollection,email1,passw1,name,surname,faculty)

    global email
    global passw
    email = " "
    passw = " "

    return redirect("/")


#fw: check available books
@app.route("/books_available")
def books_available():
    entitiesCollection = mongo_connection_entities()

    listBook = list_all_books_filtered_by_available(entitiesCollection,0)

    listCategory = list_all_category(entitiesCollection)
    
    return render_template("books.html",resultBooks=listBook, resultCategory=listCategory)

#fw: check not available books
@app.route("/books_notavailable")
def books_notavailable():

    entitiesCollection = mongo_connection_entities()

    listBook = list_all_books_filtered_by_available(entitiesCollection,1)

    listCategory = list_all_category(entitiesCollection)
    
    return render_template("books.html",resultBooks=listBook, resultCategory=listCategory)

#fw: books page 
@app.route("/books.html")
def books():
    entitiesCollection = mongo_connection_entities()
    #random_seats(entitiesCollection) #cambia il numero di persona sedute

    listBook = list_all_books(entitiesCollection)
        
    listCategory = list_all_category(entitiesCollection)

    print(listBook)

    #check if available books is change
    global booksControl
    tmpbooks = booksControl
    if booksControl == 1:
        booksControl = 0
  
    return render_template("books.html",resultBooks=listBook, resultCategory=listCategory, tmpbooks = tmpbooks)

#fw: search books
@app.route("/search", methods=["POST"])
def search():
    search = request.form.get('src_title')

    entitiesCollection = mongo_connection_entities()

    listBook = list_all_books_filtered_by_isbn(entitiesCollection,search)
    
    if len(listBook) == 0:
        listBook = list_all_books_filtered_by_autor(entitiesCollection,search)
    
    if len(listBook) == 0:
        listBook = list_all_books_filtered_by_title(entitiesCollection,search)

    listCategory = list_all_category(entitiesCollection)

    return render_template("books.html",resultBooks=listBook, resultCategory=listCategory)
    
#fw: libri filtrati per categorie
@app.route("/<string:cat>/category")
def category(cat):

    entitiesCollection = mongo_connection_entities()

    listBook = list_all_books_filtered_by_category(entitiesCollection,cat)

    listCategory = list_all_category(entitiesCollection)

    return render_template("books.html",resultBooks=listBook, resultCategory=listCategory)

#sistema il problema del concatenamento dei path per le categorie
@app.route("/<string:cat1>/<string:cat2>/category")
def control_category(cat1,cat2):
    return redirect("/" + cat2 + "/category")

#fw: staff
@app.route("/staff.html", methods=["POST","GET"])
def staff():

    entitiesCollection = mongo_connection_entities()

    user = request.form.get('user')
    passw = request.form.get('passw')

    if (user == "staff" and passw == "staff"):
        listCategory = list_all_category(entitiesCollection)
        return render_template("staffpage.html",resultCategory=listCategory)

    return render_template("staff.html")

#fw: insert one book
@app.route("/insert_book", methods=["POST"])
def insert_book():

    entitiesCollection = mongo_connection_entities()

    isbn = request.form.get('ISBN')

    if(request.form.get('action') == "savebook"):

        title = request.form.get('Title')
        description = request.form.get('Description')
        autor = request.form.get('Autor')
        category = request.form.get('select')

        insert_new_book(entitiesCollection,isbn,title,description,autor,category)
    else:
        remove_book_by_isbn(entitiesCollection,isbn)
    return redirect("/books.html")

#fw: insert one category
@app.route("/insert_category", methods=["POST"])
def insert_category():

    entitiesCollection = mongo_connection_entities()

    categoryName = request.form.get('CategoryName')

    listCategory = list_all_category(entitiesCollection)
    
    if(request.form.get('action') == "savecat"):
        if (categoryName not in listCategory):
            insert_new_category(entitiesCollection,categoryName)
    else:
        remove_category_by_name(entitiesCollection,categoryName)
        
    return redirect("/books.html")

#sensor handler
@app.route("/sensor.html")
def sensor_hander():
     return render_template("sensor.html")

#add or remove seats
@app.route("/sensor_seats", methods=["POST"])
def sensor_seats():
    add_or_remove_people = request.form.get('number_people')
    add_or_remove_people = int(add_or_remove_people)
    os.system("curl -iX POST 'http://iot-agent:7896/iot/json?k=testapikey&i=motion001' -H 'Content-Type: application/json' --data-raw '{\"m\": \"" + str(add_or_remove_people) + "\"}'")
    entitiesCollection = mongo_connection_entities()
    change_seats(entitiesCollection,add_or_remove_people)
    return redirect("/")

#modify book availability 
@app.route("/sensor_books", methods=["POST"])
def sensor_books():
    entitiesCollection = mongo_connection_entities()
    isbn = request.form.get('isbn')
    os.system("curl -iX POST 'http://iot-agent:7896/iot/json?k=testapikey&i=scanner001' -H 'Content-Type: application/json' --data-raw '{\"i\": \"" + str(isbn) + "\"}'")
    change_book_availability(entitiesCollection,isbn)
    #change available books state
    global booksControl
    booksControl = 1

    return redirect("/books.html")

# -------- SENSOR -------------

#sensorBooks
@app.route("/sensorBooksNotification", methods=["POST"])
def handle_notification_books():
    logger.info(json.loads(request.data))  
    return "notifica arrivata"

#sensorSeats
@app.route("/sensorSeatsNotification", methods=["POST"])
def handle_notification_seats():
    logger.info(json.loads(request.data))  
    return "notifica arrivata"

# ------- html block ---------

#navbar menu
@app.route("/nav.html")
def nav():
    return render_template("nav.html")

# ------- sensor control ----------

def checkSeats(seatsOld,seatsNow):
    global seatsControl
    if (seatsNow != seatsOld):
        seatsControl = seatsNow
        return 1
    return 0




# ------- test -------------

# MONGO: https://www.youtube.com/watch?v=agCkXvBQirA
@app.route("/test")
def test():
    print("Ciao Test")
    return render_template("nav.html")
    
if __name__ == '__main__':
    app.run(host='172.18.1.200', port=5050,debug=True)