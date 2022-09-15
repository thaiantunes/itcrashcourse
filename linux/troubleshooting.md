# Week 1 - Troubleshooting Concepts

## What is debugging?

- **Troubleshooting** is the process of identifying, analyzing, and solving problems
- **Debugging** is the process of identifying, analyzing, and removing bugs in a system
- We sometimes use troubleshooting and debugging interchangeably. But generally, we say troubleshooting when we're fixing problems in the system running the application, and debugging when we're fixing the bugs in the actual code of the application. 
- **Debuggers** let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more. On top of that, if we can modify the code, we can change it so that it provides more logging information. This can help us understand what's going on behind the scenes.
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

Similar commands on other OSs:
- MasOS: dtruss
- Windows: Process Monitor

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

# Week 2 - Slowness

Always important to identify the bottleneck. Which may be the CPU time, disk IO, memory, network or others.

What to check in each OS to see what resources are being exhausted:
- Linux: Commands top (cpu and memory usage) and iotop (disk-io usage)
- MacOS: Activity Monitor (CPU, memory, energy, disk and network usage)
- Windows: Resource Monitor and Performance Monitor which also let us analyze what's going on with the different resources on the computer including CPU, memory, disk and network.

On linux:
- **Load average** shows how much time the processor is busy at a given minute with one meaning it was busy for the whole minute.
- **Process priorities** are typically numbers from 0 to 19. The lower the number, the higher the priority. By default, processes start with a priority of zero. This can be changed with following commands:
	- nice: to start a process with a different priority
	- renice: to change the priority of a program that's already running.
- Linux performance material: 
	- https://www.brendangregg.com/linuxperf.html
	- https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/ 

**Cache** é um conceito. Ter um cache é ter uma forma mais rapida de acessar algum dado. Cache stores data in a form that's faster to access than its original form.

## Possible Causes of Slowness

When trying to figure out what's making a computer slow, the first step is to look into when the computer is slow.

- On start up: Sign that there are too many applications configured to start on boot.
- After days of working fine and problem goes away with reboot: It means that there's a program that's keeping some state while running that's causing the computer to slow down. For example, this can happen if a program stores some data in memory and the data keeps growing over time, without deleting old values. If a program like this stays running for many days, the data might grow so much that reading it becomes slow and the computer runs out of RAM. This is almost certainly a bug in the program. And the ideal solution for a problem like this is to change the code so that it frees up some of the memory used. If you don't have access to the code, another option is to schedule a regular restart to mitigate both the slow program and your computer running out of RAM. 
- Other option may be that the files that the program is handling are too large. If it is a log file, consider using **logrotate**. This problem would continue even after reboot!
- Hardware fails can also cause computers to slow down. Check that often with OS utilities.
- Malicious Software are even another option;
- **Memory Leak**: When a program is not releasing RAM that is not longer needed.

## Slow Web Server

Tool to check the mean time to answer 500 requests:
``` bash
ab -n 500 site.example.com/ #ab stands for ApacheBench
```

## Slow Code
Always start by writing clear code that does what it should and only try to make it faster if we realize that it's not fast enough.

Common ways to make faster code:
- Storing data that was already calculated to avoid calculating it again
- Using the right data structures for the problem
- Reorganizing the code so that the computer can stay busy while waiting for information from slow sources like disk or over the network

### Profiler
Tool that measures the resources that our code is using, giving us a better understanding of what's going on. In particular, they help us see how the memory is allocated and how the time spent. 
They are specific to each programming language:
- C: gprof
- Python: c-Profile, pprofiler3
To read the contents of the profiler analysis: kcachegrind

### Data types

| **Py Data Type** |  **Java** |    **C++**    | **Ruby** | **Go** |
|:----------------:|:---------:|:-------------:|:--------:|:------:|
|       List       | ArrayList |     Vector    |   Array  |  Slice |
|    Dictionary    |  HashMap  | Unordered Map |   Hash   |   Map  |

Lists shall be used if you need to access elements by position or will always iterate through all the elements. This could be a list of all computers in the network, of all employees in the company, or of all products currently on sale for example. 

Dictionaries shall be used if we need to look up the elements using a key. This could be the data associated to a user which we'd look up using their username, the IP associated to a computer using the host name, or the data associated to a product using the internal product code. Whenever we need to do a bunch of these lookup operations, creating a dictionary and using it to get the data will take a lot less time than iterating over a list to find what we're looking for. 

But it doesn't make sense to create a dictionary and fill it with data if we're only going to look up one value in it. In that case, we're wasting time creating the structure when we could just iterate over the list and get the element we're looking for. 

Another thing that we might want to think twice about is **creating copies of the structures that we have in memory**. If these structures are big, it can be pretty expensive to create those copies. So we should double-check if the copy is really needed.

# Week 3 - Crashing Programs

## Wrappers
One of the common reasons why program crashes is that the input it receives is not what is expects. In many cases, we can not modify the code to solve the issue. To deal with that, **wrappers** are used. A Wrapper is a function or program that provides a compatibility layer between two functions or programs so they can work well together. 

## Watchdogs
Sometimes we can't find a way to stop an application from crashing but we can make sure that if it crashes it starts back again. To do this, we can deploy a **watchdog**. This is a process that checks whether a program is running and when it's not starts the program again. To implement this, we need to write a script that stays running in the background and periodically checks if the other program is running. Whenever the check fails the watchdog will trigger the program to restart. Doing this won't avoid the crash itself. But it will at least ensure that the service is available. 

## Invalid Memory
- Accessing invalid memory means that the process tried to access a portion of the system's memory that wasn't assigned to it. Now, how does this even happen? During normal working conditions, applications will request a portion of the memory and then use the space at the OS assigned to them. But programming errors might lead to a process trying to read or write to a memory address outside of the valid range. When this happens, the OS will raise an error like segmentation fault or general protection fault. What kind of programming error is this? It typically happens with low-level languages like C or C++ where the programmer needs to take care of requesting the memory that the program is going to use and then giving that memory back once it's not needed anymore. In these languages, the variables that store memory addresses are called **pointers**.
- The errors related to this are called **segmentation faults**. Examples:
	- Forgetting to initialize a variable
	- Trying to access a list element outside of the valid range
	- Trying to use a portion of memory after having given it back
	- Trying to write more data than the requested portion of memory can hold

## Core files 
Store all the information related to the crash so that we or someone else can debug what's going on. To generate them:
``` bash
$ ulimit -c unlimited
$ ./script.py
```

To debug a core file:
``` bash
$ gdb -c core script.py
```

The ***backtrace*** command can be used to show a summary of the function calls that were used to the point where the failure occurs.   

## Resources for Debugging Crashes

https://realpython.com/python-concurrency/

https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32

https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults

https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults

## Readable Python code on GitHub:

https://github.com/fogleman/Minecraft

https://github.com/cherrypy/cherrypy

https://github.com/pallets/flask

https://github.com/tornadoweb/tornado

https://github.com/gleitz/howdoi

https://github.com/bottlepy/bottle/blob/master/bottle.py

https://github.com/sqlalchemy/sqlalchemy
