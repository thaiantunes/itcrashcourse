# Basic Linux Commands 

## Managing files and directories

- grep: pesquisa linhas ou arquivos que contenham uma palavra chave

- $?: mostra o exit status do ultimo comando

- env: mostra as variáveis do sistema

- rm: remove arquivo

- cd directory: changes the current working directory to the specified one

- pwd: prints the current working directory

- ls: lists the contents of the current directory

- ls directory: lists the contents of the received directory  

- ls -l: lists the additional information for the contents of the directory  

- ls -a: lists all files, including those hidden  

- ls -la: applies both the -l and the -a flags  

- mkdir directory: creates the directory with the received name

- rmdir directory: deletes the directory with the received name (if empty)

- cp old_name new_name: copies old_name into new_name

- mv old_name new_name: moves old_name into new_name

- touch file_name: creates an empty file or updates the modified time if it exists

- chmod modifiers files: changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable

- chown user files: changes the owner of the files to the given user

- chgrp group files: changes the group of the files to the given group

## Operating with the content of files

- cat file: shows the content of the file through standard output

- wc file: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin

- file file: prints the type of the given file, as recognized by the operating system

- head file: shows the first 10 lines of the given file

- tail file: shows the last 10 lines of the given file

- less file: scrolls through the contents of the given file (press "q" to quit)

- sort file: sorts the lines of the file alphabetically

- cut -dseparator -ffields file: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

## Additional commands

- echo "message": prints the message to standard output

- date: prints the current date

- who: prints the list of users currently logged into the computer

- man command: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)

- uptime: shows how long the computer has been running

- free: shows the amount of unused memory on the current system  

## Operating with processes

- ps: lists the processes executing in the current terminal for the current user

- ps ax: lists all processes currently executing for all users  

- ps e: shows the environment for the processes listed  

- kill PID: sends the SIGTERM signal to the process identified by PID

- fg: causes a job that was stopped or in the background to return to the foreground

- bg: causes a job that was stopped to go to the background

- jobs: lists the jobs currently running or stopped


- top: shows the processes currently using the most CPU time (press "q" to quit)  

## Redirecting Streams

``` python
#!/usr/bin/env python3

print("Dont mind me, just a bit of text here...")
```

``` bash
$ ./stdout_example.py
Dont mind me, just a bit of text here... 
$ ./stdout_example.py > new_file.txt #will overwrite whatever is on that file or create a new one
$ cat new_file.txtx
Dont mind me, just a bit of text here... 
$ ./stdout_example.py >> new_file.txt #will append the first file to the second
```

### Redirecting STDIN
Consider the following python script:
``` python
#!/usr/bin/env python3

data = input("This will come from STDIN:)
print("Now we write it to STDOUT " + data)
raise ValueError("Now we generate an error to STDERR")
```

Now lets redirect the STDIN:

``` bash
$./streams_err.py < new_file.txt
This will come from STDIN: Now we write it to STDOUT: Dont mind me, just a bit of text here... 
Traceback (most recent call last):
    File "./streams_err.py", line 5, in <module>
        raise ValueError ("Now we generate an error to STDERR")
ValueError: Now we generate an error to STDERR
```

### Redirecting STDERR

``` bash
$./streams_err.py < new_file.txt 2> error_file.txt
This will come from STDIN: Now we write it to STDOUT: Dont mind me, just a bit of text here... 
$ cat error_file.txt
Traceback (most recent call last):
    File "./streams_err.py", line 5, in <module>
        raise ValueError ("Now we generate an error to STDERR")
ValueError: Now we generate an error to STDERR
```

### File descriptors

- 0> = STDIN
- 1> = STDOUT
- 2> = STDERR

## Pipes and Pipelines

Pipes make the stdout of a function the stdin of another one. See example below.

Consider the following song hehe:

```
The itsy bitsy spider climbing up the spout
Down came the rain and washed the spider out
Out came the sun and dried up all the rain
Now itsy bitsy spider went up the spout again
```

Now lets go to the terminal:
``` bash
$ cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort - nr | head
    7 the
    3 up
    3 spider
    3 and
    2 rain
    2 itsy
    2 climbed
    2 came
    2 bitsy
    1 waterspout.
```

Whats happening: tr translate the spaces to a like break, sort will sort the words (which are one per line) alphabecatly, uniq will remove the repeated words and index them by the amount each one of them appeared on the input, sort -nr will sort the lines reverse and numericaly, head will print the first 10 lines of stdout

This also works with scripts. Consider the following python script:

``` python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    print(line.strip().capitalize()) #will capitalize the first word of each row
```

On the terminal:

``` bash
$ cat haiku.txt
advance your carrer,
automating with Python,
its so fun to learn.
$ cat haiku.txt | /capitalize.py
Advance your career, 
Automating with python,
Its so fun to learn
```

The line above $ cat haiku.txt | /capitalize.py is the same as doing /capitalize.py < haiku.txt

Use pipe only when a lot of stuff will be done, like multiple pipes.

## Globs

Used to find a list of files 

``` bash
echo *.py #will list all the files in the cwd ending with .py
echo something.* #will list all the files in the cwd starting with something
echo ????.py #will list all files starting with 4 characters and ending with .py
```