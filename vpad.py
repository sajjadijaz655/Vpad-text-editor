### Vpad text editor Software####
import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
main_application=tk.Tk()

main_application.title("Vpad Text Editor")

#####################  Main menu #################
#----------------------End menu -----------------#
main_menu=tk.Menu()

    ## File icons 

new_icon=tk.PhotoImage(file="D:/icons/new.png")
open_icon=tk.PhotoImage(file="D:/icons/open.png")
save_icon=tk.PhotoImage(file="D:/icons/save.png")
save_as_icon=tk.PhotoImage(file="D:/icons/save_as.png")
exit_icon=tk.PhotoImage(file="D:/icons/exit.png",height=20,width=20)

file=tk.Menu(main_menu,tearoff=False)

## File command
       ## new functionality
url=""
def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0,tk.END)
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="ctrl+N",command=new_file)
        
        ### open functionality

def open_file(event=None):
        global url
        url=filedialog.askopenfilename(initialdir=os.getcwd(),title="select file",filetypes=(("text file","*.txt"),("All file","*.*")))
        try:
            with open(url,"r")as fr:
                text_editor.delete(1.0,tk.END)
                text_editor.insert(1.0,fr.read())
        except FileNotFoundError:
            return
        except:
            return
        main_application.title(os.path.basename(url))
file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="ctrl+o",command=open_file)
## Save file functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open (url,"w",encoding="utf-8")as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("text file","*.txt"),("All file","*.*")))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
file.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="ctrl+s",command=save_file)
 
 ## Save as functionality
def save_as_file(event=None):
     global url
     try:
       content=text_editor.get(1.0,tk.END)
       url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("text file","*.txt"),("All file","*.*")))
       url.write(content)
       url.close
     except: 
       return
file.add_command(label="Save as",image=save_as_icon,compound=tk.LEFT,accelerator="ctrl+shift+s",command=save_as_file)
 
         ## Exit functionality

def exit_file(event=None):
    global url,text_changed
    try:
        if text_changed:
            inbox=messagebox.askyesnocancel("Warning","do you want to save this file?")
            if inbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,"w",encoding="utf-8")as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("text file","*.txt"),("All file","*.*")))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif inbox is False:
                    main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label="Exist",image=new_icon,compound=tk.LEFT,accelerator="ctrl+Q",command=exit_file)

                ### Edit Menu icons###


copy_icon=tk.PhotoImage(file="D:/icons/copy.png")
paste_icon=tk.PhotoImage(file="D:/icons/paste.png")
cut_icon=tk.PhotoImage(file="D:/icons/cut.png")
clear_all_icon=tk.PhotoImage(file="D:/icons/clear_all.png")
find_icon=tk.PhotoImage(file="D:/icons/find.png")

edit=tk.Menu(main_menu,tearoff=False)

      ##add command in edit menu
def find_file(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches +=1
                start_pos=end_pos
                text_editor.tag_config("match",foreground="red",background="yellow")
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)



    find_dialogue=tk.Toplevel()
    find_dialogue.title("Find")
    find_dialogue.resizable(0,0)
    ### Frame
    find_frame=ttk.LabelFrame(find_dialogue,text="Find/Replace")
    find_frame.pack(pady=20)

    ## label
    text_find_label=ttk.Label(find_frame,text="Find :")
    text_replace_label=ttk.Label(find_frame,text="Replace :")
    ## Entery
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    ## Button
    find_button=ttk.Button(find_frame,text="Find",command=find)
    replace_button=ttk.Button(find_frame,text="Replace",command=replace)
    ## label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    ## Entry grid
    find_input.grid(row=0,column=1,padx=4,pady=0)
    replace_input.grid(row=1,column=1,padx=4,pady=0)
    ##Button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)
    find_dialogue.mainloop()


edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="ctlr+c",command=lambda:text_editor.event_generate("<control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="ctlr+v",command=lambda:text_editor.event_generate("<control v>"))
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="ctrl+x",command=lambda:text_editor.event_generate("<control x>"))
edit.add_command(label="Clear",image=clear_all_icon,compound=tk.LEFT,accelerator="ctrl+x",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="find",image=find_icon,compound=tk.LEFT,accelerator="ctrl+f",command=find_file)
                      
                      ## View icons

