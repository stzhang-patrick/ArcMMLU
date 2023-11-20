#!/bin/bash

cd ../src

for i in {0..5}; do
python internlm.py \
    --model_name_or_path /workspace/models/internlm-chat-20b \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/InternLM-20B \
    --num_few_shot $i 
done