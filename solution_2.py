name_file_product = "product_list.txt"
name_file_check = "check.txt"

roommate_list_items = dict()

total = 0.00
total_rimmate = 0.00

#read product_list.txt and create a dictionary

file_lista = open(name_file_product,'r')

for line in file_lista :
    item = line.split(",")
    roommate_list_items[item[0]]=int(item[1])

file_lista.close()

#I scroll through the check and look for the data in the roommate_list_items
#what is mine -> I do not consider, 
#what is not mine -> I process it by: removing it from the dictionary or by scaling the quantity to be purchased

file_lista = open(name_file_check,'r')

for line in file_lista :
    item = line.split(",")
    total = total + float(item[1])

    if item[0] in roommate_list_items.keys() :
        total_rimmate = total_rimmate + float(item[1])
        if roommate_list_items[item[0]] == 1 :
            roommate_list_items.pop(item[0])
        else:
            roommate_list_items[item[0]] = roommate_list_items[item[0]] - 1

file_lista.close()

#print the totals

print(f"Total spent: {total:6.2f} euro")
print(f"Money from roommate: {total_rimmate:6.2f} euro")

#unpurchased products remain in roommate_list_items

print("Item not purchased:")
for i in roommate_list_items:
    print(f"{roommate_list_items[i]:2} {i}")
