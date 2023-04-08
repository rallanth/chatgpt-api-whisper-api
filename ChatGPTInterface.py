import gradio as gr
import openai, config, subprocess
openai.api_key = config.OPENAI_API_KEY

messages = [{"role": "system", "content": 'You are operating on time series. You determine binary decision represented as question mark in given matrix. The first column in vector represents asset price. The second column value represents binary buy or sell decision, where 1 means buy. You discover relations between vectors in the series and determine missing decision'}]

def transcribe(chat_content):
    global messages

    #audio_filename_with_extension = audio + '.wav'
    #os.rename(audio, audio_filename_with_extension)
    #audio_file = open(audio_filename_with_extension, "rb")
    transcript = chat_content

    messages.append({"role": "user", "content": transcript})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    #response = openai.ChatCompletion.create(model="gpt-4", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    #subprocess.call(["say", system_message['content']])

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

ui = gr.Interface(fn=transcribe, inputs="text", outputs="text").launch()
ui.launch()
