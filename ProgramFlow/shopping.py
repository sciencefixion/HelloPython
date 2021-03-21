shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# continue skips all the following code if the condition is true
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)


for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)