
import cv2
import numpy as np

laser_y = 250  # virtual laser line

def detect_intrusion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)

    cv2.line(frame, (0, laser_y), (frame.shape[1], laser_y), (0, 0, 255), 2)

    intrusion_area = thresh[laser_y-5:laser_y+5, :]
    if np.mean(intrusion_area) > 20:
        cv2.putText(frame, "INTRUSION DETECTED!",
                    (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)

    return frame
