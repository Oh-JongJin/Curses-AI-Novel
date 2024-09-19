import torch
from transformers import GPTNeoForCausalLM, AutoTokenizer, GenerationConfig
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
MODEL_NAME = "EleutherAI/gpt-neo-1.3B"
LOCAL_MODEL_PATH = "./gpt-neo-1.3B"


# 모델 다운로드 함수
def download_model():
    print("모델 다운로드 중...")
    model = GPTNeoForCausalLM.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    print(f"모델을 {LOCAL_MODEL_PATH}에 저장 중...")
    model.save_pretrained(LOCAL_MODEL_PATH)
    tokenizer.save_pretrained(LOCAL_MODEL_PATH)
    print("모델 다운로드 및 저장 완료!")


# 모델 로드 함수
def load_model():
    print("로컬 모델 로딩 중...")
    model = GPTNeoForCausalLM.from_pretrained(LOCAL_MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_PATH)

    # PAD 토큰 설정
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id

    # GPU 사용 가능 시 모델을 GPU로 이동
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    generation_config = GenerationConfig.from_model_config(model.config)
    generation_config.max_length = 100
    generation_config.num_return_sequences = 1
    generation_config.no_repeat_ngram_size = 2
    generation_config.do_sample = True
    generation_config.temperature = 0.7
    generation_config.pad_token_id = tokenizer.eos_token_id

    return model, tokenizer, device, generation_config


# 응답 생성 함수
def generate_response(prompt, model, tokenizer, device, generation_config):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    output = model.generate(
        **inputs,
        generation_config=generation_config
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response[len(prompt):].strip()


if __name__ == "__main__":
    if not os.path.exists(LOCAL_MODEL_PATH):
        download_model()

    model, tokenizer, device, generation_config = load_model()

    print("GPT-Neo와 대화를 시작합니다. 종료하려면 'quit'를 입력하세요.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        prompt = f"User: {user_input}\nAI: "
        response = generate_response(prompt, model, tokenizer, device, generation_config)
        print("AI:", response)

    print("대화를 종료합니다.")

