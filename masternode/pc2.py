import paramiko
import time

user_name ="root"
passwd="dhonitt123"
ip="192.168.43.87"
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username=user_name,password=passwd, look_for_keys=False)
conn=ssh_client.get_transport().open_session()
conn.invoke_shell()
conn.send("scl enable rh-python36 bash\n")
conn.send("python3 tugas.py\n")
output =conn.recv(65535)
print(output.decode("ascii"))
print("      ")
