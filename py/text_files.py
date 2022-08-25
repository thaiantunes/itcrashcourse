#reading files
file = open("spider.txt") #abre o arquivo 
print(str(file.tell()) + file.readline()) #readline - le uma linha da posição atual; tell - mostra a posição do cursor em bytes
print(file.read()) #read - le da posição atual do cursor até o fim

file.close() #fecha o arquivo

##with - open, use and shut without needing the open/close methods.
with open("spider.txt") as f:
    print(f.readline())

#iteraring through files
with open("spider.txt") as f:
    for line in f:
        print(line.upper()) #print will print not only the line_end from the text, but also from the actual print.


with open("spider.txt") as f:
    for line in f:
        print(line.upper(), end= '') #print end is \n by default, changing it to empty keeps it from adding blank lines

print('')
##atribuindo o conteudo de uma file a uma variable
f = open("spider.txt")
text = f.readlines() #cria uma lista com cada linha como uma entrada
f.close() #What is Python readline()? Python readline() method will return a line from the file when called. readlines() method will return all the lines in a file in the format of a list where each element is a line in the file.

text = [i.replace('\n','') for i in text]

print(text)

#writing files - https://docs.python.org/3/library/functions.html#open
with open("novel.txt", "w") as f:
    f.write("It was a dark and stormy night")

