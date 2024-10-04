
check_file_name = "check.txt"
product_list_name = "product_list.txt"

total = 0
money_from_roommate = 0

check = dict()
not_purchased = list()

check_file = open(check_file_name, 'r')

for line in check_file:

    line = line.strip("\n")

    item,price = line.split(',')

    if item in check.keys():
        check[item]=[ check[item][0] , check[item][1] + 1]
    else:
        check[item]=[ price , 1 ]

check_file.close()


for i in check.keys():
    print(f"item {i} price {check[i][0]} quantity {check[i][1]}")
    total = total + float(check[i][0]) * check[i][1]
print('-----------')
print(f"Total spent: {total:5.2f} euro")

file = open(product_list_name, 'r')

for line in file:
    line.strip("\n")
    item,quantity = line.split(',')
    quantity = int(quantity)

    if item in check.keys():

        if quantity <= check[item][1]:
            money_from_roommate = money_from_roommate + float(check[item][0]) * quantity
        else:
            money_from_roommate = money_from_roommate + float(check[item][0]) * check[item][1]
            T = (item , quantity - check[item][1])
            not_purchased.append(T)

    else:
        T = (item,quantity)
        not_purchased.append(T)

file.close()

print(f"Money from roommate: {money_from_roommate:5.2f} euro")
print("Item not purchased")
for i in not_purchased:
    print(i[1], i [0])
