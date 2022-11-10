import exif
import cv2
import numpy as np

img = exif.Image('original.JPG')

print(img.has_exif)

emoji = cv2.imread('exif-data-image-thumbnail-not-updating.png')
img_encode = cv2.imencode('.png', emoji)[1]
  
# Converting the image into numpy array
data_encode = np.array(img_encode)
  
# Converting the array to bytes.
byte_encode = data_encode.tobytes()

print(dir(img))

img.update_thumbnail(byte_encode)

thumb_updated = img.get_thumbnail()

decoded = cv2.imdecode(np.frombuffer(thumb_updated, np.uint8), -1)
cv2.imshow('New Thumbnail', decoded)

cv2.waitKey(0)

with open('original.JPG', 'wb') as file:
    file.write(img.get_file())