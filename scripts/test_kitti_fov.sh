#!/bin/bash

conda activate YOLOv3
python3 test.py --cfg yolov3-spp_kitti.cfg --data data/kitti.data --nosave --weights weights/training_1/best.pt --img-size 608 --iou-thres 0.5
