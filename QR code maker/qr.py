import qrcode 


link = input("Enter your website link : https://")
border_size = int(input("Enter Border size: "))
box_size = int(input("Enter Box size: "))
mage_name = input ("Enter Image name : ")
color_qr = input ("Enter the Image Fill color (Recommended = black):")
back_color_qr = input ("Enter the Image back color(Recommended = white) :")


qrcode_det = qrcode.QRCode(version = 1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size= box_size,border = border_size)


qrcode_det.add_data("https://"+ link)
qrcode_det.make(fit = True)
img=qrcode_det.make_image(fill_color =color_qr,back_color = back_color_qr)
img.save(mage_name+".png")
