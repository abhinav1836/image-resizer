import cv2  #reuires pip install opencv-python
import os
os.system('cls')
img=cv2.imread("edited-pexels-olia-danilevich-8524994.jpg", cv2.IMREAD_UNCHANGED)  # FOR DOCUMENTATION: https://pythonexamples.org/python-opencv-cv2-resize-image/#:~:text=To%20resize%20an%20image%20in,not%2C%20based%20on%20the%20requirement.

# cv2.imshow("title",img) #to show imagesres = 

# scale_percent=int(input("Enter percentage reduction: "))  #in percentage
# #calculate the 50 percent of original dimensions
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)

#CALCULATIONS IN PIXELS
width=int(input("pleaase enter width: "))
height=int(input("pleaase enter height: "))
dsize = (width, height)
# resize image

output = cv2.resize(img, dsize)

cv2.imshow("title",output)

print(img.shape)
print(output.shape)
cv2.waitKey(0)
# cv2.imwrite('O:/50.png',output) #to write new image om harddisk