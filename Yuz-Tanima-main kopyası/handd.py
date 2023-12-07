import cv2
import mediapipe as mp

class Handetec:

  def __init__(self):
    self.top = []

  def all(self, frame):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    image = frame

    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = hands.process(image)
      fingerCount = 0

      if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

          handIndex = results.multi_hand_landmarks.index(hand_landmarks)
          handLabel = results.multi_handedness[handIndex].classification[0].label
          handLandmarks = []

          for landmarks in hand_landmarks.landmark:
            handLandmarks.append([landmarks.x, landmarks.y])

          if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
            fingerCount = fingerCount+1
          elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
            fingerCount = fingerCount+1

          if handLandmarks[8][1] < handLandmarks[6][1]:
            fingerCount = fingerCount+1
          if handLandmarks[12][1] < handLandmarks[10][1]:
            fingerCount = fingerCount+1
          if handLandmarks[16][1] < handLandmarks[14][1]:
            fingerCount = fingerCount+1
          if handLandmarks[20][1] < handLandmarks[18][1]:
            fingerCount = fingerCount+1

      return str(fingerCount)

