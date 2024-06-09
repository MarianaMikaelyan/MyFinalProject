import csv
from datetime import datetime

class SalesManager:
    def __init__(self, sales_file):
        self.sales_file = sales_file
        self.sales = self.load_sales()

    def load_sales(self):
        sales = []
        try:
            with open(self.sales_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['Product Code'] = int(row['Product Code'])
                    row['Quantity'] = int(row['Quantity'])
                    row['Price'] = float(row['Price'])
                    row['Date'] = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S')
                    sales.append(row)
        except FileNotFoundError:
            print(f"No previous sales history found in {self.sales_file}.")
        return sales


# პროდუქციის გაყიდვის ოპერაციის დამატება.

    def add_sale(self, products, purchases):
        code = int(input("Enter product code to sell: "))
        if code not in [product['Product Code'] for product in products]:
            print("Product code not found.")
            return
        
        quantity = int(input("Enter quantity to sell: "))
        if not self.check_available_quantity(code, quantity, purchases):
            print("Insufficient quantity available for sale.")
            return

        price = float(input("Enter selling price: "))
        date = datetime.now()

        sale = {'Product Code': code, 'Quantity': quantity, 'Price': price, 'Date': date.strftime('%Y-%m-%d %H:%M:%S')}
        self.sales.append(sale)
        self.save_sale_to_csv()
        print("Sale added successfully.")


# აქ ვამოწმებ ის რაოდენობა რასაც ვყიდი ხომ არ აღემატება შეძენის რაოდენობას.

    def check_available_quantity(self, code, quantity, purchases):
        available_quantity = sum(purchase['Quantity'] for purchase in purchases if purchase['Product Code'] == code)
        return available_quantity >= quantity


# პროდუქციის გაყიდვის ოპერაციების შენახვა ბაზაში.

    def save_sale_to_csv(self):
        with open(self.sales_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Product Code', 'Quantity', 'Price', 'Date'])
            writer.writeheader()
            writer.writerows(self.sales)
        print(f"Sales saved to {self.sales_file} successfully.")


# პროდუქციის გაყიდვის ოპერაციების სიის ნახვა.

    def view_sales(self):
        if not self.sales:
            print("No sales history available.")
        else:
            print("\nSales History:")
            for sale in self.sales:
                print(f"Product Code: {sale['Product Code']}, Quantity: {sale['Quantity']}, Price: {sale['Price']}, Date: {sale['Date']}")
