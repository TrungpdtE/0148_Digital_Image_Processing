import numpy as np
from PIL import Image

def rgb_to_cmyk(image_path, output_path):

    img= Image.open(image_path)
    img= img.convert("RGB")
    data= np.array(img)

    #Chuyen doi RGB sang CMY
    c=1-data[...,0]/255.0
    m=1-data[...,1]/255.0
    y=1-data[...,2]/255.0

    #Tinh K
    k= np.minimum(c, np.minimum(m, y))

    #Tranh chia cho 0
    c= (c- k)/(1-k+ 1e-10)
    m= (m- k)/(1- k+ 1e-10)
    y= (y- k)/(1- k+ 1e-10)

    # Ket qua la mot mang CMYK
    cmyk=np.dstack((c, m, y, k)) * 255
    cmyk=cmyk.astype(np.uint8)

    # Tao anh CMYK va luu lai duoi dinh dang TIFF
    cmyk_img= Image.fromarray(cmyk, 'CMYK')
    cmyk_img.save(output_path, format='TIFF')

    return cmyk

cmyk_image= rgb_to_cmyk('rgb.png', 'rgb_cmyk.tiff')