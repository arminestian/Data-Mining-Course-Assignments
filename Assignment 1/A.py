import csv
from collections import defaultdict
from openpyxl import Workbook

min_support = 0.003
min_confidence = 0.25

goods = set()
single_purchase = defaultdict(int)
dict_goods = defaultdict(int)
purchases = []
shopping_carts = []
department_purchase = defaultdict(int)
department_pairs = defaultdict(int)

with open("E:/University/Data Mining/Assignments/HW1/factors.csv", 'r', errors='ignore') as file:
    data = csv.reader(file)
    current_factor = None
    current_purchase = []
    current_cart = set()
    departments = set()

    for line in data:
        factor_id = line[0]
        item = line[2]
        department_id = line[4]

        if factor_id != current_factor:
            if current_purchase:
                purchases.append(current_purchase)
                shopping_carts.append(list(current_cart))
                for dept in departments:
                    department_purchase[dept] += 1
            current_cart = set()
            current_purchase = []
            departments = set()
            current_factor = factor_id

        current_cart.add(department_id)
        current_purchase.append(item)
        goods.add(item)
        departments.add(department_id)
        single_purchase[item] += 1

    if current_purchase:
        purchases.append(current_purchase)
        shopping_carts.append(list(current_cart))
        for dept in departments:
            department_purchase[dept] += 1

for purchase in purchases:
    unique_items = set(purchase)
    for item1 in unique_items:
        for item2 in unique_items:
            if item1 != item2:
                pair = tuple(sorted((item1, item2)))
                dict_goods[pair] += 1

for cart in shopping_carts:
    unique_departments = set(cart)
    for d1 in unique_departments:
        for d2 in unique_departments:
            if d1 != d2:
                pair = tuple(sorted((d1, d2)))
                department_pairs[pair] += 1

total_transactions = len(purchases)

workbook = Workbook()
item_sheet = workbook.active
item_sheet.title = "Item Rules"
dept_sheet = workbook.create_sheet("Department Rules")

item_sheet.append(["item 1", "item 2", "Confidence", "Support"])
dept_sheet.append(["department 1", "department 2" ,"Confidence", "Support"])

for (item1, item2), count in dict_goods.items():
    support = count / total_transactions
    confidence1 = count / single_purchase[item1]
    confidence2 = count / single_purchase[item2]

    if support >= min_support and confidence1 >= min_confidence:
        item_sheet.append([item1, item2, confidence1, support])

    if support >= min_support and confidence2 >= min_confidence:
        item_sheet.append([item2, item1, confidence2, support])

for (d1, d2), count in department_pairs.items():
    support = count / total_transactions
    confidence1 = count / department_purchase[d1]
    confidence2 = count / department_purchase[d2]

    if support >= min_support and confidence1 >= min_confidence:
        dept_sheet.append([d1, d2, confidence1, support])

    if support >= min_support and confidence2 >= min_confidence:
        dept_sheet.append([d2, d1, confidence2, support])

workbook.save("association_rules.xlsx")
