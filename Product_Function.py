import csv
# პროდუქციის ფუნქციებს ვაერთიანებ ProductManager კლასში.
class ProductManager:
    def __init__(self, category_file, product_file):
        self.category_file = category_file
        self.product_file = product_file
        self.categories = self.load_categories()
        self.products = self.load_products()


    def load_categories(self):
        categories = {}
        try:
            with open(self.category_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    categories[int(row['Category Code'])] = row['Category Name']
        except FileNotFoundError:
            print(f"No category data found in {self.category_file}.")
        return categories

    def load_products(self):
        products = []
        try:
            with open(self.product_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['Product Code'] = int(row['Product Code'])
                    row['Category Code'] = int(row['Category Code'])
                    category_name = self.categories.get(row['Category Code'], 'Unknown Category')
                    row['Category Name'] = category_name
                    products.append(row)
        except FileNotFoundError:
            print(f"No product data found in {self.product_file}.")
        return products
    
# პროდუქციის ცნობარების შექმნა, პროდუქტის დამატების ფუნქციონალი.
    
    def add_product(self):
        code = int(input("Enter product code: "))
        name = input("Enter product name: ")
        unit = input("Enter unit: ")
        category_code = int(input(f"Enter category code ({list(self.categories.keys())}): "))
        if category_code not in self.categories:
            print("Invalid category code.")
            return
        category_name = self.categories.get(category_code, 'Unknown Category')
        product = {
            'Product Code': code,
            'Product Name': name,
            'Unit': unit,
            'Category Code': category_code,
            'Category Name': category_name
        }
        self.products.append(product)
        print("Product added successfully.")

# პროდუქციის ცნობარების შექმნა, პროდუქტის რედაქტირების ფუნქციონალი.

    def edit_product(self):
        code = int(input("Enter product code to edit: "))
        for product in self.products:
            if product['Product Code'] == code:
                print(f"Editing product: {product}")
                name = input(f"Enter new product name (current: {product['Product Name']}): ") or product['Product Name']
                unit = input(f"Enter new unit (current: {product['Unit']}): ") or product['Unit']
                category_code = int(input(f"Enter new category code ({list(self.categories.keys())}, current: {product['Category Code']}): ")) or product['Category Code']
                if category_code not in self.categories:
                    print("Invalid category code.")
                    return
                product['Product Name'] = name
                product['Unit'] = unit
                product['Category Code'] = category_code
                print("Product edited successfully.")
                return
        print("Product code not found.")

# პროდუქციის ცნობარების შექმნა, პროდუქტის წაშლის ფუნქციონალი.

    def delete_product(self):
        code = int(input("Enter product code to delete: "))
        for product in self.products:
            if product['Product Code'] == code:
                self.products.remove(product)
                print("Product deleted successfully.")
                return
        print("Product code not found.")

# პროდუქციის ცნობარების შექმნა, პროდუქტის სიის ნახვის ფუნქციონალი.
    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("\nProduct List:")
            for product in self.products:
                category_name = self.categories.get(product.get('Category Code'), 'Unknown Category')
                print(f"Code: {product['Product Code']}, Name: {product['Product Name']}, Unit: {product['Unit']}, Category: {category_name}")

# პროდუქციის ცნობარების შექმნა, პროდუქტის ბაზაში შენახვის ფუნქციონალი.

    def save_products(self, filename='products.csv'):
        if not self.products:
            print("No products available to save.")
        else:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Product Code', 'Product Name', 'Unit', 'Category Code', 'Category Name'])
                writer.writeheader()
                writer.writerows(self.products)
                print(f"Products saved to {filename} successfully.")