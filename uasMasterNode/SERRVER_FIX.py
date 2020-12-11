import paramiko
import time
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
ip=['192.168.43.7','192.168.43.87','192.168.43.98','192.168.43.90']
user_name ='root'
passwd='dhonitt123'
print("ambil data?:")
print("   node1 ")
print("   node2 ")
print("   node3 ")
print("   node4 ")
print("inputan dari 0")

a=list(map(int, input("Pilih node?").split(",")))
    
print("pilih rumus :")
print("1. Luas & Keliling Segitiga ")
print("2. Luas & Keliling Persegi")
print("3. Luas & Keliling Lingkaran")
        
x=input("pilih no brapa?")
if x=='1':
    a=str(input("masukkan nilai alas :"))
    t=str(input("masukkan nilai tinggi :"))
    b=str(input("masukkan nilai sisilain :"))
    c=str(input("masukkan nilai sisilainnya :"))
    for ipx in a:
        ssh_client.connect(hostname=ip[ipx],username=user_name,password=passwd, look_for_keys=False)
        conn=ssh_client.get_transport().open_session()
        conn.invoke_shell()
       
        conn.send("scl enable rh-python36 bash\n")
        conn.send("python3 wk1.py \n")
        conn.send(a+"\n")
        conn.send(t+"\n")
        conn.send(b+"\n")
        conn.send(c+"\n")
        output =conn.recv(65535)
        print(output.decode("ascii"))
        print("      ")
        
elif x=='2':
    s=str(input("masukkan nilai s :"))
    for ipx in a:
        ssh_client.connect(hostname=ip[ipx],username=user_name,password=passwd, look_for_keys=False)
        conn=ssh_client.get_transport().open_session()
        conn.invoke_shell()
        
        conn.send("scl enable rh-python36 bash\n")
        conn.send("python3 wk2.py \n")
        conn.send(s+"\n")
        output =conn.recv(65535)
        print(output.decode("ascii"))
        print("      ")
else:
    jari=str(input("masukkan nilai jari-jari :"))
    for ipx in a:
        ssh_client.connect(hostname=ip[ipx],username=user_name,password=passwd, look_for_keys=False)
        conn=ssh_client.get_transport().open_session()
        conn.invoke_shell()
        
        conn.send("scl enable rh-python36 bash\n")
        conn.send("python3 wk3.py \n")
        conn.send(jari+"\n")
        output =conn.recv(65535)
        print(output.decode("ascii"))
        print("      ")
print("berhasil mengambil nilai node")
