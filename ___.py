import asyncio
import random
import torch
import json
from transformers import pipeline, AutoTokenizer
import requests

async def llm_ask(query="", messages=False):
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers = {"Authorization": f"Bearer {api_key}"}
    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
    pr = r"Simulate 2 experts arguing on {}, reach a conclusion in greater than 50 responses, expert 1 should argue for the notion, expert 2 should argue against the notion, your output should look like this: Expert 1: ... \n Expert 2".format(query)
    if not messages:
        messages = [
            {
                "role": "system",
                "content": "You are a super intelligent person.",
            },
            {
                "role": "user",
                "content": pr,
            }
        ]
    prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
    data = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 10000,
                "do_sample": True,
                "top_p": 0.95,
                "temperature": 0.01,
                "num_return_sequences": 1,
                "return_full_text": False
            }
        }
    response = requests.post(API_URL, headers=headers, json=data).json()

    try:
        out = response[0]["generated_text"]
        with open("output.json", "w") as json_file:
            json.dump(output_data, json_file, indent=4)

        print("Output saved to output.json")
        return [out]
    except Exception as e:
        print(e)
    else:
        out = response["error"]
        with open("output.json", "w") as json_file:
            json.dump(output_data, json_file, indent=4)

        print("Output saved to output.json")
        return [out]

    #print(out["debate"]["rounds"])

    #return out
