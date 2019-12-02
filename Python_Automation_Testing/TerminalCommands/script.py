import subprocess

print("for:")
for i in range(0, 5):
    subprocess.check_call(['python', 'example.py'])

print("while: ")
i = 0
while i < 5:
    subprocess.check_call(['python', 'example.py'])
    i += 1
