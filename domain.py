# -*- coding: utf-8 -*-
import paramiko
import getpass

print("""Select server:
1: Plisko
2: Nodejs""")

user = None
passwd = None
domain = None
adduser = None
userpass = None
plisko = "10.10.10.95"
nodejs = "10.10.10.32"
port = 22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

choice = input("Server: ")
if choice is "1":
    user = input("Enter username: ")
    passwd = getpass.getpass()
    client.connect(hostname=plisko, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command('docker ps -aqf "name=docker_web_1"')
    result = stdout.read() + stderr.read()
    utf = result.decode('UTF-8')
    #stdout, stderr = client.exec_command('docker exec -i -t ' + utf + ' bash')
    #stdin, stdout, stderr = client.exec_command('docker commit ' + utf + ' advocrowd/advocrowd-first:web-lates')
    #stdin, stdout, stderr = client.exec_command('docker tag ' + utf + ' advocrowd/advocrowd-first:web-lates')
    print(str(utf))


    client.close()
elif choice is "2":
    adduser = input("Enter username: ")
    domain = input("Enter domain name: ")
    client.connect(hostname=nodejs, username=input("Enter username: "), password=input("Enter password: "), port=port)

else:
    print("Incorrect choice")
