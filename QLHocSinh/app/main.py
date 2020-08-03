from flask import render_template

from app import app, dao


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def product_load():
    return render_template("product.html", products=dao.read_products())


if __name__ == "__main__":
    app.run(debug=True)
