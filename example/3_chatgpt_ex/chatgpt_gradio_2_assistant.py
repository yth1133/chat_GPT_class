import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv
current_dir = os.path.dirname(os.path.abspath(__file__)) # 실행하려는 파일의 경로
dotenv_path = os.path.join(current_dir, '../../', '.env') # 실행파일 두개상위 경로의 env 파일
load_dotenv(dotenv_path)
open_api_key = os.getenv("TEST_KEY")
client = OpenAI(api_key=open_api_key)


# message는 유저의 채팅 메시지, history는 채팅 기록
message_history = [{"role": "system", "content": "당신은 챗봇 상담원입니다"}]
def response(message, history):
    tmp_msg = {"role": "user", "content": message}
    if history:
        assistant_msg = {"role": "assistant", "content": history[-1][-1]} # 이전 대화 내용 history 에 있는 내용 가져오기
        message_history.append(assistant_msg)   # 이전 gpt응답 내용 assistant 로 추가
    message_history.append(tmp_msg)     # 새롭게 질문할 내용
    print("질문내용입니다: ", message)
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo", # 사용할 모델명 입력,\
        messages = message_history)
    chatgpt_res = response.choices[0].message.content
    print("답변입니다: ", chatgpt_res)
    return chatgpt_res

gr.ChatInterface(
        fn=response,
        textbox=gr.Textbox(placeholder="채팅적어주세요..", container=False, scale=7),
        title="그라디오를 이용한 chatGPT api 사용법입니다",
        description="chatGPT를 이용한 답변을 받아보세요",
        theme="soft",
        examples=[["그라디오 사용법 알려줘"], ["chatGPT 사용법 알려줘"], ["챗봇 구현방법 알려줘"]],
        retry_btn="다시보내기 ↩",
        undo_btn="이전챗 삭제 ❌",
        clear_btn="전챗 삭제 💫",
).launch(share=True)