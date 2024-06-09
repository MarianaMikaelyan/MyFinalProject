import csv
# ხისტად არის პროდუქციის კატეგორიები გაწერილი
categories = [
    {'Category Code': 1, 'Category Name': 'High Quality Product'},
    {'Category Code': 2, 'Category Name': 'Medium Quality Product'},
    {'Category Code': 3, 'Category Name': 'Low Quality Product'}
]

csv_file = 'Product_Category.csv'
# პროდუქციის კატეგორიას ვინახავთ CSV ფაილის სახით. წარმოვიდგინოტ რომ ბაზაში გვაქვს კატეგორიების ცხრილი
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Category Code', 'Category Name'])
    writer.writeheader()
    for category in categories:
        writer.writerow(category)


