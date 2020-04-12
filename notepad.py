import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
main = tk.Tk()
main.geometry("1000x600")
main.title("Nura Industries Notepad")
main.wm_iconbitmap("micon.png")

main_menu = tk.Menu()

new_icon = tk.PhotoImage(file="icon/new.png")
open_icon = tk.PhotoImage(file="icon/open.png")
save_icon = tk.PhotoImage(file="icon/save.png")
save_as_icon = tk.PhotoImage(file="icon/save_as.png")
exit_icon = tk.PhotoImage(file="icon/exit.png")

file = tk.Menu(main_menu, tearoff=False)

# Edit menu icon
copy_icon = tk.PhotoImage(file="icon/copy.png")
paste_icon = tk.PhotoImage(file="icon/paste.png")
cut_item_icon = tk.PhotoImage(file="icon/cut.png")
clear_icon = tk.PhotoImage(file="icon/clear_all.png")
find_icon = tk.PhotoImage(file="icon/find.png")

edit = tk.Menu(main_menu, tearoff=False)

tool_bar = tk.PhotoImage(file="icon/tool_bar.png")
status_bar = tk.PhotoImage(file="icon/status_bar.png")

view = tk.Menu(main_menu, tearoff=False)

# color image
light_theme = tk.PhotoImage(file="icon/light_default.png")
light_plus = tk.PhotoImage(file="icon/light_plus.png")
dark_theme = tk.PhotoImage(file="icon/dark.png")
red_theme = tk.PhotoImage(file="icon/red.png")
monokia_theme = tk.PhotoImage(file="icon/monokai.png")
night_theme = tk.PhotoImage(file="icon/night_blue.png")


color_theme = tk.Menu(main_menu, tearoff=False)
theme_choose = tk.StringVar()

# color theme set
color_icon = (light_plus, light_theme, dark_theme, red_theme, monokia_theme, night_theme)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus'    : ('#474747', '#e0e0e0'),
    'Dark'          : ('#c4c4c4', '#2d2d2d'),
    'Red'           : ('#2d2d2d', '#ffe8e8'),
    'Monokai'       : ('#d3b774', '#474747'),
    'Night Blue'    : ('#ededed', '#6b9dc2')
}

main_menu.add_cascade(label = "File", menu = file)
main_menu.add_cascade(label = "Edit", menu = edit)
main_menu.add_cascade(label = "View", menu = view)
main_menu.add_cascade(label = "Color Theme", menu = color_theme)

tool_bar_label = ttk.Label(main)
tool_bar_label.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label, width=30, textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5, pady=5)

# size box
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width=20, textvariable = size_variable, state="readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

