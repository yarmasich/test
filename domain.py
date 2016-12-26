import paramiko

print("""Select server:
1: Plisko
2: Nodejs""")

user = "plisko"
passwd = "159753cfthn"
domain = None
adduser = None
userpass = None
plisko = "10.10.10.27"
nodejs = "10.10.10.32"
port = 22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

choice = input("Server:")
if choice == "1":
    adduser = input("Enter neme new user:> ")
    #userpass = input("Enter username password: ")
    client.connect(hostname=plisko, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command('sudo -S useradd -m -d /home/' + adduser + ' ' + '-s /bin/bash -G sudo' + ' ' + adduser)
    stdin, stdout, stderr = client.exec_command('sudo -S mkdir /home/' + adduser)
    stdin, stdout, stderr = client.exec_command('sudo -S mkdir /home/' + adduser + '/www')
    stdin, stdout, stderr = client.exec_command('sudo -S mkdir /home/' + adduser + '/www/log')
    stdin, stdout, stderr = client.exec_command('sudo -S mkdir /home/' + adduser + '/www/web')
    #stdin, stdout, stderr = client.exec_command('sudo -S passwd' + ' ' + adduser)
    stdin.write(passwd + '\n')
    stdin.flush()
    result = stdout.read().splitlines()

    print(result)
    client.close()
elif choice == "2":
    adduser = input("Enter username: ")
    domain = input("Enter domain name: ")
    client.connect(hostname=nodejs, username=input("Enter username: "), password=input("Enter password: "), port=port)

else:
    print("Incorrect choice")
