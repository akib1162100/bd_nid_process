import cv2
image = cv2.imread("1.jpg")
# x,y= 190,220
# image = cv2.circle(image, (x,y), radius=5, color=(0, 0, 255), thickness=-1)
# x1,y1= 700,220
# image = cv2.circle(image, (x1,y1), radius=5, color=(0, 255,0), thickness=-1)
# x2,y2= 190,500
# image = cv2.circle(image, (x2,y2), radius=5, color=(0, 255,0), thickness=-1)

# x3,y3= 700,500
# image = cv2.circle(image, (x3,y3), radius=5, color=(0, 0, 255), thickness=-1)

# #x,y= 190,220
# x4,y4= 190,270
# image = cv2.circle(image, (x4,y4), radius=5, color=(0, 0, 255), thickness=-1)
# x5,y5= 700,270
# image = cv2.circle(image, (x5,y5), radius=5, color=(0, 255,0), thickness=-1)

# x6,y6= 190,330
# image = cv2.circle(image, (x6,y6), radius=5, color=(0, 0, 255), thickness=-1)
# x7,y7= 700,330
# image = cv2.circle(image, (x7,y7), radius=5, color=(0, 255,0), thickness=-1)

# x6,y6= 190,390
# image = cv2.circle(image, (x6,y6), radius=5, color=(0, 0, 255), thickness=-1)
# x7,y7= 700,390
# image = cv2.circle(image, (x7,y7), radius=5, color=(0, 255,0), thickness=-1)

# x6,y6= 190,440
# image = cv2.circle(image, (x6,y6), radius=5, color=(0, 0, 255), thickness=-1)
# x7,y7= 700,440
# image = cv2.circle(image, (x7,y7), radius=5, color=(0, 255,0), thickness=-1)

# x6,y6= 190,570
# image = cv2.circle(image, (x6,y6), radius=5, color=(0, 0, 255), thickness=-1)
# x7,y7= 700,570
# image = cv2.circle(image, (x7,y7), radius=5, color=(0, 255,0), thickness=-1)

# cv2.imshow("image", image)
# cv2.waitKey(0)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()

x_left = 190
y_up = 220
x_val= 510
y_vals= [50,60,60,50,60,70]

crp = []
for i in range(len(y_vals)):
    cropped = image[y_up:y_up+y_vals[i], x_left:x_left+x_val]
    crp.append(cropped)
    y_up += y_vals[i]

for i in range(len(crp)):
    cv2.imwrite("cropped_"+str(i)+".jpg", crp[i])
    cv2.imshow("cropped_"+str(i), crp[i])

cv2.waitKey(0)
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


# cv2.destroyAllWindows()