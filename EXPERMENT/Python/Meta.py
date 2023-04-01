import subprocess

def run_metasploit_command(command):
    process = subprocess.Popen(["msfconsole", "-x", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, error) = process.communicate()
    return output.decode()

command = input("Enter the Metasploit Framework command: ")
print(run_metasploit_command(command))
