
def pc():
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
    conn.send("scl enable rh-python36 bash\n")
    while True:
        print("Mau ngambil data dari yang mana?")
        print("   pc1")
        print("   pc2")
        print("   pc3")
        print("   pc4")
        a=input("pilih :")
        if a=='pc1':
            conn.send("python3 pc1.py\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
       
        elif a=='pc2':
            conn.send("python3 pc2.py\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
        
        elif a=='pc3':
            conn.send("python3 pc3.py\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
        
        else:
            conn.send("python3 pc4.py\n")
            output =conn.recv(65535)
            print(output.decode("ascii"))
            print("      ")
pc()
        
