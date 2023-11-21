import gradio as gr
from openai import OpenAI
import os
from gtts import gTTS

# message는 유저의 채팅 메시지, history는 채팅 기록

open_api_key = ""
client = OpenAI(api_key=open_api_key)

message_history = [{"role": "system", "content": "당신은 챗봇 상담원입니다, 짧고 간단하게 대답해주세요"}]

def response(message, history, api_key=None):
    global open_api_key
    if api_key:
        open_api_key = api_key
        tmp_msg = {"role": "user", "content": message}
        if history:
            assistant_msg = {"role": "assistant", "content": history[-1][-1]} # 이전 대화 내용 history 에 있는 내용 가져오기
            message_history.append(assistant_msg)   # 이전 gpt응답 내용 assistant 로 추가
        message_history.append(tmp_msg)     # 새롭게 질문할 내용
        
        client = OpenAI(api_key=open_api_key)

        response = client.chat.completions.create(
            model = "gpt-3.5-turbo-1106", # 사용할 모델명 입력,\
            messages = message_history)
        chatgpt_res = response.choices[0].message.content
        
        return chatgpt_res
    else:
        return "api key 를 입력해주세요 제일 하단에 있습니다."


chat_demo = gr.ChatInterface(
    fn=response,
    textbox=gr.Textbox(placeholder="채팅적어주세요..", container=False, scale=7),
    title="그라디오를 이용한 chatGPT api 사용법입니다",
    description="chatGPT를 이용한 답변을 받아보세요 제일 하단에 본인의 api key를 입력해주세요",
    theme="soft",
    examples=[["그라디오 사용법 알려줘"], ["chatGPT 사용법 알려줘"], ["챗봇 구현방법 알려줘"]],
    retry_btn="다시보내기 ↩",
    undo_btn="이전챗 삭제 ❌",
    clear_btn="전챗 삭제 💫",
    additional_inputs=[
    gr.Textbox(label="API 키", placeholder="API 키를 입력하세요..."),
    ],
    additional_inputs_accordion_name="api key 입력"
    )

chat_demo.launch()
