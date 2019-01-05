# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 20:19:35 2018

@author: soh.samy
"""

import cv2
import numpy as np
import store_csv

def detect_whiteness_background(input_image):


    original_img = cv2.imread(input_image,0)

    # try to detect the forground object and isolate the background
    object_edges = cv2.Canny(original_img,50,100)

    cv2.imshow('object_edges',object_edges)

    _, contours, _ = cv2.findContours(object_edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        biggest_contour = max(contours, key = cv2.contourArea)

    epsilon = 0.1*cv2.arcLength(biggest_contour,True)
    approx = cv2.approxPolyDP(biggest_contour,epsilon,True)
   
    cv2.drawContours(original_img, approx, -1, (0, 0, 0), 3)
    
    cv2.imshow("rec",original_img)

    # detect the range of the background color wconsidered as white
    original_img_mask1 = cv2.inRange(original_img, (252), (255))

    cv2.imshow("after mask",original_img_mask1)
    #cv2.imwrite(input_image+"after mask"+'.jpg' , original_img_mask1)


    _, color_contour,_ = cv2.findContours(original_img_mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(color_contour) != 0:
        biggest_contour1 = max(color_contour, key = cv2.contourArea)
    
    state =""
    
    if(cv2.contourArea(biggest_contour1)>1000):
        state =  "white"
        print ("the background is white")
        print (input_image)
    else:
        state = "not white"
        print("the background is not white")
        print (input_image)
    
    data={"name":input_image,"background state":state}
    
    # save the details about the images as report
    store_csv.store_csv(data)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    original_image = "7.jpg"

    detect_whiteness_background(original_image)

