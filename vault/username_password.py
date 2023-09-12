import subprocess


def run_command(command):
    try:
        # Run the command and capture output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

        # Print the standard output
        print("Standard Output:")
        print(result.stdout)

        # Print the standard error
        print("Standard Error:")
        print(result.stderr)

        # Print the return code
        print("Return Code:", result.returncode)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    command_to_run = "ping 172.17.20.240"  # Replace with the command you want to run
    run_command(command_to_run)
