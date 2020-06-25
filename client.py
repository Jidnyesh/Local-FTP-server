from ftplib import FTP
import easygui
import os
from shutil import copyfile
base_direc = os.getcwd()
ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('/')



def uploadFile(filename1):
    
    filename = filename1 #replace with your file in your home folder
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
    print('File uploaded to Files folder')

def downloadFile(filename2):
    
    filename = filename2
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()

    localfile.close()
    print('Files are being downloaded to root folder')


xx = int(input('1.Upload\n2.Download\nInput your choice: '))
if xx==1:
    ftp.cwd('/')
    path = easygui.fileopenbox()
    temp = os.path.splitext(path)
    temp = temp[-1]
    print(path)
    print('Extension : '+temp)
    upload_nm = input('\nWith what name you wanna upload the file: ')
    upload_name = upload_nm+temp
    dst = base_direc+'\\'+upload_name
    print(dst)
    copyfile(path, dst)
    ftp.cwd('/Files/')
    uploadFile(upload_name)
    os.remove(dst)

elif xx==2:
    ftp.cwd('/Files/')
    ftp.retrlines('LIST')
    if not os.path.isdir(base_direc+'\\'+'downloads'):
        os.makedirs(base_direc+'\\'+'downloads')

    filename2 = input('\nEnter the file name to download: ')
    downloadFile(filename2)
    copyfile(base_direc+'/'+filename2, base_direc+'/downloads/'+filename2)
    os.remove(base_direc+'/'+filename2)
