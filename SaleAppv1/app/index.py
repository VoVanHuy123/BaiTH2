from flask import Flask,render_template, request
from utils import load_product
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/products")
def products():
    products = load_product()

    category_id = request.args.get("category_id",type=int)
    keyword = request.args.get("keyword","").lower()
    from_price = request.args.get("from_price",type=int)
    to_price = request.args.get("to_price",type=int)

    if category_id:
        products = [product for product in products if product["category_id"] == category_id]
    if keyword:
        products = [product for product in products if keyword in product["name"].lower()]
    if from_price is not None and to_price is not None:
        products = [product for product in products if from_price*1_000_000<= product["price"] <= to_price*1_000_000]

    return render_template("products.html", products=products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):

    products = load_product()


    product = next((p for p in products if p["id"]==product_id), None)
    if product:
        return render_template("product_detail.html", product=product)
    else:
        return "Product not found", 404


if __name__ == "__main__":
    app.run(debug=True)