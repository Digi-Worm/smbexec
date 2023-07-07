import subprocess

def execute_command():
    try:
        service = input("Enter the service (smb/ftp/ssh): ")
        ip = input("Enter the IP address: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        command = input("Enter the command to execute: ")

        full_command = f"python samdump.py {service} {ip} -u {username} -p {password} -x \"{command}\""

        print("Executing command:", full_command)
        output = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        print("Command output:\n", output)

        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Command execution failed:", e.output)
    except Exception as e:
        print("Error executing command:", e)

if __name__ == "__main__":
    execute_command()
