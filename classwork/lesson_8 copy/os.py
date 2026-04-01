
import os

print(os.getcwd())
os.chdir("./lesson_8")

os.mkdir("folder", mode=555)

print(os.getcwd())