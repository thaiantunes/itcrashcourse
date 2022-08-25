 # Git Crash Course

## Diffing Files

```bash
diff file1 file2
```
Comando para retornar o que tem diferente entre dois arquivos. É possivel usa-lo para diretórios também. 

A flag **diff -u** mostra as diferenças de forma mais fácil de entender. Tem um " - " no inicio das linhas removidas e um " + " no inicio das adicionadas. 

O **comando wdiff** mostra as palavaras que estão diferentes entre dois arquivos.

Exemplos de programas gráficos que mostram a diferença entre arquivos side by side: meld, KDiff3, vimdiff.

Para gerar um arquivo com as mudanças salvo, redireciono o resultado do diff:

``` bash
diff -u old_file new_file > change.diff
```

Esse arquivo .diff é chamado de **diff file ou patch file**.

Para aplicar as modificações de um arquivo .diff para o arquivo de código, o .py, uso o **comando patch**.

``` bash
patch código.py < changes.diff
```

## Git Sections

### Git directory 
History of all versions and modifications made to the files in the repository

### Working Tree 
Sandbox to edit the files that are currently being worked on. The state of fiiles here is labeled as **Modified**.

### Staging area 
A file mainted by Git that contains all of the information about what files and changes are going to go into your next commit. Same idea of an ECN. Will move files from the sandbox to the working tree. The state of fiiles here is labeled as **Staged**.

### Untracked Files
Files inside the repository that have never been commited have the status **Untracked**.


## Basic Git Commands

To set the user for all repositories:
``` bash
    git config --global
```
To create a new repository:
``` bash
    git init #inside the folder I want to turn into a repository
``` 
To add a file to staging area:
``` bash
    git add file.py
``` 

To see check Working Tree status:
``` bash
    git status
```

To commit the changes to be commited:
``` bash
    git commit #a text editor will open to to write the commit message
    git commit -m 'commit message' will commit directly
``` 







