# Analysis_Module.py
import csv

class AnalysisManager:
    def __init__(self, product_manager, purchase_manager, sales_manager):
        self.product_manager = product_manager
        self.purchase_manager = purchase_manager
        self.sales_manager = sales_manager

    # მთლიანი გაყიდვების კალკულაცია
    def calculate_total_sales(self):
        total_sales = sum(sale['Price'] * sale['Quantity'] for sale in self.sales_manager.sales)
        return total_sales

    # მთლიანი შეძენების კალკულაცია
    def calculate_total_purchases(self):
        total_purchases = sum(purchase['Cost'] * purchase['Quantity'] for purchase in self.purchase_manager.purchases)
        return total_purchases

    # მთლიანი მოგება-ზარალის კალკულაცია
    def calculate_profit(self):
        total_sales = self.calculate_total_sales()
        total_purchases = self.calculate_total_purchases()
        profit = total_sales - total_purchases
        return profit

    # პროდუქციის მახასიათებლების ანალიზი.
    def calculate_inventory_status(self):
        inventory = {}
        for product in self.product_manager.products:
            product_code = product['Product Code']
            inventory[product_code] = {
                'Product Name': product['Product Name'],
                'Unit': product['Unit'],
                'Category Name': product.get('Category Name', 'Unknown Category'),  # Default to 'Unknown Category'
                'Quantity': 0
            }

        for purchase in self.purchase_manager.purchases:
            product_code = purchase['Product Code']
            if product_code in inventory:
                inventory[product_code]['Quantity'] += purchase['Quantity']

        for sale in self.sales_manager.sales:
            product_code = sale['Product Code']
            if product_code in inventory:
                inventory[product_code]['Quantity'] -= sale['Quantity']

        return inventory


    def display_analysis(self):
        total_sales = self.calculate_total_sales()
        total_purchases = self.calculate_total_purchases()
        profit = self.calculate_profit()
        inventory = self.calculate_inventory_status()

        print("\n--- Analysis Report ---")
        print(f"Total Sales: ${total_sales:.2f}")
        print(f"Total Purchases: ${total_purchases:.2f}")
        print(f"Profit: ${profit:.2f}")
        print("\nInventory Status:")
        for product_code, details in inventory.items():
            print(f"Product Code: {product_code}, Name: {details['Product Name']}, Quantity: {details['Quantity']}, Unit: {details['Unit']}, Category: {details['Category Name']}")
        print("-----------------------")

    # ანალიზის შენახვა ბაზაში.
    def save_analysis(self, filename='analysis.csv'):
        total_sales = self.calculate_total_sales()
        total_purchases = self.calculate_total_purchases()
        profit = self.calculate_profit()
        inventory = self.calculate_inventory_status()

        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Product Code', 'Product Name', 'Quantity', 'Unit', 'Category Name', 'Total Sales', 'Total Purchases', 'Profit'])
            writer.writeheader()
            for product_code, details in inventory.items():
                writer.writerow({
                    'Product Code': product_code,
                    'Product Name': details['Product Name'],
                    'Quantity': details['Quantity'],
                    'Unit': details['Unit'],
                    'Category Name': details['Category Name'],
                    'Total Sales': total_sales,
                    'Total Purchases': total_purchases,
                    'Profit': profit
                })
        print(f"Analysis data saved to {filename} successfully.")
