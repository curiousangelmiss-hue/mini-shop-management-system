# Mini Shop Management System

# -----------------------------
# Product Data
# -----------------------------

products = {
    "p01": {
        "product_name": "pen",
        "price": 30,
        "quantity": 10,
        "category": "Stationery"
    },

    "p02": {
        "product_name": "pencil",
        "price": 10,
        "quantity": 20,
        "category": "Stationery"
    },

    "p03": {
        "product_name": "book",
        "price": 300,
        "quantity": 20,
        "category": "Stationery"
    },

    "p04": {
        "product_name": "journals",
        "price": 450,
        "quantity": 20,
        "category": "Stationery"
    }
}

# Sales record
sales = []

# Categories
categories = ("Stationery", "Electronics", "Grocery")

# Unique categories used in the shop
unique_categories = set()


# -----------------------------
# Add Product
# -----------------------------

def add_product():
    product_id = input("Enter Product ID: ").strip()

    if product_id in products:
        print("Product ID already exists!")
        return

    product_name = input("Enter Product Name: ").strip()
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    print("Available Categories:", categories)
    category = input("Enter Category: ").strip()

    if category not in categories:
        print("Invalid category!")
        return

    products[product_id] = {
        "product_name": product_name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    unique_categories.add(category)

    print("Product added successfully!")


# -----------------------------
# View Products
# -----------------------------

def view_products():
    if not products:
        print("No products available.")
        return

    print("\n========== ALL PRODUCTS ==========")

    for product_id, product in products.items():
        print("\nProduct ID:", product_id)
        print("Name:", product["product_name"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
        print("Category:", product["category"])


# -----------------------------
# Search Product
# -----------------------------

def search_product():
    product_id = input("Enter Product ID: ").strip()

    if product_id in products:
        product = products[product_id]

        print("\nProduct Found!")
        print("Product ID:", product_id)
        print("Product Name:", product["product_name"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
        print("Category:", product["category"])

    else:
        print("Product Not Found!")


# -----------------------------
# Sell Product
# -----------------------------

def sell_product():
    product_id = input("Enter Product ID: ").strip()

    if product_id not in products:
        print("Product not found!")
        return

    sale_quantity = int(input("Enter quantity to sell: "))

    if sale_quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    available_quantity = products[product_id]["quantity"]

    if sale_quantity > available_quantity:
        print("Insufficient stock!")
        print("Available stock:", available_quantity)
        return

    price = products[product_id]["price"]

    total_amount = price * sale_quantity

    products[product_id]["quantity"] -= sale_quantity

    sales.append({
        "product_id": product_id,
        "quantity": sale_quantity,
        "total": total_amount
    })

    print("\nSale successful!")
    print("Total amount: Rs.", total_amount)
    print("Remaining stock:", products[product_id]["quantity"])


# -----------------------------
# Low Stock Products
# -----------------------------

def low_stock():
    print("\n========== LOW STOCK PRODUCTS ==========")

    found = False

    for product_id, product in products.items():

        if product["quantity"] < 5:
            found = True

            print(
                product_id,
                "-",
                product["product_name"],
                "-",
                product["quantity"],
                "remaining"
            )

    if not found:
        print("No low-stock products.")


# -----------------------------
# Sales Summary
# -----------------------------

def sales_summary():
    total_products_sold = 0
    total_sales = 0

    for sale in sales:
        total_products_sold += sale["quantity"]
        total_sales += sale["total"]

    print("\n========== SALES SUMMARY ==========")
    print("Total Products Sold:", total_products_sold)
    print("Total Sales Amount: Rs.", total_sales)


# -----------------------------
# Main Menu
# -----------------------------

def main_menu():

    menu = {
        "1": ("Add Product", add_product),
        "2": ("View Products", view_products),
        "3": ("Search Product", search_product),
        "4": ("Sell Product", sell_product),
        "5": ("Low Stock Products", low_stock),
        "6": ("Sales Summary", sales_summary)
    }

    while True:

        print("\n========== MINI SHOP MANAGEMENT SYSTEM ==========")

        for number, option in menu.items():
            print(number + ".", option[0])

        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in menu:
            menu[choice][1]()

        elif choice == "7":
            print("\nThank you for using Mini Shop Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# -----------------------------
# Start Program
# -----------------------------

main_menu()
