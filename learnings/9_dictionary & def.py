import os 

all_servers = [{"name": "server-01", "ip": "192.168.1.10", "status": "active", "location": "paris"},
           {"name": "server-02", "ip": "192.168.1.11", "status": "inactive", "location": "london"},
           {"name": "server-03", "ip": "192.168.1.12", "status": "active", "location": "new york"}]

production_servers = [{"name": "server-01", "ip": "192.168.1.10", "status": "active", "location": "paris"},
                      {"name": "server-03", "ip": "192.168.1.12", "status": "active", "location": "new york"}]


#Define
def get_active_servers_ips(servers):
    active_ips = []
    for server in servers:
        if server["status"] == "active":
            active_ips.append(server["ip"])
    return active_ips

active_ips = get_active_servers_ips(all_servers)
print(active_ips)

#Ouvir/créer un fichier et écrire dedans :
with open("active_ips.txt", "w") as my_variable:
    for ip in active_ips:
        my_variable.write(ip + "\n")

#Ouvrir un fichier, lire et récipérer ses infomations :
with open("active_ips.txt", "r") as my_variable:
    active_ips = my_variable.read()
    ips_from_file = active_ips.split("\n")

directory_contents = os.listdir() # Equivalent d'une commande ls qui retourne une liste string
for content in directory_contents : # Boucle de vérif pour savoir si c'est un fichier ou un dossier
    if os.path.isfile(content):
        print(f"{content} is a file")
    elif os.path.isdir(content):
        print(f"{content} is a dir")
    else:
        print(f"{content} is somthing elese")

directory_contents = os.listdir()
for content in directory_contents : # Boucle de vérif pour print uniquement les fichiers pythons
    if os.path.isfile(content) and content.endswith(".py"):
        print(f"{content} \n")

