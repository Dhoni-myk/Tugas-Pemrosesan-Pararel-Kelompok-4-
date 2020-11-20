def pc1():
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
    conn.send("python3 pc1.py\n")
    time.sleep(1)
    output =conn.recv(65535)
    print(output.decode("ascii"))
    print("      ")
    manggil()
def pc2():
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
    conn.send("python3 pc2.py\n")
    time.sleep(1)
    output =conn.recv(65535)
    print(output.decode("ascii"))
    print("      ")
    manggil()
def pc3():
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
    conn.send("python3 pc3.py\n")
    time.sleep(1)
    output =conn.recv(65535)
    print(output.decode("ascii"))
    print("      ")
    manggil()
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
    conn.send("scl enable rh-python36 bash\n")
    conn.send("python3 pc4.py\n")
    time.sleep(1)
    output =conn.recv(65535)
    print(output.decode("ascii"))
    print("      ")
    manggil()
def manggil():
    print("mau ngambil data yang mana?:")
    print("   pc1")
    print("   pc2")
    print("   pc3")
    print("   pc4")
    a=input("pilih :")
    if a=='pc1':
        pc1()
    elif a=='pc2':
        pc2()
    elif a=='pc3':
        pc3()
    else:
        pc4()
manggil()
