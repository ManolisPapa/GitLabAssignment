import subprocess
import os

root_dir = '.'  # Adjust if the username-id folders are elsewhere
output1 = 'output1.txt'
output2 = 'output2.txt'

with open(output1, 'r') as out1, open(output2, 'r') as out2:
    urls1 = list(out1.read().splitlines())
    urls2 = list(out2.read().splitlines())
    usernames = []
    for url in urls1:
        usernames.append(url.split('/')[-2])  # Extract username from URL
    for i in range(len(urls2)):
        if os.path.exists(usernames[i]):
            print(f"Directory {usernames[i]} already exists, skipping clone.")
        else:
            subprocess.run(['git', 'clone', urls2[i], usernames[i]], check=True)