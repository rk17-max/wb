from flask import *
  
app = Flask(__name__) 
 
@app.route('/')  
def test():  
    return "hello, this is our first flask website";  




@app.route("/home")
def home():
    return "Welcome to our home page"


@app.route('/signup', methods=['POST'])
def signup():
    fullname = request.form['fullname']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    phone = request.form['phone']
    dob = request.form['dob']
    
    if password != confirm_password:
        return "Passwords do not match!"
    
 
    return f"welcome {fullname}"

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['email']
    passwrd = request.form['password']
    return f"Welcome {uname}"  
  
if __name__ =='__main__':  
    app.run(debug = True)  