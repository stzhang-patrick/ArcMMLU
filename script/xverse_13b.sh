#!/bin/bash

cd ../src

for i in {0..5}; do
python xverse.py \
    --model_name_or_path /workspace/models/XVERSE-13B \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/XVERSE-13B \
    --num_few_shot $i
done


