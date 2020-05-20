from flask import Flask,render_template
#render_template method used to fetch templates
app = Flask(__name__)#instantiating flask object with name which equals main
#if this script is imported to other script then name = filename and this script wont execute
@app.route('/home/')
def home():
    return render_template("home.html")
@app.route('/about/')#this is a decorator shud be followed by f/n to b executed
def about():
    return render_template("about.html")
if __name__=="__main__":
    app.run(debug=True)
