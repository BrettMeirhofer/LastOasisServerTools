import subprocess


try:
    result = subprocess.run(["E:\SteamLibrary\steamapps\common\Last Oasis Testing SDK\RunDevKit.bat"], check=True, text=True, capture_output=True)
    print(f"STDOUT: {result.stdout}")
    print(f"STDERR: {result.stderr}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
