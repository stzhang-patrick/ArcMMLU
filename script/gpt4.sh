#!/bin/bash

cd ../src

python gpt4.py \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/GPT4 \
    --num_few_shot 0


python gpt4.py \
    --data_dir ../arcmmlu_data \
    --save_dir ../results/GPT4 \
    --num_few_shot 5