tool_bar_icon=tk.PhotoImage(file="D:/icons/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="D:/icons/status_bar.png")


view=tk.Menu(main_menu,tearoff=False)
            ## Add checkbutton
          ## view menu functionality
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True



view.add_checkbutton(label="Tool bar",onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="status bar",onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
            
                ### Color theme
                
light_default_icon=tk.PhotoImage(file="D:/icons/light_default.png")
light_plus_icon=tk.PhotoImage(file="D:/icons/light_plus.png")
dark_icon=tk.PhotoImage(file="D:/icons/dark.png")
red_icon=tk.PhotoImage(file="D:/icons/red.png")
monokai_icon=tk.PhotoImage(file="D:/icons/monokai.png")
night_blue_icon=tk.PhotoImage(file="D:/icons/night_blue.png")
color_theme=tk.Menu(main_menu,tearoff=False)

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    "light Default":("#000000","#ffffff"),
    "light plus":("#474747","#eoeoeo"),
    "Dark":("#c4c4c4","#2d2d2d"),
    "Red":("#2d2d2d","#ffe8e8"),
    "Monokia":("#d3b774","#474747"),
    "Night blue":("#ededed","#6b9dc2")
}

         ## color theme functionality
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count +=1

              ### Cascade ###

main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit) 
main_menu.add_cascade(label="View",menu=view) 
main_menu.add_cascade(label="Color Theme",menu=color_theme)

#####################  Tool bar #################


tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
          ### font Box

font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(column=0,row=0,padx=5)

           ## Size box

size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")
font_size["values"]=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

## Bold button ##
bold_icon=tk.PhotoImage(file="D:/icons/bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

## Itallic button ##
italic_icon=tk.PhotoImage(file="D:/icons/italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

## Underline button ##
under_icon=tk.PhotoImage(file="D:/icons/underline.png")
under_btn=ttk.Button(tool_bar,image=under_icon)
under_btn.grid(row=0,column=4,padx=5)

## color_font  button ##
font_color_icon=tk.PhotoImage(file="D:/icons/font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

## align left  button ##
align_left_icon=tk.PhotoImage(file="D:/icons/align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

## align center  button ##
align_center_icon=tk.PhotoImage(file="D:/icons/align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=8,padx=5)

## align Right  button ##
align_right_icon=tk.PhotoImage(file="D:/icons/align_right.png")
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=7,padx=5)

#----------------------End toolbar -----------------#

#####################  text editor #################
text_editor=tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(comman=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

 ## Font family and font size functionality
 #  
current_font_family="Arial"
current_font_size=12
def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)

def change_size(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_size)
            ## Button functionality

 #### bold button functionality
def change_bold():
    text_property=tk.font.Font(font=text_editor["font"]) ## used for check text weight and other property
    if text_property.actual()["weight"]=="normal":
        text_editor.configure(font=(current_font_family,current_font_size,"bold"))
    if text_property.actual()["weight"]=="bold":
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
bold_btn.configure(command=change_bold)

## itallic functionality

def change_italic():
    text_property=tk.font.Font(font=text_editor["font"]) ## used for check text weight and other property
    if text_property.actual()["slant"]=="roman":
        text_editor.configure(font=(current_font_family,current_font_size,"italic"))
    if text_property.actual()["slant"]=="italic":
        text_editor.configure(font=(current_font_family,current_font_size,"roman"))
italic_btn.configure(command=change_italic)

## underline buton functionality

def change_underline():
    text_property=tk.font.Font(font=text_editor["font"]) ## used for check text weight and other property
    if text_property.actual()["underline"]==0:
        text_editor.configure(font=(current_font_family,current_font_size,"underline"))
    if text_property.actual()["underline"]==1:
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
under_btn.configure(command=change_underline)

## font_color functionality
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

                 #### align functionality
#align_left 
def align_left():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_configure("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"left")
align_left_btn.configure(command=align_left)


#align_center 
def align_center():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_configure("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"center")
align_center_btn.configure(command=align_center)

#align_right
def align_right():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_configure("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"right")
align_right_btn.configure(command=align_right)



#----------------------End text editor -----------------#

#####################  Main Statusbar #################

status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
text_changed=False
def change(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,"end-1c").split())
        char=len(text_editor.get(1.0,"end-1c"))
        status_bar.config(text=f"Characters:{char} words:{words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",change)

#----------------------End status bar -----------------#


main_application.config(menu=main_menu)
   ##Bind shortcut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as_file)
main_application.bind("<Control-q>",exit_file)
main_application.bind("<Control-f>",find_file)



main_application.mainloop()

