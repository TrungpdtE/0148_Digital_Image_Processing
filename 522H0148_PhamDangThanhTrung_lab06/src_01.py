import cv2
import pandas as pd
from datetime import datetime 

# Assigning our static_back to None 
static_back = None
motion_list = [None, None] 
time = [] 
df = pd.DataFrame(columns=["Start", "End"]) 

# Capturing video from file
video = cv2.VideoCapture('1.avi') 

while True: 
    check, frame = video.read() 
    if not check: 
        break

    motion = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(gray, (21, 21), 0) 

    if static_back is None: 
        static_back = gray 
        continue

    diff_frame = cv2.absdiff(static_back, gray) 
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] 
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) 
    cnts, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    for contour in cnts: 
        if cv2.contourArea(contour) < 10000: 
            continue
        motion = 1
        (x, y, w, h) = cv2.boundingRect(contour) 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) 

    motion_list.append(motion) 
    motion_list = motion_list[-2:] 

    if motion_list[-1] == 1 and motion_list[-2] == 0: 
        time.append(datetime.now()) 
    if motion_list[-1] == 0 and motion_list[-2] == 1: 
        time.append(datetime.now()) 

    cv2.imshow("Gray Frame", gray) 
    cv2.imshow("Difference Frame", diff_frame) 
    cv2.imshow("Threshold Frame", thresh_frame) 
    cv2.imshow("Color Frame", frame) 

    key = cv2.waitKey(1) 
    if key == ord('q'): 
        if motion == 1: 
            time.append(datetime.now()) 
        break

# Appending time of motion in DataFrame 
for i in range(0, len(time), 2): 
    if i + 1 < len(time):  # Kiểm tra nếu chỉ số i + 1 hợp lệ
        df = pd.concat([df, pd.DataFrame({"Start": [time[i]], "End": [time[i + 1]]})], ignore_index=True)

# Save to CSV
if not df.empty:
    df.to_csv("Time_of_movements.csv", index=False) 
else:
    print("Không có dữ liệu để lưu.")

video.release() 
cv2.destroyAllWindows()
