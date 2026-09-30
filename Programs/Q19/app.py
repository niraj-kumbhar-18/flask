# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/order

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "flasklab"
 
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        customer = request.form['customer']
        food_item = request.form['food_item']
        quantity = request.form['quantity']
        price = request.form['price']
 
        if customer == "" or food_item == "" or quantity == "" or price == "":
            flash("All fields are required!")
        else:
            quantity = int(quantity)
            price = float(price)
 
            subtotal = quantity * price
            service_charge = subtotal * 0.05
            gst = (subtotal + service_charge) * 0.18
            final_bill = subtotal + service_charge + gst
 
            flash(f"Customer: {customer}, Item: {food_item}, Subtotal: {subtotal}, Service Charge: {service_charge:.2f}, GST: {gst:.2f}, Final Bill: {final_bill:.2f}")
 
    return render_template('order.html')
 
if __name__ == "__main__":
    app.run(debug=True)
