import cv2
import numpy as np

def load_cascades(face_cascade_path, eye_cascade_path):
    """Load Haar cascades for face and eye detection."""
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
    return face_cascade, eye_cascade

def preprocess_image(img):
    """Enhance the image for better detection."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)  # Enhance contrast
    return gray

def non_max_suppression(boxes, overlapThresh):
    """Apply Non-Maximum Suppression to filter out overlapping boxes."""
    if len(boxes) == 0:
        return []

    boxes = np.array(boxes)
    pick = []

    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 0] + boxes[:, 2]
    y2 = boxes[:, 1] + boxes[:, 3]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)    
    idxs = np.argsort(y2)

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        overlap = (w * h) / area[idxs[:last]]

        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))

    return boxes[pick].astype("int")

def detect_faces_and_eyes(img, face_cascade, eye_cascade):
    """Detect faces and eyes in the image and draw rectangles around them."""
    gray = preprocess_image(img)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=2, minSize=(30, 30))

    if len(faces) == 0:
        print("No faces detected")
        return img

    boxes = []
    for (x, y, w, h) in faces:
        boxes.append((x, y, w, h))

    # Apply Non-Maximum Suppression
    boxes = non_max_suppression(boxes, 0.3)

    for (x, y, w, h) in boxes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

    return img

def main(image_path, face_cascade_path, eye_cascade_path):
    """Main function to run the face and eye detection."""
    face_cascade, eye_cascade = load_cascades(face_cascade_path, eye_cascade_path)
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error loading image: {image_path}")
        return

    result_img = detect_faces_and_eyes(img, face_cascade, eye_cascade)

    cv2.imshow('Detected Faces and Eyes', result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main('test2.jpg', 'haarcascade_frontalface_default.xml', 'haarcascade_eye.xml')