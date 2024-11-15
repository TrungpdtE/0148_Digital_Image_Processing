import cv2
import numpy as np
import time
from skimage.metrics import structural_similarity as ssim

#Tải tệp video hoặc từ camera
video_path = 'cat.mp4'
use_camera = False  #Đặt True nếu muốn dùng webcam
cap = cv2.VideoCapture(0 if use_camera else video_path)

#Kiểm tra xem video có mở thành công không
if not cap.isOpened():
    print("Lỗi: Không thể mở video.")
    exit()

#Lấy thuộc tính video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps

#Định nghĩa codec và tạo đối tượng VideoWriter
out = cv2.VideoWriter('CAT_OUT.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (frame_width, frame_height))

#Đọc khung hình đầu tiên
ret, prev_frame = cap.read()
if not ret:
    print("Lỗi: Không thể đọc khung hình.")
    exit()

#Chuyển khung hình sang thang độ xám
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

#Hàm hiển thị FPS
def display_fps(frame, fps):
    cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

#Hàm viết chữ lên video
def write_text(frame, text, position=(50, 50)):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#Hàm xử lý khung hình để ước lượng chuyển động
def process_frame(prev_gray, gray):
    frame_diff = cv2.absdiff(prev_gray, gray)
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    return thresh

#Hàm lưu khung hình với dấu thời gian
def save_frame_with_timestamp(frame, timestamp):
    filename = f'frame_{timestamp:.2f}.jpg'
    cv2.imwrite(filename, frame)

#Khởi tạo biến để tính toán FPS
prev_time = time.time()
frame_counter = 0

#Hàm phát video ngược
def play_video_reverse(frames):
    for frame in reversed(frames):
        cv2.imshow('Frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

#Thu thập khung hình để phát ngược
frames = []

#Thiết lập callback chuột cho các sự kiện
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Chuột được nhấn tại vị trí: ({x}, {y})")
cv2.namedWindow("Frame Difference")
cv2.setMouseCallback("Frame Difference", click_event)

#Khởi tạo tham số cho các tính năng khác
record_slow_motion = False  #Đặt True để quay chậm
denoise = False  #Đặt True để khử nhiễu
similarity_threshold = 0.9  #Ngưỡng tương đồng giữa các khung hình

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    #Thu thập khung hình để phát ngược
    frames.append(frame)

    #Chuyển khung hình hiện tại sang thang độ xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Xử lý khung hình để ước lượng chuyển động
    thresh = process_frame(prev_gray, gray)

    #Hiển thị FPS
    current_time = time.time()
    calculated_fps = 1 / (current_time - prev_time)
    prev_time = current_time
    display_fps(frame, calculated_fps)

    #Viết chữ lên video
    write_text(frame, 'Dang xu li video')

    #Lưu khung hình với dấu thời gian
    timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
    save_frame_with_timestamp(frame, timestamp)

    #Hiển thị khung hình kết quả
    cv2.imshow('Frame Difference', thresh)

    #Ghi khung hình vào video đầu ra
    out.write(cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR))

    #Phát chậm
    if record_slow_motion:
        cv2.waitKey(100)  #Điều chỉnh để tốc độ chậm hơn

    #Tính toán độ tương đồng giữa các khung hình
    if ssim(prev_gray, gray) < similarity_threshold:
        print("Phát hiện thay đổi đáng kể giữa các khung hình!")

    #Khử nhiễu nếu được bật
    if denoise:
        frame = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)

    #Cập nhật khung hình trước đó
    prev_gray = gray

    #Thoát vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

#Phát video ngược
play_video_reverse(frames)

#Giải phóng đối tượng capture và writer
cap.release()
out.release()

#Đóng tất cả cửa sổ OpenCV
cv2.destroyAllWindows()
