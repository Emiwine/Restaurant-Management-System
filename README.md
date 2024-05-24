<h1>Restaurant Management System</h1>
<hr> 
Welcome to the Restaurant Management System, a Python-based project that simulates a restaurant ordering system. This system allows customers to place orders from a predefined menu, calculates the total cost, and generates QR codes for UPI payments via popular payment apps like PhonePe, Paytm, and Google Pay.

<hr>
Features
Display a restaurant menu with various items and their prices.
Allow customers to place orders by selecting items from the menu.
Calculate and display the total amount to be paid.
Generate UPI payment QR codes for PhonePe, Paytm, and Google Pay based on the provided UPI ID.
<hr>
Requirements
Python 3.x
qrcode library (for generating QR codes)
PIL library (for displaying QR codes)

<hr>
Place an Order:

The system will display a menu with available items and their prices.
Enter the name of the item you want to order. If you wish to stop ordering, type exit.
The system will ask if you want to add another item. Respond with Yes or No.
<hr>
Payment:

After placing the order, the system will ask for your UPI ID.
Based on the provided UPI ID, QR codes for PhonePe, Paytm, and Google Pay will be generated and displayed.
Scan the QR code with the respective payment app to complete the payment.

<hr>
<h4>Example Output</h4>

---------------Welcome to PYTHON Restaurant-------------

Margherita Pizza = Rs250
Pepperoni Pizza = Rs300
BBQ Chicken Pizza = Rs350
Veggie Burger = Rs150
Cheese Burger = Rs180
Chicken Burger = Rs200
Spaghetti Bolognese = Rs220
Penne Arrabbiata = Rs200
Caesar Salad = Rs120
Greek Salad = Rs150
Espresso = Rs80
Cappuccino = Rs100
Latte = Rs120
Cold Coffee = Rs100
Fresh Orange Juice = Rs90
Lemonade = Rs60
Chocolate Cake = Rs150
Cheesecake = Rs180
Ice Cream Sundae = Rs120

Enter the name of the item that you want to order (or type 'exit' to finish): Margherita Pizza
Your item Margherita Pizza has been added to your order.
Do you want to add another item? (Yes/No): Yes
Enter the name of the item that you want to order (or type 'exit' to finish): Espresso
Your item Espresso has been added to your order.
Do you want to add another item? (Yes/No): No
The total amount to pay is Rs330
Enter the UPI ID = your_upi_id@bank


