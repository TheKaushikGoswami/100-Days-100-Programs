# importing cv2

import cv2

# importing watermark that we are going to use & python file and image in same folder

logo = cv2.imread("./Programs/Day 3 - Watermark Creator/assets/watermark.png")

# importing image on which we are going to apply watermark

img = cv2.imread("./Programs/Day 3 - Watermark Creator/assets/image.png")


# height and width of the watermark
h_logo, w_logo, _ = logo.shape

# height and width of the image
h_img, w_img, _ = img.shape

# calculating coordinates of center
# calculating center, where we are going to
# place our watermark
center_y = int(h_img/2)
center_x = int(w_img/2)

# calculating from top, bottom, right and left
top_y = center_y - int(h_logo/2)
left_x = center_x - int(w_logo/2)
bottom_y = top_y + h_logo
right_x = left_x + w_logo

# adding watermark to the image
destination = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(destination, 1, logo, 0.5, 0)

# displaying and saving image
img[top_y:bottom_y, left_x:right_x] = result
cv2.imwrite("./Programs/Day 3 - Watermark Creator/final_image.jpg", img)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()