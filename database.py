from peewee import *

db = SqliteDatabase('customer_order.db')
db.connect()

class Customer(Model):
    first_name = CharField()
    last_name  = CharField()
    country = CharField()
    class Meta:
        database = db

class Order(Model):
    product = CharField()
    total_amount  = CharField()
    cust_name=ForeignKeyField(Customer, backref='order', null=True)
    class Meta:
        database = db

def set_up_database():
    db.drop_tables([Customer, Order], safe=True)
    db.create_tables([Customer, Order])

def get_customer(id=None):
    if id==None:
        customers = Customer.select()
    else:
        customers = Customer.select().where(Customer.id == id)
    customers = [
        {
            'id':customer.id,
            'first_name':customer.first_name,
            'last_name':customer.last_name,
            'country':customer.country
        }
        for customer in customers
    ]
    return customers

def get_customer_search(key):
    customers = Customer.select().where(Customer.first_name.contains(key) | Customer.last_name.contains(key))
    customers = [
        {
            'id':customer.id,
            'first_name':customer.first_name,
            'last_name':customer.last_name,
            'country':customer.country
        }
        for customer in customers
    ]
    return customers

def get_orders(id=None):
    if id is None:
        orders = Order.select()
    else:
        orders = Order.select().where(Order.id == id)
    
    order_details = []
    for order in orders:
        customer_name = None
        if order.cust_name is not None:
            customer_name = order.cust_name.first_name
        
        order_info = {
            'id': order.id,
            'product': order.product,
            'total_amount': order.total_amount,
            'customer': customer_name
        }
        order_details.append(order_info)
    
    return order_details


def add_customer(first_name,last_name,country):
    customer = Customer(first_name=first_name,last_name=last_name,country=country)
    customer.save()

def add_orders(product,total_amount, customerId):
    orders = Order(product=product,total_amount=total_amount, cust_name=customerId)
    orders.save()

def update_customer(id, first_name,last_name,country):
    customer = Customer.select().where(Customer.id == id).get()
    customer.first_name = first_name
    customer.last_name = last_name
    customer.country = country
    customer.save()


def update_orders(id, product,total_amount):
    orders = Order.select().where(Order.id == id).get()
    orders.product = product
    orders.total_amount = total_amount
    orders.save()

def delete_customer(id):
    #Item.delete().where(Item.id == id).execute()
    customer = Customer.select().where(Customer.id == id).get()
    customer.delete_instance()

def delete_orders(id):
    #Item.delete().where(Item.id == id).execute()
    orders = Order.select().where(Order.id == id).get()
    orders.delete_instance()




