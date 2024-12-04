# # Pyhton Decorator Function
# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("Hello")

# @delay_decorator
# def say_bye():
#     print("Bye")

# def say_greeting():
#     print("How are you?")

# decorated_function = delay_decorator(say_greeting)
# decorated_function()

from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World! </h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media.tenor.com/L5wtm55bKhQAAAAM/cute-cat.gif" width=200 height=200>'

@app.route('/bye')
def say_bye():
    return "<u><em><b>Bye!</b></em></u>"

# @app.route('/username/<path:name>')
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name} Prajapati, You are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)