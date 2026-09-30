# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/product/Laptop/50000/Electronics

from flask import Flask
app = Flask(__name__)
 
@app.route('/product/<product_name>/<int:price>/<category>')
def product(product_name, price, category):
    discount = price * 0.10
    subtotal = price - discount
    gst = subtotal * 0.18
    final_price = subtotal + gst
 
    return f"""
    <h1>Product Information</h1>
    <b>Product Name:</b> {product_name}<br>
    <b>Category:</b> {category}<br>
    <b>Price:</b> {price}<br>
    <b>Discount (10%):</b> {discount}<br>
    <b>GST (18%):</b> {gst}<br>
    <b>Final Price:</b> {final_price:.2f}
    """
 
if __name__ == "__main__":
    app.run(debug=True)
