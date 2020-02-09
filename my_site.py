from flask import Flask, render_template
import json
import requests
import os
import pathlib
file_path = pathlib.Path(__file__).parent.absolute()
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
    with open (os.path.join(file_path,'static/page_data/timeline.json')) as timeline_file:
        timeline = json.load(timeline_file)
    timeline = add_descriptions(timeline)
    return render_template('timeline.html',
                            page_title = page,
                            timeline = timeline)

@app.route("/projects")
def projects():
    page = "Projects"
    body_text = "Not much content here yet!"
    return render_template('home.html',
                            page_title = page,
                            page_body_text = body_text)

def add_descriptions(file):
    for company,company_details in file.items():
        for role,role_details in company_details["roles"].items():
            if role_details["role_description"] =="":
                role_details["role_description"] = get_filler()
    return file

def get_filler(paragraphs=1, length='short'):
    text = requests.get('https://loripsum.net/api/{}/{}/plaintext'.format(paragraphs, length))
    return text.text

if __name__ == '__main__':
    app.run(debug=True)