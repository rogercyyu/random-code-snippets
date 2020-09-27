import os
l = os.listdir(os.getcwd())

for n in l[::2]:
    os.unlink(n)
