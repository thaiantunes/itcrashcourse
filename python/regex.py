# Regex

import re
'''https://regex101.com/'''
'''https://regexcrossword.com/'''

## Basic matching with grep
'''grep ~palavra a procurar~ path (grep é case sensitive)
grep -i python path (o -i tira a case sensitiveness do grep)
. and ^ and $ -> wildcards
grep l.rts path (devolve tudo tipo larts, lerts, lirts etc)
grep ^fruit path (devolve tudo que começa com fruit)
grep cat$ path (devolve tudo que termina com fruit)'''

## Simple matching with Python

result = re.search(r"aza", "plaza")
print(result) #devolve a posição da matching string e qual ela era
print(result.span()) #devolve o span como tupla

print(re.search(r'aza', 'bazaar').span())

print(re.search(r'aza', 'maze')) #retorna None se não achar um match

print(re.search(r'p.ng', 'penguin')) #usando wildcard no match
print(re.search(r'p.ng', 'sponge'))

print(re.search(r'p.ng', 'Pangea')) #retorna None pq eh case senstive
print(re.search(r'p.ng', 'Pangea', re.IGNORECASE))

## Wildcards and Character Classes

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go")) #retorna None pq nao tem nada antes do way

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9")) #combinando varias coisas para procurar qualquer uma delas
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy")) 

print(re.search(r"[^a-zA-Z]", "This is not a letter, is a space")) #colocar ^ antes do span que coisas que pode, significa que elas nao podem. funciona como um not.
print(re.search(r"[^a-zA-Z ]", "This is not a letter, is a space")) #agora vai ser not space tb

print(re.search(r"cat|dog", "I like cats.")) #vai achar cat ou dog, o que vier primeiro
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like both cats and dogs."))

print(re.findall(r"cat|dog", "I like both cats and dogs")) #devolve uma lista com todas as aparicoes de cat e de dog

## Repetition Qualifiers .*+?^[]

print(re.search(r"Py.*n", "Pygmalion")) #retorna todos os caracteres que estiverem entre Py e n. Eh considerado um comportamento greedy.
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"a.*a", "text", re.IGNORECASE)) #retorna palavras que tem duas letras a
print(re.search(r"Py[a-z]*n", "Python Programming")) #assim nao contem o espaco

print(re.search(r"o+l", "goldfish")) 
print(re.search(r"o+l", "woolly"))

print(re.search(r"p?each", "I like peaches")) #a interrogacao significa q pode ter um ou zero da letra antes dele
print(re.search(r"p?each", "One each of them"))

print(re.search(r"[A-Za-z]{5}", "a ghost")) #procura intervalos que contenham 5 do que defini nos colchetes
print(re.findall(r"[A-Za-z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[A-Za-z]{5}\b", "a scary ghost appeared")) #vao ser so palavras inteiras
print(re.findall(r"\w{5,10}", "I really like strawberries")) #vai ser tudo entre 5 e 10 caracteres
print(re.findall(r"\w{5,}", "I really like strawberries")) #vai ser tudo acima de 5 caracteres
print(re.findall(r"s\w{,20}", "I really like strawberries")) #vai ser tudo abaixo de 20 caracteres que comeca com s

## Escaping Characters
'''What to do if I need to match one of the special characters?'''
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome")) #o backslash significa que isso o ponto nao eh mais um wildcard

## Capturing Groups

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result[0]) #devolve Lovelace, Ada
print(result[1]) #devolve Lovelace
print(result[2]) #devolve Ada
print("{} {}".format(result[2], result[1])) 

## Example

log = "July 21 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\b[A-Z]*\b)"
    result = re.search(regex, log_line)
    if result is None:
            return ""
    return "{} {}".format(result[1], result[2])

print(extract_pid(log))

## Splitting and Replacing
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!)")) #vai dividir a string com os marcadores que passei como argumento
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
print(re.sub(r"^(\w*), (\w*)$", r"\2 \1", "Lovelace, Ada"))

