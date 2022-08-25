#!/usr/bin/env python3
import shutil #devolve dados do hd
import psutil #devolve dados da cpu
import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    response = requests.get("http://www.google.com")
    return response.status_code == 200

def check_disk_usage(disk):
	du = shutil.disk_usage(disk) #quantidade de disco sendo usada
	free = du.free / du.total * 100 #porcentagem de disco livre
	return free > 20 

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
	print("ERROR!")

elif check_connectivity() and check_localhost():
	print("Everything is OK!")

else:
    print("Network error!")

#https://xkcd.com/1205/