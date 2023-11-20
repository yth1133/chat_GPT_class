import random
import gradio as gr

def random_response(message, history):
    return message + " "+ random.choice(["반갑습니다", "좋은하루 되세요"])

demo = gr.ChatInterface(random_response)
demo.launch()