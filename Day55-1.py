from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World! </h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media.tenor.com/L5wtm55bKhQAAAAM/cute-cat.gif" width=200 height=200>'

def make_bold(function):
    print("make_bold is called")
    
    def wrapper():
        print("Wrapper is called")
        result = function()
        return f"<b>{result}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        result = function()
        return f"<em>{result}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        result = function()
        return f"<u>{result}</u>"
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

print(say_bye())

if __name__ == "__main__":
    app.run(debug=True)

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user)
