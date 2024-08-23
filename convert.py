import cv2
video = cv2.VideoCapture('C:\\Users\\admin\\Desktop\\Live wallpaper\\LT1.mp4');
b,img = video.read();
c = 0;
while b:
    imgp = 'C:\\Users\\admin\\Desktop\\Live wallpaper\\imgLT1\\%s.jpg'%(c);
    cv2.imwrite(imgp,img);
    b,img = video.read();
    c+=1;