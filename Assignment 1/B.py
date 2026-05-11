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

with open("E:/University/Data Mining/Assignments/HW1/factors.csv", 'r', errors='ignore') as file:
    data = csv.reader(file)
    current_factor = 0
    current_purchase = []
    current_cart = set()
    departments = set()
    
    for line in data:
        factor_id = line[0]
        item = line[2]
        department_id = line[3]

        if factor_id != current_factor:
            if current_purchase:
                purchases.append(current_purchase)
                shopping_carts.append(list(current_cart))
                for dept in departments:
                    department_purchase[dept] += 1
            current_purchase = []
            current_cart = set()
            departments = set()
            current_factor = factor_id

        current_cart.add(department_id)
        current_purchase.append((item, department_id))
        goods.add(item)
        departments.add(department_id)
        single_purchase[item] += 1

    if current_purchase:
        purchases.append(current_purchase)

mylist = list()
for purchase in purchases:
    unique_items = sorted(set(purchase))
    for i in range(len(unique_items)):
        for j in range(i + 1, len(unique_items)):
            if unique_items[i][1] == unique_items[j][1]:
                mylist.append(unique_items[i][1])
                pair = (unique_items[i][0], unique_items[j][0])
                dict_goods[pair] += 1

workbook = Workbook()
file = workbook.active
file.title = "Item Rules (Same Dept)"
file.append(["item 1", "item 2", "Confidence", "Support", "department"])

total_transactions = len(purchases) - 1

i = 0
for (item1, item2), count in dict_goods.items():
    support = count / total_transactions
    confidence1 = count / single_purchase[item1]
    confidence2 = count / single_purchase[item2]

    if support >= min_support and confidence1 >= min_confidence:
        file.append([item1, item2, confidence1, support, mylist[i]])

    if support >= min_support and confidence2 >= min_confidence:
        file.append([item2, item1, confidence2, support, mylist[1]])

file.append([])

workbook.save("item_rules_same_department.xlsx")
