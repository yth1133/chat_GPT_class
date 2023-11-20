import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
open_api_key = os.getenv("TEST_KEY")
client = OpenAI(api_key=open_api_key)

audio_file= open("/home/yth1133/chatgpt_gradio/audio_test.m4a", "rb")

transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcript.text)