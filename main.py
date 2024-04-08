import cv2
import os
import numpy as np

column = 3
rows = 2
h_margin = 40
v_margin = 20


images = os.listdir("images")
image_obj = [cv2.imread(f"images/{filename}") for filename in images]

shape = cv2.imread("images/1.jpeg").shape
# print(shape)

big_img = np.zeros((shape[0] * rows + h_margin * (rows+1), shape[1] * column + v_margin * (column+1), shape[2]), np.uint8)

big_img.fill(255)

positions = [(x,y) for x in range(column) for y in range(rows)]
# print(positions)

for (pos_x, pos_y), image in zip(positions, image_obj):
  x = pos_x * (shape[1] + v_margin) + v_margin
  y = pos_y * (shape[0] + h_margin) + h_margin
  big_img[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite("grid.jpeg", big_img)