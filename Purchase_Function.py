# Purchase_Function.py
import csv
from datetime import datetime


# პროდუქციის შეძენის ფუნციონალის chaseManager კლასში გაერთიანება .

class PurchaseManager:
    def __init__(self, purchase_file):
        self.purchase_file = purchase_file
        self.purchases = self.load_purchase_history()

    def load_purchase_history(self):
        purchases = []
        try:
            with open(self.purchase_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['Product Code'] = int(row['Product Code'])
                    row['Quantity'] = int(row['Quantity'])
                    row['Cost'] = float(row['Cost'])
                    row['Date'] = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S')
                    purchases.append(row)
        except FileNotFoundError:
            print(f"No previous purchase history found in {self.purchase_file}.")
        return purchases


# პროდუქციის შეძენის ოპერაციის დამატება.

    def add_purchase(self, products):
        code = int(input("Enter product code to purchase: "))
        for product in products:
            if product['Product Code'] == code:
                quantity = int(input("Enter quantity: "))
                cost = float(input("Enter cost: "))
                date = datetime.now()
                purchase = {
                    'Product Code': code,
                    'Quantity': quantity,
                    'Cost': cost,
                    'Date': date.strftime('%Y-%m-%d %H:%M:%S')
                }
                self.purchases.append(purchase)
                self.save_purchase_to_csv()
                print("Purchase added successfully.")
                return
        print("Product code not found.")


# პროდუქციის შეძენის ისტორიული ჩანაწერების შენახვა ბაზაში.

    def save_purchase_to_csv(self):
        with open(self.purchase_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Product Code', 'Quantity', 'Cost', 'Date'])
            writer.writeheader()
            writer.writerows(self.purchases)
        print(f"Purchases saved to {self.purchase_file} successfully.")

# პროდუქციის შეძენების სიის ნახვის ფუნქციონალი.

    def view_purchases(self):
        if not self.purchases:
            print("No purchase history available.")
        else:
            print("\nPurchase History:")
            for purchase in self.purchases:
                print(f"Product Code: {purchase['Product Code']}, Quantity: {purchase['Quantity']}, Cost: {purchase['Cost']}, Date: {purchase['Date']}")
