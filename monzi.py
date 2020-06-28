import subprocess
import os
import time

# command = 'python command_example.py'

os.chdir(os.path.expanduser('~/ParlAI'))
# command = ['python -m parlai.scripts.interactive_web', '-t blended_skill_talk', '-mf zoo:blender/blender_90M/model']
command = 'python -m parlai.scripts.interactive_web -t blended_skill_talk -mf zoo:blender/blender_90M/model --include-personas False'
proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# b = process.stdout.readline()#.decode("utf-8").strip()
# b = b.decode("utf-8")
# time.sleep(5)
# proc.stdout.flush()
# while True:
    # b = proc.stdout.readline()#.decode("utf-8").strip()
    # if 'chat starts' in b.decode("utf-8"):
        # break
# print(type(proc.stdout))
print("!!!!!!!!!!!! welcome to SimSimE world !!!!!!!!!!!!\n")
time.sleep(6)
print('Enter your ID: ', end='')
id = input()
while True:
    print('Enter Your Message: ', end='')
    # process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    a = f"{input()}\n".encode("utf-8")
    proc.stdin.write(a)
    proc.stdin.flush()
    start = time.time()

    while True:
        b = proc.stdout.readline()#.decode("utf-8").strip()
        b = b.decode("utf-8")
        if 'Enter Your Message' in b:
            break
    if 'TransformerGenerator' in b:
        b = b.replace('TransformerGenerator', 'SimSimE')
    b = b[20:-1]
    print(b + ' (response time: {:.2f}s)'.format(time.time() - start))

    if a == '[EXIT]':
        break
