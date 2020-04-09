#!/bin/bash

conda activate YOLOv3
python calc_anchors.py --path data/kitti_training_files_train.txt --num_clusters 9
