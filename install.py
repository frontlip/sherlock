import os
while True:
    print("""
    Обновить - 0
    Установка - 1
    """)
    t=input("[???]=>")
    if t == '1':
        os.system("pip install request")
        os.system("pip install colorama")
        os.system("python3 sherl.py")
        save_file = open("sher.sh", "w+")
        save_file.write("python3 /sherlock/sherl.py")
        save_file.close()
        os.system("cat sher.sh > /data/data/com.termux/files/usr/bin/sher")
        os.system("chmod 700 /data/data/com.termux/files/usr/bin/sher")
        os.system("cd ..")
    elif t == 0:
        os.system("pkg install wget")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/sherl.py")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/index.php")
        pos.system("python3 sherl.py")
    else:
        print("0/1 ???")