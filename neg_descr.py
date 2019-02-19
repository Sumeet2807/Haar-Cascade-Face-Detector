import os
import sys


path = sys.argv[1]
file_out = sys.argv[2]

file = open(file_out, 'w')


for filename in os.listdir(path):

    content = path + "/" + filename + "\n"
    file.write(content)


file.close() 