from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def create():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    # print("Name", request.form["name"])
    # print("Email", request.form["email"])
    return render_template("result.html")

@app.route("/danger", methods=["GET"])
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True) 