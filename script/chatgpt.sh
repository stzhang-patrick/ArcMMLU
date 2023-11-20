#!/bin/bash

cd ../src

python chatgpt.py \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/ChatGPT \
    --num_few_shot 0

python chatgpt.py \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/ChatGPT \
    --num_few_shot 5
