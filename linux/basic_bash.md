# Basic Bash Scripting

- Bash shebang: #!/bin/bash
- STDOUT: echo 
- Writing echo alone prints a blank line 
- Defining a variable:
    ``` bash
    variable=value #it is not allowed to add space between the variable name, equal sign and value!
    ```
- Calling a variable: $variable
- Calling arguments: $1 $2 ...

``` bash
#!/bin/bash

echo "Hello World"
```

```bash 
#!/bin/bash

FILE=/home/thainara/Documents/
name=$FILE$1 #concatenates two strings, $1 is the first passed arguments

if [ -f $name ]; then # -f is only for files, -e also includes directories. [ ] is the test, returns 0 if true
    echo "$1 exists"
else
    echo "ERROR! $1 doesnt exists!"
fi
```

## Comparison Operators

https://tldp.org/LDP/abs/html/comparison-ops.html

### Integers Comparison

- -eq = is equal to
- -ne = is not equal to
- -gt = is greater than
- -ge = is greater than or equal to
- -lt = is less than
- -le = is less than or equal to
- < = is less than (within double parentheses)
- <= = is less than or equal to (within double parentheses)
- > = is greater than (within double parentheses)
- >= = is greater than or equal to (within double parentheses)

## while loops 

``` bash
#!/bin/bash

n=1
while [ $n -le 5 ]; do
        echo "Iteration number $n"
        ((n+=1))
done
```

## for loops 

``` bash
#!/bin/bash

for file in *.HTM; do #will list all files ending with .HTM in the cwd
    name=$(basename "$file" .HTM) #will get the basename of file, removing the indicated extension
    mv "$file" "$name.html"
done
```

