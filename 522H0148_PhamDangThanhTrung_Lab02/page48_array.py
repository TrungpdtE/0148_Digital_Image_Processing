import numpy as np

rgb_array= np.array([
    [[255, 255, 255], [0, 0, 0], [200, 200, 50]],
    [[50, 200, 50], [50, 200, 200], [200, 50, 200]]
])

rgb_scale= 255
cmyk_scale= 100

def rgb_to_cmyk(r, g, b):
    if (r== 0) and (g== 0) and (b== 0):
        # den
        return 0, 0, 0, cmyk_scale

    # rgb [0,255] -> cmy [0,1]
    c= 1- r/ float(rgb_scale)
    m= 1- g/ float(rgb_scale)
    y= 1- b/ float(rgb_scale)

    # lay ra k [0,1]
    min_cmy= min(c, m, y)
    c= (c- min_cmy)
    m= (m- min_cmy)
    y= (y- min_cmy)
    k= min_cmy

    # chuyen ve khoang [0,cmyk_scale]
    return c* cmyk_scale, m* cmyk_scale, y* cmyk_scale, k* cmyk_scale

# Tao mang CMYK
cmyk_array= np.zeros((rgb_array.shape[0], rgb_array.shape[1], 4), dtype=np.float32)

# Chuyen doi tung pixel
for i in range(rgb_array.shape[0]):
    for j in range(rgb_array.shape[1]):
        r,g,b= rgb_array[i, j]
        c,m,y,k= rgb_to_cmyk(r, g, b)
        cmyk_array[i,j] = [c,m,y,k]

print("Mang CMYK:")
print(cmyk_array)