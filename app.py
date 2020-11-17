from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommender")
def recommender():
    return render_template("input_form.html")


@app.route("/result", methods=["GET", "POST"])
def result():

    return render_template("result.html")


if __name__ == '__main__':
    app.run(debug=True)
