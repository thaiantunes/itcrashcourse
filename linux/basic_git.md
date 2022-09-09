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

# GitHub

A remote repository for hosting service for Git 

Git is a distributed VCS, which means each developer has a copy of the whole repository on their local machine.

GitHub is good for personal and open source code. For real configuration and development work, you should use a secure and private Git server, and limit the people authorized to work on it.

## Basic Interaction with GitHub

To clone a repository to local machine:
``` bash
git clone github-repo-link
``` 

To commit from your local repo to a remote repo
``` bash
git push
```
To get the newest updates from a remote repository:
``` bash
git pull
```

To make github not ask for username/password everytime, I can use a SSH-key pair to make github recognize my computer OR use the credential helper. It will save my user/password for 15min and not ask for it in this time frame.
``` bash
git config --global credential.helper cache
```

### Basic Commands Review 
| Command | Explanation |
| :----: | :----: |
| git clone URL | Clones a remote repository into a local workspace |
| git push | Push commits from your local repo to a remote repo |
| git pull | Fetch the newest updates from a remote repository and merges it automatically |
| git push -u origin <branch name> | Pushes a new branch into github |


## Working with Remotes

To check the remote repos:
``` bash
git remote -v
git remote show origin
```

To get the newest updates from a remote repository, but not merge them, just really get them and see that they are there:
``` bash
git fetch
```

To check the remote log:
``` bash
git log origin/master #the (HEAD->master) lines are local commits and the (origin/master, origin/HEAD) are commits on the remote
```

If there are changes made to the remote repo that are not on the local repo, git status will show that. If the changes are not divergent, git status will state that they can be fast-forwarded. To merge the changes of the master branch on the remote repository to the local repository:

``` bash
git merge origin/master
```

### Remote Commands Review 
| Command | Explanation |
| :----: | :----: |
| git remote | Lists remote repos |
| git remote -v | List remote repos verbosely |
| git remote show <name> | Describes a single remote repo |
| git remote update | Fetches the most up-to-date objects |
| git fetch | Fetch the newest updates from a remote repository, but does not merge it  |
| git branch -r | Lists remote branches; can be combined with other branch arguments to manage remote branches |

## Managing Conflicts

The lines that have conflicts will be marked with a ">>>". Look for it when going through conflicts in a large file.

Keyword: Three-way Merge

## Colaborating

### Best Practices for Collaboration 
- It's a good idea to always synchronize your branches before starting any work on your own.
- Avoid having very large changes that modify a lot of different things.
- When working on a big change, it makes sense to have a separate feature branch.
- Regularly merge changes made on the master branch back onto the feature branch.
- If you need to maintain more than one version of a project at the same time, it's common practice to have the latest version of the project in the master branch and a stable version of the project on a separate branch. You'll merge your changes into the separate branch whenever you declare a stable release.
-  We can use rebase to make sure our history is linear. Rebasing can help a lot with identifying bugs, but use it with caution. Whenever we do a rebase, we're rewriting the history of our branch. The old commits get replaced with new commits, so they'll be based on different snapshots than the ones we had before and they'll have completely different hash sums. This works fine for local changes, but can cause a lot of trouble for changes that have been published and downloaded by other collaborators. So as a general rule, you shouldn't rebase changes that have been pushed to remote repos.
- Having good commit messages is important.
- Whenever we collaborate with others, there's bound to be some merge conflicts and they can sure be a pain.
Play video starting at :3:51 and follow transcript3:51
I've definitely been frustrated when encountering complex merge conflicts and trying to debug the results. If I'm dealing with this type of merge conflict, my first step is to work backward and disable everything I've done and then see if the source still works, then I slowly add pieces of code until I hit the problem. 

### Forking
Forking is a way of creating a copy of the given repository so that it belongs to our user. In other words, our user will be able to push changes to the forked copy, even when we can't push changes to the other repo. When collaborating on projects hosted on GitHub, the typical workflows, first, create a fork of the repo, and then work on that local fork. 

### Pull Request 
Pull request is a commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree.

### Interactive Rebase
You shouldn't rewrite history when the commits have been published. That's because someone else may have already synchronized that repo with those contents. This rule is waived with pull requests, since it's usually only you who have cloned your fork of the repository. For that, we can use ***interactive rebase***
```bash
git rebase -i master
```

On the commit message window, there are many commands options. A few include: squash and fixup.

## Code Review 

Means going through someone else's code, documentation or configuration and checking that it all makes sense and follows the expected patterns. 

### Goals
- Improve the project by making sure that changes are high quality
- Helps us make sure that the contents are easy to understand.
- Ensures that the style is consistent with the overall project.
- Ensures that we don't forget any important cases

### Code V Tools
Coder V tools let us comment on someone else's code. These let us leave feedback on how they could make their code better.

### Common Code Issues
- Unclear names that makes the code hard to understand
- Forgetting to add a test
- Forgetting to handle a specific condition
- If we're writing documentation, our reviewer can help us catch typos and things that aren't totally clear. 

### Nits
Comments are mostly a suggestion for making the code better. These comments are usually prefixed, saying that it's a Nit.

## CI/CD
A continuous integration system will build and test our code every time there's a change. This means that it will run whenever there's a new commit in the main branch of our code. It will also run for any changes that come in through pull request. In other words, if we have continuous integration configured for our project, we can automatically run our tests using the code in a pull request. This way, we can verify that the test will pass after the new changes get merged back into the tree and that means instead of hoping our collaborators will remember to properly test their code, we can rely on our automated testing system to do it for us.

Continuous deployment means the new code is deployed often. The goal is to avoid roll outs with a lot of changes between two versions of a project and instead do incremental updates with only a few changes at a time. This allows errors to be caught and fixed early. Typical configurations include deploying a new version whenever a commit is merged into the main tree or whenever a branch is tagged for release.

A common platform of CICD is Jenkins

Some repository hosting services like GitLab provide their own infrastructure for doing continuous integration. GitHub doesn't offer an integrated solution. Instead, the popular alternative is to use Travis which communicates with GitHub and can access the information from GitHub projects to know which integrations to run.

### CI/CD Concepts
- Pipelines: Specify the steps that need to run to get the result you want. For a simple Python Project, the pipeline could be to just run the automated tests. For a web service written in Go, the pipeline could be compiled the program, run the unit tests and integration tests and finally deploy the code to a test instance.
- Artifacts: Name used to describe any files that are generated as part of the pipeline. This typically includes the compiled versions of the code but can include other generated files like PDFs for the documentation or OS specific packages for easy installation.