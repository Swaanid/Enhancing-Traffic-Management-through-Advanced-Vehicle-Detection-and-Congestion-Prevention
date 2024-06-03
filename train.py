from ultralytics import YOLO
import torch
import os

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model 


# Use the model
results = model.train(data="config.yaml", epochs=50)  # train the model
  

 



