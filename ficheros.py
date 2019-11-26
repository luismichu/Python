import os

print(os.getcwd())
os.chdir('C:/Dir')
print(os.listdir())
os.makedirs('carpeta')
os.rmdir('carpeta')
print(os.path.isfile('./'))
print(os.path.isdir('./'))

#with open('test.txt', 'w') as file:
#	file.write('Hello World')

fichero = open("test.txt", "w")
fichero.write('test')
fichero.close()