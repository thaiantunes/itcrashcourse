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

### Head 
HEAD is the latest commit in the project. It works as a bookmark of where you left of. Is also a pointer to the current branch. "The currently checked-out snapshot of your project."


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
    git commit -m 'commit message' #will commit directly
``` 

To print the changes made to the repository:
``` bash
    git log
```

To commit skipping the staging area (works only for tracked files):
```bash
git commit -a (-m) #shortcut to stage any changes to tracked files and commit them in one step #the -m flag is optional, to commit the commit message directly as well.
```

To print more information about a specific commit:
``` bash
    git show git_id
```

To print more information about all commits:
``` bash
    git log --stat
```

To print the diff between the current file on the repository and the one being commited:
``` bash
    git diff
    git add -p #will show the changes and confirm before commit
```

To remove a file from the repository and untrack it:
``` bash
    git rm
```

To rename or move a file on the repository:
``` bash
    git mv
```

To ignore files in 
``` bash
    git rm
```

## Commit Message

Should be a short descriprion of the change (up to 50 characters), followed by one or more paragraphs giving more details of the change (if needed).

## Commands to Undo Changes

To undo changes to modified, unstaged files: 
``` bash
    git checkout
```

To undo changes to modified, staged files: 
``` bash
    git reset HEAD
```

To overwrite the previous commit:
``` bash
    git add #do whatever was missing/wrong
    git commit -amend #not use on public repositories!!!
```

To rollback a commit:
``` bash
    git revert HEAD #revert the latest commit
    git revert commit_id #revert to the specified commit
```

## Working with Branches

To list all existing branches:
``` bash
    git branch
```

To create a new branch:
``` bash
    git branch new-branch 
```

To switch to a new branch:
``` bash
    git checkout new-branch
```

To create a new branch and switch to it:
``` bash
    git ch  eckout -b new-feature
```

To delete a branch:
``` bash
    git branch -d new-feature
```

### Merging
Term that Git uses for combining branched data and history together. Git uses two different algorithms to perform a merge: fast-forward and three-way merge.

To merge a branch to master:
``` bash
    git branch new-feature
```

The stop the merge:
To delete a branch:
``` bash
    git merge --abort
```
