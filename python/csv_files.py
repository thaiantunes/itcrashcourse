import csv

## Reading csv
f = open("example.csv")
csv_f = csv.reader(f, delimiter=';') #default delimiter is comma

for row in csv_f:
    print(row)

## Writing csv
hosts = [["local_host", "127.0.0.1"], ["local_network","192.168.0.1"]]

with open("example_hosts.csv", "w", newline='') as f_hosts:
    writer = csv.writer(f_hosts)
    writer.writerows(hosts)

## Reading using Dictionaries
with open("example_dict.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

## Writing using Dictionaries
users = [{"name":"Sol Mansi", "username":"solm", "department":"IT infrastructure"}, {"name":"Lio Nelson", "username":"lion", "department":"User Experience Research"}, {"name":"Charlie Grey", "username":"greyc", "department":"Development"}]
keys = ["name", "username", "department"]

with open("example_users.csv", "w", newline='') as f_users:
    writer = csv.DictWriter(f_users, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
