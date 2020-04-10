#!/bin/bash

unit_model_folder="unit_fov_lyft2kitti"
unit_model_dir="/home/user/work/master_thesis/code/UNIT/outputs/$unit_model_folder"
output_file="$unit_model_dir/$unit_model_folder.txt"
fov_inputs="/home/user/work/master_thesis/datasets/lyft_kitti/object/training/fov"
transformation_outputs="/home/user/work/master_thesis/code/yolov3/lyft2kitti/images"
"" > $output_file
for checkpoint in $unit_model_dir/checkpoints/"gen_"*".pt"
do
  rm $transformation_outputs/*
  echo "CHECKPOINT: $checkpoint" >> $output_file  

  # UNIT   
  conda activate base
  python /home/user/work/master_thesis/code/UNIT/test_fov_converter.py --dataset="lyftkitti" --config $unit_model_dir/config.yaml --checkpoint $checkpoint --input $fov_inputs --output_folder $transformation_outputs --a2b 1

  # YOLO
  conda activate YOLOv3
  python3 test.py --cfg yolov3-spp_kitti.cfg --data data/lyft2kitti.data --weights weights/best.pt --img-size 608 --iou-thres 0.5 >> $output_file 
done
