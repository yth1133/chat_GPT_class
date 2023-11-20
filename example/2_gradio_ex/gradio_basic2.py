import gradio as gr

def gradio_basic(name, age): 

    return f"안녕하세요 {name}({age}) 님, 그라디오 기본편입니다."
excamples = [
    ["홍길동"],
    ["김철수"]
]
app =  gr.Interface(fn = gradio_basic, 
                    title="그라디오 기본편 실습",
                    inputs=[gr.Textbox(lines=5, max_lines=6, label="이름을 입력하세요"),
                            gr.Textbox(lines=5, max_lines=6, label="나이를 입력하세요")],
                    outputs=gr.Textbox(lines=1, max_lines=6, label="결과가 출력됩니다"),
                    examples=excamples) 
app.launch(share=True) 
