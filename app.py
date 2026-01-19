from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "jewels_secret_key"

products = [
    {"id": 1, "name": "Gold Necklace", "price": 85000, "image": "https://images.unsplash.com/photo-1617038260897-7f7e6fa2f1bb?auto=format&fit=crop&w=600&q=80"},
    {"id": 2, "name": "Diamond Ring", "price": 125000, "image": "https://images.unsplash.com/photo-1585386959984-a41552231693?auto=format&fit=crop&w=600&q=80"},
    {"id": 3, "name": "Bridal Set", "price": 350000, "image": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=600&q=80"},
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", [])
    cart.append(product_id)
    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart_ids = session.get("cart", [])
    cart_items = [p for p in products if p["id"] in cart_ids]
    total = sum(p["price"] for p in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/clear")
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for("cart"))

if __name__ == "__main__":
    app.run(debug=True)
