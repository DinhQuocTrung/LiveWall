import ctypes
import os
import winreg as reg

cimg = len(os.listdir('C:\\Users\\admin\\Desktop\\Live_wallpaper\\imgLT1\\'));
c = 0;

while 1:
	if c >= cimg:
		c = 0;

	imgp = 'C:\\Users\\admin\\Desktop\\Live_wallpaper\\imgLT1\\%s.jpg'%(c);

	# key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Control Panel\Desktop", 0, reg.KEY_SET_VALUE)
	# reg.SetValueEx(key, "WallPaper", 0, reg.REG_SZ, imgp)
	a = open(imgp)

	a.close()
	ctypes.windll.user32.SystemParametersInfoA(20, 0, imgp, 0)
	# wp.set_wallpaper(imgp);
	# print(imgp)

	c += 1;
	