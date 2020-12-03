def pc1():
    
    import paramiko
    import time

    user_name ="root"
    passwd="dhonitt123"
    ip="192.168.43.7"
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=user_name,password=passwd, look_for_keys=False)
    conn=ssh_client.get_transport().open_session()
    conn.invoke_shell()
    while True:
        print("pilih cari yang mana :")
        print("1. Luas & Keliling Segitiga"
              "2. Luas & Keliling Persegi"
              "3. Luas & Keliling Lingkaran")
        x=input("pilih no brapa?")
        if x=='1':
            a=str(input("masukkan nilai alas :"))
            t=str(input("masukkan nilai tinggi :"))
            b=str(input("masukkan nilai sisilain :"))
            c=str(input("masukkan nilai sisilainnya :"))
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
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk2.py \n")
            conn.send(s+"\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
        else:
            jari=str(input("masukkan nilai jari-jari :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk3.py \n")
            conn.send(jari+"\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
            
            
                
    

def pc2():
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
   while True:
        print("pilih cari yang mana :")
        print("1. Luas & Keliling Segitiga"
              "2. Luas & Keliling Persegi"
              "3. Luas & Keliling Lingkaran")
        x=input("pilih no brapa?")
        if x=='1':
            a=str(input("masukkan nilai alas :"))
            t=str(input("masukkan nilai tinggi :"))
            b=str(input("masukkan nilai sisilain :"))
            c=str(input("masukkan nilai sisilainnya :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk1.py \n")
            conn.send(a+"\n")
            conn.send(t+"\n")
            conn.send(b+"\n")
            conn.send(c+"\n")
            time.sleep(1)
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")   
        elif x=='2':
            s=str(input("masukkan nilai s :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk2.py \n")
            conn.send(s+"\n")
            time.sleep(1)
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
        else:
            jari=str(input("masukkan nilai jari-jari :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk3.py \n")
            conn.send(jari+"\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
def pc3():
    import paramiko
    import time

    user_name ="root"
    passwd="dhonitt123"
    ip="192.168.43.98"
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=user_name,password=passwd, look_for_keys=False)
    conn=ssh_client.get_transport().open_session()
    conn.invoke_shell()
    while True:
        print("pilih cari yang mana :")
        print("1. Luas & Keliling Segitiga"
              "2. Luas & Keliling Persegi"
              "3. Luas & Keliling Lingkaran")
        x=input("pilih no brapa?")
        if x=='1':
            a=str(input("masukkan nilai alas :"))
            t=str(input("masukkan nilai tinggi :"))
            b=str(input("masukkan nilai sisilain :"))
            c=str(input("masukkan nilai sisilainnya :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk1.py \n")
            conn.send(a+"\n")
            conn.send(t+"\n")
            conn.send(b+"\n")
            conn.send(c+"\n")
            time.sleep(1)
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")   
        elif x=='2':
            s=str(input("masukkan nilai s :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk2.py \n")
            conn.send(s+"\n")
            time.sleep(1)
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
        else:
            jari=str(input("masukkan nilai jari-jari :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk3.py \n")
            conn.send(jari+"\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
def pc4():
    import paramiko
    import time

    user_name ="root"
    passwd="dhonitt123"
    ip="192.168.43.90"
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=user_name,password=passwd, look_for_keys=False)
    conn=ssh_client.get_transport().open_session()
    conn.invoke_shell()
    while True:
        print("pilih cari yang mana :")
        print("1. Luas & Keliling Segitiga"
              "2. Luas & Keliling Persegi"
              "3. Luas & Keliling Lingkaran")
        x=input("pilih no brapa?")
        if x=='1':
            a=str(input("masukkan nilai alas :"))
            t=str(input("masukkan nilai tinggi :"))
            b=str(input("masukkan nilai sisilain :"))
            c=str(input("masukkan nilai sisilainnya :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk1.py \n")
            conn.send(a+"\n")
            conn.send(t+"\n")
            conn.send(b+"\n")
            conn.send(c+"\n")
            time.sleep(1)
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")   
        elif x=='2':
            s=str(input("masukkan nilai s :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk2.py \n")
            conn.send(s+"\n")
            time.sleep(1)
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
        else:
            jari=str(input("masukkan nilai jari-jari :"))
            conn.send("scl enable rh-python36 bash\n")
            conn.send("python3 wk3.py \n")
            conn.send(jari+"\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
def manggil():
    print("mau ngambil data yang mana?:")
    print("   pc1")
    print("   pc2")
    print("   pc3")
    print("   pc4")
    a=a.split(",")
    if a=='pc1,pc2':
        pc1()
        pc2()
    elif a=='pc2':
        pc2()
    elif a=='pc3':
        pc3()
    else:
        pc4()
manggil()
