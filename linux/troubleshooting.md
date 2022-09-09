# Week 1 - Troubleshooting Concepts

## What is debugging?

- ***Troubleshooting*** is the process of identifying, analyzing, and solving problems
- ***Debugging*** is the process of identifying, analyzing, and removing bugs in a system
- We sometimes use troubleshooting and debugging interchangeably. But generally, we say troubleshooting when we're fixing problems in the system running the application, and debugging when we're fixing the bugs in the actual code of the application. 
- ***Debuggers*** let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more. On top of that, if we can modify the code, we can change it so that it provides more logging information. This can help us understand what's going on behind the scenes.
- Heisenbug: É um bug de software que parece desaparecer ou alterar seu comportamento quando se tenta estudá-lo

## Problem Solving Steps

1. Getting information
	- Reproduction case: Clear description of how and when the problem appears
	- Internal documentation, question asked on the internet
	- Questions to ask the user/start gathering information:
		- What were you trying to do?
		- What steps did you follow?
		- What was the expected result?
		- What was the actual result?

2. Root Cause
	- Get to the bottom of what's going on, what triggered the problem, and how we can change that
	- Finding the root cause is essential for performing the long-term remediation
	- The cycle for finding it: looking at the information we have, coming up with a hypothesis that could explain the problem, and then testing our hypothesis. If we confirm our theory, we found the root cause. If we don't, then we go back to the beginning and try different possibility.
	- Whenever possible, we should check our hypothesis in a test environment, instead of the production environment that our users are working with.

3. Performing the necessary remediation
	-  This might include an immediate remediation to get the system back to health, and then a medium or long-term remediation to avoid the problem in the future

- É importante ir fazendo um relatório com tudo que for sendo considerado root cause, os motivos de ser ou não ser cada opção. O que foi feito que deu certo, errado, etc.

## Debugging Commands

To print all script system calls (calls that the programs running on our computer make to the running kernel):
``` bash
strace <file.py> #will print all the system calls
strace -o failure.strace <file.py> #will save all system calls to the failure.strace file
``` 

To print all script library calls:
``` bash
ltrace <file.py> #will print all library calls
``` 

Others: top, iotop, iostat, vmstat, ionice, iftop, rsync (-bwlimit)

## System Logs
When the problem is connected to a specific user/machine, the first step is to read the logs available to you.
	- Linux: /var/log/syslog and user-specific logs like the xsession-errors file located in the user's home directory
	- MacOS: syslog + Library Logs Directory
	- Windows: Use Event Viewer tool 