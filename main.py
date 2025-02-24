# TASK: Create an interactive grocery list manager.

# Define a function to add an item to the list
def list_add(grocery_list : list, item: str):
# Append the item to the list and return it
    grocery_list.append(item)
    return grocery_list

# Define a function to remove an item from the list
def list_remove(grocery_list: list, item: str):
# If the item exists, remove it
    if item in grocery_list:
        grocery_list.remove(item)
        return grocery_list
# If not, display a message saying the item is not in the list
    else:
        print("the item you want to remove from the list is not part of the list ")
        return grocery_list
# Define a function to display the grocery list
def print_list(grocery_list):
    print(grocery_list)
# If the list is not empty, print all items with numbers
    if grocery_list:
        print("here's your list: ")
        index=0
        for item in grocery_list:
            index+=1
            print(f"{index} {item}") 
            # If the list is empty, display a message
    else:
        print("your list is empty ")

# Start with an empty grocery list
new_grocery=[]
# Use a loop to let the user choose an action:
while True:
    answer1=(input("would you like to edit this list? (y/n) "))
    if answer1=="n":
        print('goodbye! ')
        break
    else:
        answer2=int(input('enter 1(add), 2(remove), 3(view list), 4(exit) '))
        if answer2==1:# (1) Add an item
            item_add=str(input('what is the item you would like to add? '))
            new_grocery=list_add(new_grocery,item_add)
# (2) Remove an item
        elif answer2==2:
            item_remove=(str(input('what is the item you would like to remove? ')))
            new_grocery=list_remove(new_grocery,item_remove)

# (3) View the list
        elif answer2==3:
            new_grocery=print_list(new_grocery)
# (4) Exit the program
        elif answer2=="4":
            print('goodbye! ')
            continue
# Call the corresponding function based on user input
# Continue looping until the user chooses to exit
        else:
            break
