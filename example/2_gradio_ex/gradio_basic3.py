import gradio as gr
import numpy as np
def my_function(input1, input2, slider, checkbox, dropdown, radio, file, microphone):
    # 입력 값을 조합하여 결과 생성
    sr, data = microphone
    output1 = f"입력값 처리1: {input1}, Slider 값: {slider}, Checkbox 상태: {checkbox}, Dropdown 선택: {dropdown}, Radio 선택: {radio}, 파일 업로드: {file.name if file else '없음'}"
    output2 = f"입력값 처리2: {input2}"
    output3 = np.flipud(data)
    return output1, output2

app = gr.Interface(
    fn=my_function,
    inputs=[
        gr.Textbox(lines=1, max_lines=6, label="Input 1"),
        gr.Textbox(lines=1, max_lines=6, label="Input 2"),
        gr.Slider(maximum=100, minimum=0, step=5, label="크기조정"),
        gr.Checkbox(label="체크박스"),
        gr.Dropdown(["옵션1", "옵션2", "옵션3"], label="옵션선택창"),
        gr.Radio(["옵션1", "옵션2", "옵션3"], label="옵션선택창"),
        gr.File(label="Upload a file"),
        gr.Microphone()
        ],
    outputs=[
        gr.Textbox(lines=1, max_lines=6, label="Output1"),
        gr.Textbox(lines=1, max_lines=6, label="Output2"),
        gr.Audio(label="Output3") 
        ]
)
app.launch(share=True)
