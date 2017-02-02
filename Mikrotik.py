import paramiko
import getpass

print("""Select action:
1: Add new domain name
2: Delete domain name""")

user = "admin"
mikrotik = "nas2.oknet.pp.ua"
port = 22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
choice = input("Your choice: ")

if choice is "1":
    passwd = getpass.getpass()
    domain = input("Enter domain name: ")
    ip_address = input("Enter ip address: ")
    client.connect(hostname=mikrotik, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command(
        '/ip dns static add name=' + domain + ' address=' + ip_address + ' comment=' + domain)
    stdin, stdout, stderr = client.exec_command(
        '/ip proxy access add dst-port=80 dst-host=' + domain + ' action=allow disabled=no comment=' + domain)
    stdin, stdout, stderr = client.exec_command('/ip proxy access remove [find comment=deny]')
    stdin, stdout, stderr = client.exec_command('/ip proxy access add action=deny disabled=no comment=deny ')
    result = stdout.read() + stderr.read()
    utf = result.decode('UTF-8')
    client.close()

elif choice is "2":
    passwd = getpass.getpass()
    domain = input("Enter domain name: ")
    client.connect(hostname=mikrotik, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command('/ip dns static remove [find comment=' + domain + ']')
    stdin, stdout, stderr = client.exec_command('/ip proxy access remove [find comment=' + domain + ']')
    client.close()
else:
    print("Incorrect choice")
