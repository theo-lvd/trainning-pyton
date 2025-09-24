import subprocess

#subprocess.run(["ls", "-la"])

#subprocess.run(["ls", "-la"], capture_output=True, text=True)

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)

if result.returncode == 0:
    print(result.stdout) #.stdout = l'output 
else:
    print(result.stderr) #.stderr = l'error (demande d'imprimer le message d'erreur pour pouvoir comprendre)

