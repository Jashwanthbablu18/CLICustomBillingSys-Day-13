# Day 13 - Custom Billing System
# Topic: Functions, *args, **kwargs

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("💰 Welcome to Day 13 - Custom Billing System")
    print("🔹 Topic: Functions, *args and **kwargs in Python\n")

# This function is used to build the bill and displays the bill. And here *items represents *args and **extra_charges represents **kwargs.
def generate_bill(cust_name, *items, **extra_charges):

    # This displays the name of the customer
    print(f"\n🧾 Bill for: {cust_name}")
    print("-" * 40)

    # Total amount is initialised as 0
    total_amt = 0

    # Assuming items are tuples like ("ItemName", price) and looping over them
    for item in items:
        
        # unpacking the items like ("Apple,30") will assigned to itemName and price
        itemName, price = item

        # This displays the item along with the price
        print(f"🛒 {itemName}: ₹{price}")

        # Adds the price to total amount(Increments by price).
        total_amt += price

    print("-" * 40)

    # Displays the subtotal amount
    print(f"Subtotal: ₹{total_amt}")

    # This applies any additional fees or discounts, looping over the extra_charges retrives label and charge(Key -> label, value -> charge) 
    # from dictionary Some might be negative (like, discounts).
    for label, charge in extra_charges.items():
        # this displays lable with charge
        print(f"{label.title()}: ₹{charge}")
        # this updates the total amount with charge(+ve(Like Taxes) or -ve(Like discounts))
        total_amt += charge

    print("=" * 40)
    # This displays the total amount to be paid by adding the taxes or removing discounts
    print(f"Total Payable: ₹{total_amt}")
    print("=" * 40)

    # This whole function returns total amount.
    return total_amt 

# main:
def main():

    # Calls show_intro() to display introduction msg.
    show_intro()

    print("🙏 Welcome to Jash bros and co 😊")

    # Test case 1 - with extras: Means second 3 args are positional args they get collected into *items (*args) and last 3 args are keyword args 
    # they will get collected into **extra_charges (**kwargs). 
    generate_bill(
        "Jashwanth",
        ("Mangoes", 100),
        ("Bread", 40),
        ("Kisan Jam", 20),
        tax=10,
        discount=-5,
        delivery=15
    )

    # Test case 2 - with no extras: Means in this case the args are positional args(*items holds these tuples) and **extra_charges will be an 
    # empty dictionary{ } because any extra charges are applied in this case.
    generate_bill(
        "Navadeep",
        ("Notebook", 70),
        ("Pen", 10)
    )

    # Test case 3 - With empty bill no items and no extra charges
    generate_bill(
    "Empty Bill",
    # No items (no *args)
    # No extra charges (no **kwargs)
    )

### We can see many more test cases but for simplicity and for no confusion we can end up here.

    print("Thankyou for visiting 🙏, please visit again...😊😊😊")
# Entry point
if __name__ == "__main__":
    main()
