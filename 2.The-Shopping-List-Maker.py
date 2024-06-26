#Task 1

shopping_list = []

print("What items should we add to the shopping list? \n Enter 'done' to stop adding items")

while True:
    new_item = input("Adding item: ")
    if new_item == 'done':
        break

    shopping_list.append(new_item)

#Task 2
print("Would you like to remove any items? If so type the item to remove it from the list. \n If not type 'no' to print our the list")

while True:
    removed_item = input("Removing item: ")
    if removed_item == 'no':
        break
    else:
        shopping_list.remove(removed_item)

#Task 3

print("Shopping list: ")    
for item in shopping_list:
    print(item)