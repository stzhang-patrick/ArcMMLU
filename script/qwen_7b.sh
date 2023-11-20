#!/bin/bash

cd ../src

for i in {0..5}; do
python qwen.py \
    --model_name_or_path /workspace/models/Qwen-7B \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/Qwen-7B \
    --num_few_shot $i 
done
