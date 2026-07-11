from flask import Flask, request, Response, redirect, url_for, session
log = Flask(__name__)
log.secret_key = "SuperSecret"

#HomePage
@log.route("/", methods =["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username== "admin" and password == "123":
            session["user"] = username #store in Session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Creds",mimetype="text/plain")
        
    return '''
        <h2> LOGIN PAGE </h2>
        <form method="POST">
        Username = <input type = "text" name = "username"><br>
        Password = <input type = "password" name = "password"><br>
        <input type = "submit" value = "login">
        </form>
'''

# Welcome Page
@log.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome , {session["user"]}! </h2>
        <a href ="{url_for('logout')}">Logout</a>
    '''
    return redirect(url_for("login"))

# logout Page
@log.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
  
if __name__ == "__main__":
    log.run(debug=True)


