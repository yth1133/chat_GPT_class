from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# .env 파일에 API 키가 저장되어 있는 경우 가져오기
# open_api_key = os.getenv("OPEN_API_KEY")
open_api_key = os.getenv("TEST_KEY")

# 만약 .env 파일에 API 키가 없는 경우 사용자에게 입력 받기 또는 다른 방법으로 획득하기
if open_api_key is None:
    open_api_key = input("API 키를 입력하세요: ")


# .env 파일에 API 키 저장하기
with open(".env", "w") as env_file:
    env_file.write(f"OPEN_API_KEY={open_api_key}\n")

#open_api_key 변수에는 API 키가 저장 확인
print("API 키:", open_api_key)

########### gradio 구현 ###########
client = OpenAI(api_key=open_api_key)

# 기본익히기
response = client.chat.completions.create(
    model = "gpt-3.5-turbo", # 사용할 모델명 입력
    messages=[
        {"role": "system", "content": "당신은 챗봇 상담원입니다"},
        {"role": "user", "content": "안녕하세요 요새 날씨가 춥네요"},
    ]
)
print(response.choices[0].message.content)
