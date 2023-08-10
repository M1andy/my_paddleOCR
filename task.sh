#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

# python tools/train.py -c my_configs/ch_PP-OCRv3_rec_distillation.yml 
python3 tools/train.py -c my_configs/rec_r45_abinet_pretrain.yml
