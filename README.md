# Test-Project
This is a simple project to show I'm confident with python/django.

## The given task
>Imagine a pizza ordering services with following functionality:

>- Order pizza . Order data: pizza id, pizza size (30cm/50cm), customer name, customer address (just plain text)
>- Update order
>- Remove order
>- See a list of customer orders

>Tasks:

>1. Design Model/DB structure
>2. Design and implement API with Django (Rest) Framework for the described web service. Please note:
>	-  You don’t have to take care about authentication etc, we are just interested in structure and data modelling.
>	-  You don’t have to implement any UI, just the API endpoints
>3. Write test(s) for at least one of these endpoint(s)

## Installation
Clone this git repository:
```
git clone https://github.com/dakrulski/django-pizza-example.git
```
Create a python virtual enviroment for python3 and activate it.

Go to the project folder:
```
cd pizza
```
Install the requirements:
```
pip install -r requirements.txt
```
Run the migrations:
```
python manage.py migrate
```
Start the server:
```
python manage.py runserver
```
This will start the webserver on http://127.0.0.1:8000/.
## Documentation
The API endpoints are:

| Endpoint   | Description |
|------------|-----------|
| /order/list/\<customer name\>/ | to list the orders from a customer |
| /order/create/ | to create a new order |
| /modify/\<pizza id\>/ | to update and delete an order |

An automatic generated interactive API documentation can be found under http://127.0.0.1:8000/docs/ if the server is running.
## Tests
To run the tests:
```
python manage.py test
```

## If I had more time, these are the things I would have done differently
- Definitely implement authorization and authentication
- Make the models more complex. For example add a customer model with a referenced address model, add a model for different pizza sizes and add a model for prices with reference to the size model and to the pizza model.


