#!/bin/bash

cd ../src

for i in {0..5}; do
python hf_causal_model.py \
    --model_name_or_path /workspace/models/Baichuan-7B \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/Baichuan-7B \
    --num_few_shot $i 
done
