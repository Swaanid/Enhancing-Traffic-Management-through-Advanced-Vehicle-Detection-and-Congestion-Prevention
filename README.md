
# Enhancing Traffic Management Through Advanced Vehicle Detection and Congestion Prevention 

## Introduction  
Urban areas face significant challenges due to traffic congestion, leading to wasted time, increased fuel consumption, and economic inefficiencies. Traditional traffic systems often fail to adapt to dynamic traffic conditions. This project leverages the **YOLOv8s** deep learning model to develop a real-time vehicle detection system, addressing these challenges by identifying various vehicle classes in urban traffic scenarios.  

---

## Data Collection and Annotation  
- **Dataset**: Comprising 920 annotated images extracted from traffic videos.  
- **Classes**: Cars, two-wheelers, autos, buses, and trucks.  
- **Annotation Tool**: Used LabelImg for bounding box labeling in YOLO format, ensuring high-quality data for training.  

---

## Model Building Using YOLOv8s  
- **Model Architecture**: YOLOv8s with 225 layers, 11.1M parameters, and a computational footprint of 28.7 GFLOPs.  
- **Training Setup**:  
  - **Epochs**: 30.  
  - **Image Size**: 640×640 pixels.  
  - **Batch Size**: 16.  
  - **Optimizer**: AdamW with momentum and weight decay parameters.  
  - **Data Augmentation**: Applied random augmentations for robustness.  
- **Objective**: Enable precise and efficient vehicle detection in real-time.  

---

## Real-Time Video Prediction  
- **Implementation**: Integrated YOLOv8s with OpenCV for processing video streams.  
- **Output**: Annotated video frames with bounding boxes and labels for detected vehicles.  
- **Potential Applications**:  
  - Traffic monitoring.  
  - Adaptive traffic signal control.  
  - Insights into traffic patterns and incidents.  

---

## Model Evaluation  
The model's performance was assessed using various metrics across different vehicle classes:  

| Class          | Precision (%) | Recall (%) | mAP@0.5 (%) |  
|----------------|---------------|------------|-------------|  
| **Car**        | 83.5          | 80         | 85.8        |  
| **Two-Wheeler**| 69            | 74.1       | 77.1        |  
| **Auto**       | 73.3          | 45.7       | 49.9        |  
| **Bus**        | 68.2          | 50.7       | 61.0        |  
| **Truck**      | 68.4          | 47.8       | 57.7        |  
| **All Classes**| 72.5          | 59.7       | 66.3        |  

- **Challenges**: The model performs well for cars and two-wheelers but faces difficulty with classes like autos, buses, and trucks due to dataset imbalance.  
- **Overall Metrics**:  
  - Precision: 72.5%.  
  - Recall: 59.7%.  
  - mAP@0.5: 66.3%.  

---

## Conclusion  
This project demonstrates the feasibility of using the YOLOv8s model for **real-time traffic vehicle detection**, excelling in identifying cars and two-wheelers.  
- **Future Directions**:  
  - Enhance the dataset for underperforming classes.  
  - Integrate with adaptive traffic control systems to dynamically optimize traffic flow.  
- **Impact**: Promising tool for intelligent transportation systems, paving the way for improved urban traffic management.  

