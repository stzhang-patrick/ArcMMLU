import os
import torch
import numpy as np
import argparse
from mp_utils import choices, format_example, gen_prompt, softmax, run_eval

from peft import PeftModel
from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

from mp_utils import extract_choice

def extract_answer(text):
    if len(text) == 1: 
        return text
    index = text.find("答案：")
    if index != -1:
        answer = text[index + len("答案："):]
        return extract_choice(answer)
    else:
        return text

def eval_chat(model, tokenizer, subject, dev_df, test_df, num_few_shot, max_length, cot, args):
    cors = []
    all_preds = []
    answers = choices[: test_df.shape[1] - 2]
    print("Current subject:"+subject)

    for i in tqdm(range(test_df.shape[0])):
        prompt_end = format_example(test_df, i, subject, include_answer=False, cot=cot)
        prompt = gen_prompt(dev_df=dev_df,
                            subject=subject,
                            prompt_end=prompt_end,
                            num_few_shot=num_few_shot,
                            tokenizer=tokenizer,
                            max_length=max_length,
                            cot=cot)
        label = test_df.iloc[i, test_df.shape[1] - 1]

        pred, history = model.chat(tokenizer, prompt, history=[])
        pred = extract_answer(pred)
        if pred and pred[0] in choices:
            cors.append(pred[0] == label)
        all_preds.append(pred.replace("\n", ""))

    acc = np.mean(cors)
    print("Average accuracy {:.3f} - {}".format(acc, subject))
    print("{} results, {} inappropriate formated answers.".format(len(cors), len(all_preds)-len(cors)))
    return acc, all_preds, None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name_or_path", type=str, default="/workspace/models/internlm-chat-7b")
    parser.add_argument("--lora_weights", type=str, default="")
    parser.add_argument("--data_dir", type=str, default="../arcmmlu_data")
    parser.add_argument("--save_dir", type=str, default="../results/InternLM-7B")
    parser.add_argument("--num_few_shot", type=int, default=0)
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--load_in_8bit", action='store_true')
    parser.add_argument("--cot", default=False, action='store_true')
    args = parser.parse_args()

    # Initialize models
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(args.model_name_or_path, trust_remote_code=True, device_map="auto")
    
    # Always use Chat-style evaluation
    run_eval(model, tokenizer, eval_chat, args)
