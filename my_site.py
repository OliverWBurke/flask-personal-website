from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    page = "Home"
    body_text = "Not much content here yet!"
    return render_template('home.html',
                            page_title = page,
                            page_body_text = body_text)

@app.route("/timeline")
def timeline():
    page = "Timeline"
    body_text = "Not much content here yet!"
    return render_template('home.html',
                            page_title = page,
                            page_body_text = body_text)

@app.route("/projects")
def projects():
    page = "Projects"
    body_text = "Not much content here yet!"
    return render_template('home.html',
                            page_title = page,
                            page_body_text = body_text)

if __name__ == '__main__':
    app.run(debug=True)