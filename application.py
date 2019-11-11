import os
from flask import Flask, session, redirect, render_template, request, jsonify, flash
from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/main")
def main():
    return render_template("main.html")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/loginSubmit", methods=["GET", "POST"])
def loginSubmit():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("error.html", message="Please Provide Username")
        elif not request.form.get("password"):
            return render_template("error.html", message="must provide password")
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                            {"username": request.form.get("username")})
        result = rows.fetchone()
        if result == None or not check_password_hash(result[1], request.form.get("password")):
            return render_template("error.html", message="Invalid Username or Password")                
        session["user_id"] = result[0]
        session["user_name"] = result[1]  
        return render_template("main.html") 
    else:
        return render_template("login.html")      
@app.route("/registerSubmit", methods=["GET", "POST"])
def registerSubmit():
    """ Register user """
    
    # Forget any user_id
    session.clear()
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", message="must provide username")

        # Query database for username
        userCheck = db.execute("SELECT * FROM users WHERE username = :username",
                          {"username":request.form.get("username")}).fetchone()

        # Check if username already exist
        if userCheck:
            return render_template("error.html", message="username already exist")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("error.html", message="must provide password")

        elif not request.form.get("email"):
            return render_template("error.html", message="Please Enter Email")

        elif not request.form.get("contact"):
            return render_template("error.html", message="Please enter Contact")

        # Hash user's password to store in DB
        hashedPassword = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        
        # Insert register into DB
        db.execute("INSERT INTO users VALUES (:username, :password, :email, :contact)",
                            {"username":request.form.get("username"), 
                             "password":hashedPassword,
                             "email":request.form.get("email"),
                             "contact":request.form.get("contact")
                             })

        # Commit changes to database
        db.commit()

        flash('Account created', 'info')

        # Redirect user to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

