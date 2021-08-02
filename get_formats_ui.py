import json
import dearpygui.dearpygui as dpg
import dearpygui.themes as themes

import youtube_dl

DARK_IMGUI_THEME = themes.create_theme_imgui_dark()
LIGHT_IMGUI_THEME = themes.create_theme_imgui_light()


def get_details_callback():
    url = dpg.get_value(txt_url)
    print("Yaay: " + url)
    results = get_url_details(url)

    dpg.set_value(lbl_title, results['title'])
    dpg.set_value(lbl_extractor, results['extractor_key'])
    dpg.set_value(lbl_format, results['format'])
    # dpg.set_value(lbl_title, "Wooh")
    meta_json = json.dumps(results, indent=4)

    # print(meta_json)
    with open("tmp/content_detail.json", 'w') as f:
        f.write(meta_json)
        f.close()


def get_url_details(url):
    ytdl_opts = {}
    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)
    return meta


with dpg.window(label="main", width=500, height=300) as main_win_id:
    dpg.set_item_theme(main_win_id, LIGHT_IMGUI_THEME)
    dpg.add_text("Check file details")
    txt_url = dpg.add_input_text(label="URL")

    dpg.add_spacing(count=2)

    with dpg.table(header_row=False, row_background=True,
                   borders_innerH=True, borders_outerH=True,
                   borders_innerV=True, borders_outerV=True):

        dpg.add_table_column(width_fixed=True)
        dpg.add_table_column()

        # row 1
        dpg.add_text("Title:")
        dpg.add_table_next_column()
        lbl_title = dpg.add_text("...", wrap=0.0)

        # row 2
        dpg.add_table_next_column()
        dpg.add_text("Extractor:")
        dpg.add_table_next_column()
        lbl_extractor = dpg.add_text("...", wrap=0.0)

        # row 3
        dpg.add_table_next_column()
        dpg.add_text("Format:")
        dpg.add_table_next_column()
        lbl_format = dpg.add_text("...", wrap=0.0)

    dpg.add_spacing(count=2)

    with dpg.table(header_row=True):
        dpg.add_table_column(label="Video Format")
        dpg.add_table_column(label="Audio Format")

        dpg.add_combo(items=["A", "B", "C"], width=-1)
        dpg.add_table_next_column()
        dpg.add_combo(items=["A", "B", "C"], width=-1)

    dpg.add_spacing(count=2)
    dpg.add_button(label="Get details", callback=get_details_callback)


dpg.setup_viewport()
dpg.set_viewport_title(title='c3n7')
dpg.set_viewport_width(1366)
dpg.set_viewport_height(768)

dpg.start_dearpygui()
