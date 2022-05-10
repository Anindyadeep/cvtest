from enum import Flag
import os
from sre_parse import FLAGS 
import cv2 
import streamlit as st 

cam_source = 0
on = st.button('On')
off = st.button('Off')

cap = cv2.VideoCapture(cam_source)
app_window = st.image([])

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
FLAG = False

if on:   
    FLAG = True 
    size = (frame_width, frame_height)

    result = cv2.VideoWriter('pp.avi', 
                            cv2.VideoWriter_fourcc(*'MJPG'),
                            10, size)

    while on and not off:
        ret, frame = cap.read()
        result.write(frame)
        app_window.image(frame)
        cv2.waitKey(30)

        if off:
            break 
    cap.release()
    result.release()

if Flag and off:
    with open("pp.avi", "rb") as file:
        btn = st.download_button(
            'Download',
            data = file, 
            file_name= "pp.avi",
            mime="video/avi"
        )