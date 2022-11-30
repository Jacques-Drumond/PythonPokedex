from flask import Flask, render_template, request
import os

app = Flask(__name__)

pic_folder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = pic_folder


@app.route("/pokedex")

def index():
    image1 = os.path.join(app.config['UPLOAD_FOLDER'], "pokedex.jpg")
    return render_template("pokedex.html", user_image = image1)


app.run(debug=True)