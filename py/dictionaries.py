#dictionary = {"key1":value1, "key2":value2, "key3":value3}
#dictionaries are mutable
#https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
dic = {"key1":4, "key2":67, "key3":25, "key4":56}
print(dic)
print(dic["key1"])

dic["key1"] = 7 #will replace the value of the key
print(dic)
print(dic["key1"])

dic["key5"] = 5345 #will add another key/value pair to the dictionary
print(dic)

del dic["key3"] #will delet key3
print(dic) 

for key, value in dic.items(): #items method creats a tuple with first the key, second the value
    print("{} value is {}".format(key,value))

for value in dic.values(): #creates a list with only values
    print(value)

for key in dic.keys(): #creates a list with only keys
    print(key)

#example with a list as the value
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
	for color in value:
		print("{} {}".format(color, key))

'''Definition

x = {key1:value1, key2:value2} 

Operations

len(dictionary) - Returns the number of items in the dictionary

for key in dictionary - Iterates over each key in the dictionary

for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary

if key in dictionary - Checks whether the key is in the dictionary

dictionary[key] - Accesses the item with key key of the dictionary

dictionary[key] = value - Sets the value associated with key

del dictionary[key] - Removes the item with key key from the dictionary

Methods

dict.get(key, default) - Returns the element corresponding to key, or default if it's not present

dict.keys() - Returns a sequence containing the keys in the dictionary

dict.values() - Returns a sequence containing the values in the dictionary

dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.

dict.clear() - Removes all the items of the dictionary'''

