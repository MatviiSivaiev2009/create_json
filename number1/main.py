import customtkinter
from PIL import Image
import os
import json

app = customtkinter.CTk()
width = 448 
height = 515 

def create_path(file_name):
    path_file = __file__.split("\\")
    del path_file[-1]
    # del path_file[-1]
    path_file = "/".join(path_file)
    path_file = os.path.join(path_file, file_name)
    return path_file

app.geometry(f"{width}x{height}")
app.title("App_Json")

font = customtkinter.CTkFont(family = "Inter")

app_frame = customtkinter.CTkFrame(
    master = app,
    corner_radius = 10,
    border_color = "#FCA625",
    border_width = 2,
    fg_color = "#403A3A",
    width = width,
    height = height
)
app_frame.place(x = 0, y = 0)

background_image = customtkinter.CTkImage(dark_image = Image.open(create_path("images/bg_image.png")), size = (391, 391))
background_label = customtkinter.CTkLabel(
    master = app_frame,
    image = background_image,
    text = ""
)
background_label.place(x = 28, y = 95)

# json_image = customtkinter.CTkImage(dark_image = Image.open(create_path("images/json_label.png")), size = (110 , 55))
json_title = customtkinter.CTkLabel(
    master = app_frame,
    text = "CREATE\n JSON",
    text_color = "white",
    bg_color = "transparent",
    width = 211,
    height = 45,
    font = customtkinter.CTkFont(family = "Inter", size = 36, weight = "bold")
)
json_title.place(x = 119, y = 10)

name_entry = customtkinter.CTkEntry(
    master = app_frame,
    placeholder_text = "Entry your name: ",
    corner_radius = 10,
    border_color = "#FCA625",
    placeholder_text_color = "#FFFFFF",
    fg_color = "#4F4F4F",
    bg_color = "transparent",
    width = 307,
    height = 66,
    font = customtkinter.CTkFont(family = "Inter", size = 18)
)
name_entry.place(x = 72, y = 115)

surname_entry = customtkinter.CTkEntry(    
    master = app_frame,
    placeholder_text = "Entry your surname: ",
    corner_radius = 10,
    border_color = "#FCA625",
    placeholder_text_color= "#FFFFFF",
    fg_color = "#4F4F4F",
    bg_color = "transparent",
    width = 307,
    height = 66,
    font = customtkinter.CTkFont(family = "Inter", size = 18)
)
surname_entry.place(x = 72, y = 226)

age_entry = customtkinter.CTkEntry(
    master = app_frame,
    placeholder_text = "Entry your age: ",
    corner_radius = 10,
    border_color = "#FCA625",
    placeholder_text_color= "#FFFFFF",
    fg_color = "#4F4F4F",
    bg_color = "transparent",
    width = 307,
    height = 66,
    font = customtkinter.CTkFont(family = "Inter", size = 18)
)
age_entry.place(x = 72, y = 337)

def write_json(path_json):
    try:
        age = int(age_entry.get())
    except ValueError:
        warning_message = customtkinter.CTkToplevel()
        warning_message.geometry("200x80")
        warning_message.title("Error")
        error_label = customtkinter.CTkLabel(
            master = warning_message,
            text = "Error: Age must be an integer"        
        )
        error_label.place(x = 15, y = 30)
        return
    
    # if type(age_entry.get()) == int:
    #     age = age_entry.get
    
    dict = {
        "name": name_entry.get(),
        "surname": surname_entry.get(),
        "age": age
    }
    with open(create_path(path_json), "w") as file:
        json.dump(dict, file, ensure_ascii = False, indent = 4)
        
save_button = customtkinter.CTkButton(
    master = app_frame,
    text = "SAVE",
    corner_radius = 15,
    border_color = "#FCA625",
    border_width = 2,
    fg_color = "#4F4F4F",
    bg_color = "transparent",
    width = 144,
    height = 47,
    font = customtkinter.CTkFont(family = "Inter", size = 18, weight = "bold"),
    command = lambda: write_json("json/1.json")
)
save_button.place(x = 160, y = 434)



       
app.mainloop()
