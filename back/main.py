import os
import torch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM
import uvicorn

# FastAPI 앱 생성
app = FastAPI()

# CORS 미들웨어 추가 (모든 출처 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GPU 사용 설정
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# 모델 로드
model_id = "Bllossom/llama-3.2-Korean-Bllossom-3B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

#서버 구축
@app.get("/chat")
async def chat(q: str):
    instruction = q

    messages = [
        {"role": "user", "content": f"{instruction}"}
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.convert_tokens_to_ids("<|end_of_text|>"),
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        max_new_tokens=512,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9
    )

    result = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)

    return {"response": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
