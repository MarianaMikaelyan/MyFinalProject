from Product_Function import ProductManager
from Purchase_Function import PurchaseManager
from Sales_Function import SalesManager
from Analysis_Module import AnalysisManager

def final():
    category_file = 'Product_Category.csv'
    product_file = 'products.csv'
    purchase_file = 'purchases.csv'
    sales_file = 'sales.csv'
    
    product_manager = ProductManager(category_file, product_file)
    purchase_manager = PurchaseManager(purchase_file)
    sales_manager = SalesManager(sales_file)
    analysis_manager = AnalysisManager(product_manager, purchase_manager, sales_manager)

# ძირითადი მოდულების მენიუ არის შექმნილი.
 
    while True:
        try:
            print("\n--- Main Menu ---")
            print("1: Product Module")
            print("2: Purchase Module")
            print("3: Sales Module")
            print("4: Analytics Module")
            print("5: Exit")
            choice = input("Enter your choice: ").strip()

            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    # პროდუქტის მოდულში ცალკე მენიუ არის საჭირო რადგან მოდულში ბევრი სხვადასხვა ფუნქციონალია.
                    while True:
                        try:
                            print("\n--- Product Module ---")
                            print("1: Add Product")
                            print("2: Edit Product")
                            print("3: Delete Product")
                            print("4: View Products")
                            print("5: Back to Main Menu")
                            choice1 = input("Enter your choice: ").strip()

                            if choice1.isdigit():
                                choice1 = int(choice1)
                                if choice1 == 1:
                                    product_manager.add_product()
                                elif choice1 == 2:
                                    product_manager.edit_product()
                                elif choice1 == 3:
                                    product_manager.delete_product()
                                elif choice1 == 4:
                                    product_manager.view_products()
                                elif choice1 == 5:
                                    break  
                                else:
                                    print("Invalid choice. Please enter a number between 1 and 5.")
                            else:
                                print("Invalid input. Please enter a number.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")

                elif choice == 2:
                    # შეძენის მოდულში ცალკე მენიუ არის საჭირო რადგან მოდულში ბევრი სხვადასხვა ფუნქციონალია.
                    while True:
                        try:
                            print("\n--- Purchase Module ---")
                            print("1: Add Purchase")
                            print("2: View Purchases")
                            print("3: Back to Main Menu")
                            choice2 = input("Enter your choice: ").strip()

                            if choice2.isdigit():
                                choice2 = int(choice2)
                                if choice2 == 1:
                                    purchase_manager.add_purchase(product_manager.products)
                                elif choice2 == 2:
                                    purchase_manager.view_purchases()
                                elif choice2 == 3:
                                    break
                                else:
                                    print("Invalid choice. Please enter a number between 1 and 3.")
                            else:
                                print("Invalid input. Please enter a number.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")

                elif choice == 3:
                    # გაყიდვის მოდულში ცალკე მენიუ არის საჭირო რადგან მოდულში ბევრი სხვადასხვა ფუნქციონალია.
                    while True:
                        try:
                            print("\n--- Sales Module ---")
                            print("1: Add Sale")
                            print("2: View Sales")
                            print("3: Back to Main Menu")
                            choice3 = input("Enter your choice: ").strip()

                            if choice3.isdigit():
                                choice3 = int(choice3)
                                if choice3 == 1:
                                    sales_manager.add_sale(product_manager.products, purchase_manager.load_purchase_history())
                                elif choice3 == 2:
                                    sales_manager.view_sales()
                                elif choice3 == 3:
                                    break
                                else:
                                    print("Invalid choice. Please enter a number between 1 and 3.")
                            else:
                                print("Invalid input. Please enter a number.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")

                elif choice == 4:
                    # ანალიზის მოდულში ცალკე მენიუ აღარ გავაკეთე რადგან მინდოდა ერთ ფაილად ყოფილიყო ანალიტიკა
                    analysis_manager.display_analysis()

                elif choice == 5:
                    # ყველა აქ განხორციელებული ოპერაციების შენახვა ბაზებში როცა კოდის გაშვებას ვასრულებ.
                    product_manager.save_products()
                    purchase_manager.save_purchase_to_csv()
                    sales_manager.save_sale_to_csv()
                    analysis_manager.save_analysis()  # Save analysis data
                    print("Data saved successfully. Exiting the program.")
                    return

                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            else:
                print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    final()
