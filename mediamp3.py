import os, random, subprocess
#import media

randomfile = random.choice(os.listdir("D:\\Music\\Collection\\"))
file = 'D:\\Music\\Collection\\' + randomfile
subprocess.call(['C:\\Program Files\\Windows Media Player\\wmplayer.exe', file])