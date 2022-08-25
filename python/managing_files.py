import os
import datetime

#os.remove("novel.txt") #delet file
#os.rename("spider_song.txt", "spider.txt") #rename file
os.path.exists("spider.txt") #retorna true se o arquivo existir
os.path.getsize("spider.txt") #retorna tamanho em bytes

#data de criação
print(os.path.getmtime("spider.txt")) #retorna quanto tempo depois do dia 1/1/1970 o arquivo foi criado, em segundos
timestamp = os.path.getmtime("spider.txt")
dte = str(datetime.datetime.fromtimestamp(timestamp))
print(dte[0:9])

#print(os.path.abspath("spider.txt")) #retorna o caminho absoluto do arquivo

#directories
# print(os.getcwd()) #retorna o cwd
# os.mkdir("new_dir") #cria novo diretorio (pasta) no diretorio atual
# os.chdir("new_dir") #muda para o diretorio passado como argumento
# print(os.getcwd())
# os.rmdir("new_dir") #deleta o diretorio passado como argumento, SÓ FUNCIONA SE ELE ESTIVER VAZIO!!!
#os.listdir("new_dir")
#os.chdir("..") #volta pro diretorio pai

#os.listdir("C:\Users\t.antunes\OneDrive - strohm\Py")

def parent_directory(): #retorna o ABSOLUTO do pai do diretorio atual
  # Create a relative path to the parent of the current working directory 
  relative_parent = os.path.join(os.getcwd(), '..')

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)


