import gradio as gr

def gradio_basic(name): 

    return f"안녕하세요 {name} 님, 그라디오 기본편입니다."

app =  gr.Interface(fn = gradio_basic, 
                    title="그라디오 기본편 실습",
                    inputs="text",
                    outputs="text",
)
app.launch() 
