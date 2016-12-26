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
plisko = "95.46.44.18"
nodejs = "10.10.10.32"
port = 22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

choice = input("Server:")
if choice == "1":
    user = input("Enter username: ")
    passwd = getpass.getpass()
    adduser = input("Enter neme new user: ")
    domain = input("Enter domain name: ")
    # userpass = input("Enter username password: ")
    client.connect(hostname=plisko, username=user, password=passwd, port=port)
    client.exec_command('sudo -S useradd -m -d /home/' + adduser + ' ' + '-s /bin/bash -G sudo' + ' ' + adduser)
    client.exec_command('sudo -S mkdir /home/' + adduser)
    #stdin, stdout, stderr = client.exec_command('passwd' + ' ' + adduser)
    client.exec_command('mkdir /home/' + adduser + '/www')
    client.exec_command('mkdir /home/' + adduser + '/www/log')
    client.exec_command('mkdir /home/' + adduser + '/www/web')
    client.exec_command('chown -R' + ' ' + adduser + ':' + adduser + ' ' + '/home/' + adduser )
    client.exec_command('echo' + ' ' + "'<VirtualHost *:80> \n"
                                        "ServerName" + " " + domain + "\n"
                                        "DocumentRoot /home/" + adduser + "/www/web/ \n"
                                        "ErrorLog /home/" + adduser + "/www/log/dev_error.log \n"
                                        "<Directory /home/" + adduser + "/www/web/> \n"
                                        "Options Indexes FollowSymLinks \n"
                                        "AllowOverride All \n"
                                        "Order allow,deny \n"
                                        "Allow from all \n"
                                        "</Directory> '" + ' ' + '>' + ' ' + '/etc/apache2/sites-available/' + domain + '.conf')
    client.exec_command('a2ensite' + ' ' + domain + '.conf')
    client.exec_command('/etc/init.d/apache2 restart')
    #result = stdout.read().splitlines()

    #print(result)
    client.close()
elif choice == "2":
    user = input("Enter username: ")
    passwd = input("Enter password: ")
    adduser = input("Enter username: ")
    domain = input("Enter domain name: ")
    client.connect(hostname=plisko, username=user, password=passwd, port=port)

else:
    print("Incorrect choice")
