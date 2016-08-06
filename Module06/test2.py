item = "puck, low"
add_item = "matt, fel"
items = item.split(",")
items_2 = add_item.split(",")

print(items[0].strip())
print(items[1].strip())

# add item to dictionary 
my_dict = {items[0].strip() : items[1].strip()}
# dynamically add item to dictonary. Add to for loop
my_dict[items_2[0].strip()] = items_2[1].strip()

print(my_dict)

# get the value where key = puck
print(my_dict.get(items[0].strip()))
print(my_dict.get(items_2[0].strip()))

'''
# in a for loop to get key and value
for key in dict:
print(key +" "+ dict[key]
'''
