#!/bin/bash

cd ../src

# v1
for i in {0..5}; do
python chatglm.py \
    --model_name_or_path /workspace/models/chatglm-6b \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/ChatGLM-6B \
    --num_few_shot $i 
done

# v2
for i in {0..5}; do
python chatglm.py \
    --model_name_or_path /workspace/models/chatglm2-6b \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/ChatGLM2-6B \
    --num_few_shot $i 
done
