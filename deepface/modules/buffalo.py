from typing import Any

import cv2
import numpy as np

import insightface
from insightface.app import FaceAnalysis

from deepface.commons import image_utils

def parsenp(obj):
  if isinstance(obj, np.ndarray):
    return obj.tolist()
  if isinstance(obj, np.float32):
    return float(obj)
  if isinstance(obj, np.int64):
    return int(obj)
  return obj

app = FaceAnalysis(name='buffalo_l', silent=True)
app.prepare(ctx_id=-1)

def represent(img_path: str) -> Any:
  img, img_name = image_utils.load_image(img_path)

  # img = cv2.imread(image_path)
  faces = app.get(img)

  resp_objs = []

  for face in faces:
    embedding = parsenp(face['embedding'])
    bbox = parsenp(face['bbox'])
    facial_area = {
      "x": bbox[0],
      "y": bbox[1],
      "w": bbox[2] - bbox[0],
      "h": bbox[3] - bbox[1],
      "age": parsenp(face['age']),
      "gender": parsenp(face['gender'])
    }
    face_confidence = parsenp(face['det_score'])
    data = {
      "facial_area": facial_area,
      "face_confidence": face_confidence,
      "embedding": embedding,
    }
    resp_objs.append(data)
    print(data['facial_area'])
  return resp_objs
