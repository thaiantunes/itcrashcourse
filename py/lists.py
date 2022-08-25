x = ["Now", "we", "are", "cooking!"]
lst = ["oh nice", "really smart", "congrats"]
print(type(x))
print(len(x)) #show the amount of elements of a string
print(x[0]) #return the indexed element
x[2] = "arent" #replaces the element by another one
print(x)

x.append("food") #add item to end of the list
x.insert(0, "food") #add item to index parameter 
x.insert(435, "food") #if index out of range, item will be added to end of stirng
x.remove("arent") #remove item from list
x.pop(2) #remove indexed item from list
x.extend(lst) #adiciona os itens sem ser como lista (separadamente), enquanto o append vai adicionar como lista

#strings can only hold characters and are imutable
#lists can hold anything and are mutable
#tuples can hold anything and are imutable

###using enumerate function
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners, start=1):
    print("{} - {}".format(index, person))

###list comprehension
#creates lists while iterating stuff. can use conditionals.
#https://www.programiz.com/python-programming/list-comprehension
 
h_letters = [letter for letter in "human"]
print(h_letters)
number_list = [x for x in range(20) if x%2 == 0]
print(number_list)
num_list = [y for y in range (100) if y%2 == 0 if y%5 == 0] #y is appended to num_list if satisfies both conditions
print(num_list)