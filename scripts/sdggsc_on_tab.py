import requests
import json
import gradio as gr
from modules import script_callbacks
import os


def render_html(url,text):
    thead = ('<tr>'
        +'    <th>扩展</th>'
        +'    <th>网址</th>'
        +'    <th>Branch</th>'
        +'    <th>版本信息</th>'
        +'    <th>Date</th>'
        +'    <th>更新</th>'
        +'</tr>'
    )
    msg=''
    if url is None or not url.strip():
      msg = 'Input From url，please'
    elif text is None or not text.strip() or text.strip().lower() == "none":
      msg = 'select Search type，please'

    if msg != "":
        tbody = ('<tr>'
            +'    <td colspan="6" style="text-align:center">'+msg+'</td>'
            +'</tr>'
        )
    else:
        tbody = ('<tr>'
            +'    <td><label><input class="gr-check-radio gr-checkbox" name="two-shot" type="checkbox" checked="checked">'+text+'</label></td>'
            +'    <td><a href="#" target="_blank">'+url+'</a></td>'
            +'    <td>main</td>'
            +'    <td><a href="#" target="_blank">6b55dd52</a></td>'
            +'    <td>Sun Apr  2 11:24:25 2023</td>'
            +'    <td class="extension_status">未知</td>'
            +'</tr>'
        )

    html = (
        '<table style="width: 100%;">'
        +'<thead>'
        +thead
        +'</thead>'
        +'<tbody>'
        +tbody
        +'</tbody>'
        +'</table>'
    )

    return  html

def on_ui_tabs():
    with gr.Blocks() as sdggsc_interface:
    
        url = gr.Textbox(label="From url")
        with gr.Row():
            strs=['None',"checkpoints", "controlnets", "embeddings", "loras", "vaes", "lycoris", "clips", "hypernetworks", "esrgans"]
            a=gr.Dropdown(label="Search type", interactive=True, elem_id="script_list", choices=strs, value='None')
            # ep=gr.Examples(
            #     examples=[['asdc','checkpoints']],
            #     inputs=[url,a],
            #     outputs=op,
            #     fn=render_html
            # )
            name = gr.Textbox(label="Search name")
        section_btn = gr.Button("Search")
        op=gr.HTML()
    
        section_btn.click(render_html, [url,a], op)

    return (sdggsc_interface, "GoogleDriveSharingCenter", "sdggsc_interface"),
  
script_callbacks.on_ui_tabs(on_ui_tabs)
