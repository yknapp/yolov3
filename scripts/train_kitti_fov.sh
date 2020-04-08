#!/bin/bash

conda activate YOLOv3
python3 train.py --cfg yolov3-spp_kitti.cfg --data data/kitti.data --weights ''