# bold button
bold_icon = tk.PhotoImage(file="icon/bold.png")
bold_btn = ttk.Button(tool_bar_label, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# Italic button
italic_icon = tk.PhotoImage(file="icon/italic.png")
italic_btn = ttk.Button(tool_bar_label, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# Underline button
underline_icon = tk.PhotoImage(file="icon/underline.png")
underline_btn = ttk.Button(tool_bar_label, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# font color button
font_color_icon = tk.PhotoImage(file="icon/font_color.png")
font_color_btn = ttk.Button(tool_bar_label, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# align left
align_left_icon = tk.PhotoImage(file="icon/align_left.png")
align_left_btn = ttk.Button(tool_bar_label, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center
align_center_icon = tk.PhotoImage(file="icon/align_center.png")
align_center_btn = ttk.Button(tool_bar_label, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# align right
align_right_icon = tk.PhotoImage(file="icon/align_right.png")
align_right_btn = ttk.Button(tool_bar_label, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)


# text editor
text_editor = tk.Text(main)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family function
font_now = "Arial"
font_size_now = 16


def change_font(main):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font=(font_now, font_size_now))


def change_size(main):
    global font_size_now

    font_size_now = size_variable.get()
    text_editor.configure(font=(font_now, font_size_now))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)


# Bold function
def bold_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font=(font_now, font_size_now, "bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font=(font_now, font_size_now, "normal"))


# italic function
bold_btn.configure(command = bold_fun)


def italic_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"]=='roman':
        text_editor.configure(font=(font_now, font_size_now, "italic"))
    if text_get.actual()["slant"]=='italic':
        text_editor.configure(font=(font_now, font_size_now, "roman"))


italic_btn.configure(command=italic_fun)


# underline function
def underline_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font=(font_now, font_size_now, "underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font=(font_now, font_size_now, "normal"))


underline_btn.configure(command=underline_fun)


def color_choose():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=color_choose)


# alignment function left
def align_left():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "left")


align_left_btn.configure(command=align_left)


def align_right():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "right")


align_right_btn.configure(command=align_right)


def align_center():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "center")


align_center_btn.configure(command=align_center)

# status bar
status_bars=ttk.Label(main,text="status bar")
status_bars.pack(side=tk.BOTTOM)


text_change = False


def change_word(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word=len(text_editor.get(1.0, "end-1c").split())
        character = len(text_editor.get(1.0, "end-1c").replace(" ",""))
        status_bars.config(text=f"character:{character} word:{word}")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", change_word)


# color theme function

def change_theme():
    get_theme = theme_choose.get()
    colour_tuple = color_dict.get(get_theme)
    fg_color, bg_color = colour_tuple[0], colour_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count = 0

for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icon[count], variable= theme_choose, compound=tk.LEFT, command=change_theme)
    count += 1

# view menu


# tool bar and status bar hide
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)


def hide_toolbar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar_label.pack_forget()
        show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_tool_bar = True


def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar = True


view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0, variable=show_tool_bar, image=tool_bar, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0, variable=show_status_bar, image=status_bar, compound=tk.LEFT, command=hide_statusbar)

# edit menu
edit.add_command(label="copy", image=copy_icon, compound=tk.LEFT, accelerator="ctrl+c", command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_item_icon, compound=tk.LEFT, accelerator="ctrl+x",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear", image=clear_icon, compound=tk.LEFT, accelerator="ctrl+Alt+x",command=lambda:text_editor.delete(1.0, tk.END))


# define find
def find_fun():

    def find(event=None):
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground="red", background="blue")

    def replace(event=None):
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_popup = tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("find word")
    find_popup.resizable(0,0)

    # frame for find
    find_fram = ttk.LabelFrame(find_popup, text="find and Replace word")
    find_fram.pack(pady=20)

    text_find = ttk.Label(find_fram, text="Find")
    text_replace = ttk.Label(find_fram, text="Replace")

    find_input = ttk.Entry(find_fram, width=30)
    replace_input = ttk.Entry(find_fram, width=30)

    find_button = ttk.Button(find_fram, text="Find", command=find)
    replace_button = ttk.Button(find_fram, text="Replace", command=replace)

    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)


edit.add_command(label = "Find", image = find_icon, compound=tk.LEFT, accelerator="ctrl+f", command=find_fun)

# file menu
text_url = " "


def new_file(event=None):
    global text_url
    text_editor.delete(1.0, tk.END)


file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="ctrl+N", command=new_file)


def open_file(event=None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir=os.getcwd(), title="select file", filetypes=(("Text file","*.txt"), ("All files", "*.*")))
    try:
        with open(text_url, "r") as for_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main.title(os.path.basename((text_url)))


file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="ctrl+o", command=open_file)


def save_file(event=None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0, tk.END))
            with open(text_url, "w", encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
            content2 = text_editor.get(1.0, tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return


file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="ctrl+s", command=save_file)


def save_as_file(event=None):
    global text_url
    try:
        content = text_editor.get(1.0, tk.END)
        text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
        text_url.write(content)
        text_url.close()

    except:
        return


file.add_command(label="Save as", image=save_as_icon, compound=tk.LEFT, accelerator="ctrl+alt+s", command=save_as_file)


def exit_fun(event=None):
    global text_url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel("warning", "DO you want to save this file")
            if mbox is True:
                if text_url:
                    content = text_editor.get(1.0, tk.END)
                    with open(text_url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        main.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    text_url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
                    text_url.write(content2)
                    text_url.close()
                    main.destroy()
            elif mbox is False:
                main.destroy()
        else:
            main.destroy()
    except:
        return


file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="ctrl+", command=exit_fun)


main.config(menu=main_menu)
main.mainloop()