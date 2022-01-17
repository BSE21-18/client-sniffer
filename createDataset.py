import os
from machine import Pin, SoftSPI
from sdcard import SDCard

# Pin assignment:
# MISO -> GPIO 13
# MOSI -> GPIO 12
# SCK  -> GPIO 14
# CS   -> GPIO 27
spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))
sd = SDCard(spisd, Pin(27))


print('Root directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
#print('SD Card contains:{}'.format(os.listdir()))


# 1. To read file from the root directory:
# f = open('sample.txt', 'r')
# print(f.read())
# f.close()

# 2. To create a new file for writing:
f = open('test.csv', 'w')
f.write('"gas1":"345PH","gas2":"345PH","gas3":"345PH","gas4":"345PH","gas5":"345PH","gas6":"345PH"\n')
f.write('"345PH","345PH","345PH","345PH","345PH","345PH"')
f.close()

# 3. To append some text in existing file:
# f = open('sample3.txt', 'a')
# f.write('Some text for sample 3')
# f.close()

# 4. To delete a file:
#os.remove('test.csv')

# 5. To list all directories and files:
# os.listdir()

# 6. To create a new folder:
# os.mkdir('sample folder')

# 7. To change directory:
# os.chdir('directory you want to open')

# 8. To delete a folder:
# os.rmdir('folder to delete')

# 9.  To rename a file or a folder:
# os.rename('current name', 'd)