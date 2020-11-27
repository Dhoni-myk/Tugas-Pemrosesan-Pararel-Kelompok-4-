import psutil
print("CPU :",psutil.cpu_percent(),"%")

print("MEMORI :",psutil.virtual_memory().percent,"%")

sent=(psutil.net_io_counters().bytes_sent)
received=(psuti.net_io_counters().bytes_recv)
a=int(sent/10000)
b=int(received/10000)
print("TXRX :",a,"kbps/",b."kbps")
