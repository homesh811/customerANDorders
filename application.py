from bottle import route, post, run, template, redirect, request
import database

database.set_up_database()
@route("/")
def get_index():
    redirect("/customer")

@route("/")
def get_index():
    redirect("/order")

@route("/customer")
def get_customer():
    key = request.query.get("key")
    if(key):
        customer = database.get_customer_search(key)
    else:
        customer = database.get_customer()
        key=""
    return template("customer.tpl",customer_order=customer, key=key)

@route("/order")
def get_orders():
    orders = database.get_orders()
    return template("order.tpl",customer_order=orders)

@route("/add1")
def get_add():
    return template("add_customer.tpl")

@route("/add2")
def get_orders():
    customers = database.get_customer()
    return template("add_order.tpl", customers = customers)

@post("/add1")
def post_add1():
    first_name = request.forms.get("first_name")
    last_name= request.forms.get("last_name")
    country= request.forms.get("country")
    database.add_customer(first_name,last_name,country)
    redirect("/customer")  

@post("/add2")
def post_add2():
    product = request.forms.get("product")
    total_amount= request.forms.get("total_amount")
    customerId = request.forms.get("customerId")

    database.add_orders(product,total_amount, customerId)
    redirect("/order")    

@route("/update1/<id>")
def get_update1(id):
    customer = database.get_customer(id)
    return template("update_customer.tpl", customer=customer[0])

@route("/update2/<id>")
def get_update2(id):
    orders = database.get_orders(id)
    customers = database.get_customer()
    return template("update_order.tpl", order=orders[0], customers=customers)

@post("/update1")
def post_update1():
    customer = request.forms.get("first_name")
    last_name = request.forms.get("last_name")
    country= request.forms.get("country")
    id = request.forms.get("id")
    database.update_customer(id, customer, last_name, country)
    redirect("/customer")    

@post("/update2")
def post_update2():
    product = request.forms.get("product")
    total_amount = request.forms.get("total_amount")
    id = request.forms.get("id")
    database.update_orders(id, product, total_amount)
    redirect("/order") 

@route("/delete1/<id>")
def get_delete1(id):
    database.delete_customer(id)
    redirect("/customer")

@route("/delete2/<id>")
def get_delete2(id):
    database.delete_orders(id)
    redirect("/order")

run(host='localhost', port=8080)