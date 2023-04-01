from flask import Flask, render_template, url_for
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def Cust_Comm():
    return "ipconfig"

@app.route("/run_command_1")
def run_command_1():
    # Define the command you want to run
    command = Cust_Comm()

    # Capture the output of the command
    result = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True)

    # Return the output to the web page with a return button
    return f"{result.stdout}<br><br><a href='{url_for('index')}'>Return</a>"

@app.route("/run_command_2")
def run_command_2():
    # Define the command you want to run
    command = "Get-ComputerInfo"

    # Capture the output of the command
    result = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True)

    # Return the output to the web page with a return button
    return f"{result.stdout}<br><br><a href='{url_for('index')}'>Return</a>"

@app.route("/run_script")
def run_script():
    # Define the script you want to run
    script = "script.py"

    # Run the script
    subprocess.run(["python", script])

    return "Script executed!"

if __name__ == "__main__":
    app.run()
