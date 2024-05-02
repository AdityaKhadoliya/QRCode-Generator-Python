import qrcode
import image

qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the code image and complicated picture.
    box_size = 10, # size of the box where qr code will be displayed.
    border = 5 # it is the while part of image -- border in all 4 sides with the white color.
)

#Here, I have used the link of my Linkedin Page - we can use link or any text we want to let people see.
data = "https://www.linkedin.com/in/aditya-saini-940a5885/"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("LinkedIn_Page.png")
