import torch
from transformers import GPTJForCausalLM, AutoTokenizer

# 모델과 토크나이저 로드
print('model and tokenizer loading...')
model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

# PAD 토큰 설정
print('PAD token setting...')
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = model.config.eos_token_id

# GPU 사용 가능 시 모델을 GPU로 이동
print('CUDA enable...')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


def generate_response(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # 텍스트 생성
    output = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )

    # 생성된 텍스트 디코딩
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response[len(prompt):].strip()


# 대화 루프
print("GPT-J와 대화를 시작합니다. 종료하려면 'quit'를 입력하세요.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break

    prompt = f"User: {user_input}\nAI: "
    response = generate_response(prompt)
    print("AI:", response)

print("대화를 종료합니다.")
