shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
# None is roughly equivalent to null in C or Java
found_at = None

# for index in range(6):
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

    print("Item found at position {}".format(found_at))