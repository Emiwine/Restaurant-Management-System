

import qrcode

#define the menu of restaurant

menu = {
    'Margherita Pizza': 250,
    'Pepperoni Pizza': 300,
    'BBQ Chicken Pizza': 350,
    'Veggie Burger': 150,
    'Cheese Burger': 180,
    'Chicken Burger': 200,
    'Spaghetti Bolognese': 220,
    'Penne Arrabbiata': 200,
    'Caesar Salad': 120,
    'Greek Salad': 150,
    'Espresso': 80,
    'Cappuccino': 100,
    'Latte': 120,
    'Cold Coffee': 100,
    'Fresh Orange Juice': 90,
    'Lemonade': 60,
    'Chocolate Cake': 150,
    'Cheesecake': 180,
    'Ice Cream Sundae': 120,
}

# Greet
print("---------------Welcome to PYTHON Restaurant-------------\n")
for item, price in menu.items():
    print(f"{item} = Rs{price}")
print()

order_total = 0

while True:
    item = input("Enter the name of the item that you want to order (or type 'exit' to finish): ")
    if item.lower() == 'exit':
        break
    elif item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available.")

    another_item = input("Do you want to add another item? (Yes/No): ")
    if another_item.lower() != "yes":
        break

print(f"The total amount to pay is Rs{order_total}")






#Taking upi id as a input
upi_id = input("Enter the UPI ID = ")

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
    
#create the qrcode for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)


#display the qr code 

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()

