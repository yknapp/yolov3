#!/bin/bash

conda activate YOLOv3
python3 detect.py --cfg yolov3-spp_kitti.cfg --weights weights/training_1/best.pt --img-size 608 --iou-thres 0.5 --source kitti/images/001456.png --output detection_output/
