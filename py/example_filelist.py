import os

dir = "C:\\Users\\t.antunes\\OneDrive - strohm\\Py"

for name in os.listdir(dir):
    fullname = os.path.join(dir, name) #vai adicionar o path ao nome do arquivo de acordo com o sistema operacional
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

