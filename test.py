import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv
import pygame
from gtts import gTTS
load_dotenv()
open_api_key = os.getenv("TEST_KEY")
client = OpenAI(api_key=open_api_key)

# 오디오 재생을 위한 코드
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


# message는 유저의 채팅 메시지, history는 채팅 기록
message_history = [{"role": "system", "content": "당신은 챗봇 상담원입니다"}]
def response(message, history):
    tmp_msg = {"role": "user", "content": message}
    if history:
        assistant_msg = {"role": "assistant", "content": history[-1][-1]} # 이전 대화 내용 history 에 있는 내용 가져오기
        message_history.append(assistant_msg)   # 이전 gpt응답 내용 assistant 로 추가
    message_history.append(tmp_msg)     # 새롭게 질문할 내용
    
    # tts 로 출력 확인하기
    txt = "안녕하세요! 저는 여기서 당신을 도와드릴 수 있습니다. 무엇을 도와드릴까요?"
    tts = gTTS(text=txt, lang="ko")
    speech_file_path2 = "./chatgpt_gradio/speech2.mp3"
    tts.save(speech_file_path2)
    chatgpt_res = "실행중"

    play_audio(speech_file_path2)   
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
).launch()