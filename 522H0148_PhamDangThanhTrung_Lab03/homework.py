import cv2

# Capture video tu webcam
cap = cv2.VideoCapture(0)

# Doc anh logo TDT
logo = cv2.imread("lab3_img2.png", cv2.IMREAD_UNCHANGED)

# Lay kich thuoc cua logo
logo_height, logo_width = logo.shape[:2]

# Tao doi tuong VideoWriter de luu video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Capture tung khung hinh
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Lay kich thuoc cua khung hinh
    frame_height, frame_width = frame.shape[:2]
    
    # Dinh vi tri dat logo (goc duoi ben phai)
    x_offset = frame_width - logo_width
    y_offset = frame_height - logo_height
    
    # Chen logo len khung hinh
    for c in range(0, 3):
        frame[y_offset:y_offset+logo_height, x_offset:x_offset+logo_width, c] = \
            logo[:, :, c] * (logo[:, :, 3] / 255.0) + \
            frame[y_offset:y_offset+logo_height, x_offset:x_offset+logo_width, c] * (1.0 - logo[:, :, 3] / 255.0)
    
    # Ghi khung hinh co logo vao video output
    out.write(frame)
    
    # Hien thi khung hinh ket qua
    cv2.imshow('Homework Cam', frame)
    
    # Thoat vong lap khi nhan phim 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giai phong doi tuong capture va writer
cap.release()
out.release()
cv2.destroyAllWindows()