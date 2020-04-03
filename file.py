helloFile = open('hello.txt')
content = helloFile.read()
print(content)
helloFile.close()
'''
helloFile = open('hello2.txt', 'w')
helloFile.write('Hello!!!!!')
helloFile.write('Hello!!!!!')
helloFile.write('Hello!!!!!')
helloFile.close()

helloFile = open('hello2.txt', 'a')
helloFile.write('Hello!!!!!')
helloFile.close()

import shutil

shutil.copy('hello2.txt', 'testfolder\\hello3.txt') # we are already working in current directory
shutil.copytree('testfolder', 'test2')
shutil.move('hello2.txt', 'testfolder\\hello3.txt')
shutil.rmtree('test4')

import os
cwd = os.getcwd()
print(cwd)

os.unlink('hello2.txt')
os.rmdir('test2')'''

import os
cwd = os.getcwd()
print(cwd)
