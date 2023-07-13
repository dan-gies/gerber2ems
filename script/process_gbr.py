
import subprocess

def gbr_to_png(input_name, output_name):
    return_code = subprocess.call(f"gerbv {input_name} gerber_import-Edge_Cuts.gbr --background=\#ffffff --foreground=\#000000ff --foreground=\#ff00000f -o not_cropped.png --dpi=2540 --export=png -a", shell=True)
    subprocess.call(f"convert not_cropped.png -trim {output_name}", shell=True)

import cv2
import numpy as np


def get_outline(input_name):

    image = cv2.imread(input_name)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    t = 230 # threshold: tune this number to your needs

    # Threshold
    ret, thresh = cv2.threshold(gray,t,255,cv2.THRESH_BINARY_INV)

    # Contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours