import os
import random
path="C:\\Users\\Admin\\Desktop\\docs\\archive"
files = os.listdir(path)
a = random.choice(files)
os.startfile(a)
