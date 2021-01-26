# Detection Algorithm
 
The file contains code for detecting traffic signs.

The image color base is converted to HSV in order to form a mask with suitable red color range.
The original image is now compared with the mask in order to extract red regions on the image.
This extracted image is now used to find edges using CANNY EDGE Detection algoritm.
The image generated from CANNY EDGE is now used for contour approximation with area as metric to detect the traffic sign.
