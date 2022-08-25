name = "abcde"
print(name)

#len counts characters of string
print(len(name))

#to index a string
#the first character is index as 0 ; the last character will be len(string)-1
#for the last character, do string[-1]
print(name[1])
print(name[-1])
print(name[len(name)-1]) #wont work for an empty string

#slice is the portion of a string that can contain more than one character; also sometimes called a substring
print(name[1:4])
print(name[:3])
print(name[3:])
print(name[2::2]) #começa no index 2 e vai até o final pulando a cada 2 tipo (2, 4, 6). o padrao é 1!

#modifing strings - strings in python are immutable
frase = "frase com wrro"
frase_corrigida = frase[:10] + "e" + frase[11:]
print(frase_corrigida)

#applying methods to strings 
pets = "cats & dogs"
print(pets.index("&"))
print(pets.index("c"))
print(pets.index("s")) #index method will return the first index found
print("dragons" in pets)
print("cats" in pets)
print("cat" in pets)

#inverter uma string
stringtorta = "araniaht"
inverter = stringtorta[::-1]
print(inverter)

#example
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@")
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_domain("thainara@gmail.com", "gmail.com", "hotmail.com"))

print("Thainara".upper()) #retorna tudo em maiuscula
print("Thainara".lower()) #retorna tudo em minuscula


#other string methods
name1 = "  yes  "
name1.strip() #remove spaces on the begining/end of a string
name1.lstrip() #remove spaces on the left side of a string
name1.rstrip() #remove spaces on the right side of a string
name1.count("s") #counts how many times a substring appears within the string
name1.endswith("es") #returns True if the string ends with the parameter
name1.isnumeric() #return True if the string is made of just numbers
print(" ".join(["This", "is", "a", "string", "joined", "by", "spaces"])) #will join the substrings with the initial string in between them
print("...".join(["This", "is", "a", "string", "joined", "by", "..."]))
print("This is another example".split()) #by default will split the string by the spaces
print("This.is.another.example".split("."))

#removing spaces between words in a string -- replace method
stringWithoutSpaces = "Lets remove those spaces".replace(" ", "")
print(stringWithoutSpaces)

#formating strings
name2 = "Manny"
number2 = len(name) * 3
number3 = 7.123
print("Hello {}, your lucky number is {}".format(name2, number2))
print("Your lucky number is {number}, {name}".format(name=name2, number=number2*2))
print("{:.2f}".format(number3)) #formats the amount of decimals

#example
def to_celsius(x):
    return (x-32)*5/9

for x in range (0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x))) # o {:>3} faz ficar espacado 3 caracteres para a direita, o {:>6.2f} faz ficar espacado 6 caracteres para a direita e terminar com 2 decimais

#removing all numeric characters in a string
strig = 'h3llo lets try this 324 very n1ce 43 progr4m!11!'
strig = ''.join([i for i in strig if not i.isnumeric()]).replace('  ', ' ')
print(strig)

# String Operations Cheatsheet
# len(string) Returns the length of the string
# for character in string Iterates over each character in the string
# if substring in string Checks whether the substring is part of the string
# string[i] Accesses the character at index i of the string, starting at zero
# string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

# String methods Cheatsheet
# string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
# string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
# string.count(substring) Returns the number of times substring is present in the string
# string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
# string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
# string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
# string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
# delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
# string.rfind - igual a index, mas com a ultima ocorrencia da substring