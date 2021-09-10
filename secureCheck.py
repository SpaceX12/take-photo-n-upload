import dropbox
import cv2
import time
import random

s_time = time.time()

def takeSnapshot():
    number = random.randint(0,200)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = 'img'+str(number)+'.png'

        cv2.imwrite(img_name, frame)
        start_time =time.time()
        result = False

    return img_name
    print('ss taken')
    
    videoCaptureObject.release()
    cv2.destroyAllWindows() 

def upload(img_name):
    acToken = 'wuEivkyQg0MAAAAAAAAAAXjb4h0trKMNmrZY7yFChKSfsk-ULePKf6APIOF1md5l'
    fileFrom = img_name      
    fileTo = "/photo-folder/" + str(img_name)
    dbx=dropbox.Dropbox(acToken)

    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(), fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - s_time) >= 5):
            name = takeSnapshot()
            upload(name)

main()