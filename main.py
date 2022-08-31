import qrcode
from time import sleep
from random import randint
import os 

os.system("color 4")

Banner = """

     _____   _____   _____   _____   _____   _____   _____   _____   _____   _____   _____
    |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

 _ 	   ______     ______     __         ______     ______                ___   ____      
| |	  /\  ___\   /\  __ \   /\ \       /\  __ \   /\  == \     _____    / _ \ |  _ \	
| |	  \ \ \____  \ \ \/\ \  \ \ \____  \ \ \/\ \  \ \  __<    |_____|  | | | || |_) |	
| |	   \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\           | |_| ||  _ <    
| |	    \/_____/   \/_____/   \/_____/   \/_____/   \/_/ /_/            \__\_\|_| \_\   
|_|                                                                                     
     _____   _____   _____   _____   _____   _____   _____   _____   _____   _____   _____
    |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

CREATOR: Toyirov-Dev 


"""

print(Banner)
sleep(1.5)

data = input("QR text --> ")
sleep(1)
qr_color = input("QR-color --> ")
sleep(1)
bg_color = input("QR-background --> ")

qr = qrcode.QRCode(version = 3,
					box_size = 50,
					border = 1)
qr.add_data(data)
qr.make(fit = True)

rn = randint(100, 100000000000)
name = "qr" + str(rn) + ".png"

try:
	img = qr.make_image(fill_color = qr_color,
					back_color = bg_color)
	img.save("photos/" + name)
	print("\nQR GENERETED!")
except Exception as e:
	print("ERROR!")

input()