import os
import PIL.Image
import PIL.ImageTk
import pyglet
import pyperclip
import time
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

from number import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pyglet.font.add_file(resource_path("share_tech_mono.ttf"))

class Numconvert(ThemedTk):

    prefix_conversion = {"binary": "0b", "octal": "0o", "decimal": "0d", "hexadecimal": "0x"}
    bases = {"binary": 2, "octal": 8, "decimal": 10, "hexadecimal": 16}

    def __init__(self):
        ThemedTk.__init__(self, themebg = True)
        self.set_theme("equilux")
        self.title("numconvert")
        self.iconbitmap(resource_path("icon.ico"))
        self.geometry("400x500")
        self.resizable(False, False)

        font = "Share Tech Mono"
        entry_font = "Consolas"

        copy_image = PIL.Image.open(resource_path("copy.png"))
        copy_image.thumbnail((20, 20), PIL.Image.ANTIALIAS)
        copy_image = PIL.ImageTk.PhotoImage(copy_image)

        error_image = PIL.Image.open(resource_path("error.png"))
        error_image.thumbnail((20, 20), PIL.Image.ANTIALIAS)
        error_image = PIL.ImageTk.PhotoImage(error_image)

        style = Style()
        style.configure("TButton", foreground = "#777777", font = (font, 11))
        style.configure("convert.TButton", foreground = "#58932D")
        style.configure("TEntry", selectbackground = "#555555")
        style.configure("TLabel", font = (font, 11))
        style.configure("TLabelframe.Label", font = (font, 11), foreground = "#777777", background = "#414141")
        style.configure("TLabelframe.TButton", background = "#414141")
        style.configure("clear.TLabelframe.TButton", foreground = "#E03C31", background = "#414141")
        style.configure("TLabelframe.TCombobox", background = "#414141", selectbackground = "#464646")
        style.configure("choosing.TLabelframe.TCombobox", background = "#414141", selectbackground = "#6A6A6A")
        style.configure("TLabelframe.TEntry", background = "#414141")
        style.configure("invalid.TLabelframe.TEntry", foreground = "#E03C31", background = "#414141")
        style.configure("TLabelframe.TLabel", foreground = "#777777", background = "#414141")

        def character_limit(object, limit):
            if len(object.get()) >= limit:
                object.set(object.get()[:limit])
            if object == self.value_string:
                self.value_error_label.place_forget()

        def copy_number():
            pyperclip.copy(self.prefix_entry.get() + self.value_entry.get())
            self.focus()

        def copy_converted_number():
            pyperclip.copy(self.converted_prefix_entry.get() + self.converted_value_entry.get())
            self.focus()

        def clear(widget):
            widget.delete(0, "end")

        def clear_number():
            self.type_combobox.set("")
            set_prefix(self.type_combobox, self.prefix_entry)
            clear(self.prefix_entry)
            clear(self.value_entry)
            self.type_error_label.place_forget()#
            self.value_error_label.place_forget()
            self.value_error_tooltip.destroy()
            self.focus()

        def clear_converted_number():
            self.converted_type_combobox.set("")
            set_prefix(self.converted_type_combobox, self.converted_prefix_entry)
            clear(self.converted_prefix_entry)
            clear(self.converted_value_entry)
            self.converted_type_error_label.place_forget()
            self.focus()

        def convert():
            type = self.type_combobox.get().strip()
            converted_type = self.converted_type_combobox.get().strip()
            value = self.value_entry.get().strip()
            number = None
            if type and value:
                try:
                    number = Number(value, Numconvert.bases[type])
                    clear(self.converted_value_entry)
                except ValueError:
                    self.value_error_label.place(x = 52.5, y = 95, anchor = "center")
                    self.value_error_tooltip.destroy()
                    self.value_error_tooltip = Tooltip(self.value_error_label, "invalid value", color = "#E03C31")
            if not type:
                self.type_error_label.place(x = 90, y = 40, anchor = "center")
            if not value:
                self.value_error_label.place(x = 52.5, y = 95, anchor = "center")
                self.value_error_tooltip.destroy()
                self.value_error_tooltip = Tooltip(self.value_error_label, "enter a value", color = "#E03C31")
            if number and converted_type:
                self.converted_value_entry.insert(0, number.convert(Numconvert.bases[converted_type]))
            elif not converted_type:
                self.converted_type_error_label.place(x = 90, y = 40, anchor = "center")

            self.focus()

        def switch():
            prefix_entry = self.prefix_entry.get()
            value_entry = self.value_entry.get()
            type_combobox = self.type_combobox.current()
            converted_prefix_entry = self.converted_prefix_entry.get()
            converted_value_entry = self.converted_value_entry.get()
            converted_type_combobox = self.converted_type_combobox.current()

            clear_number()
            clear_converted_number()

            self.prefix_entry.insert(0, converted_prefix_entry)
            self.value_entry.insert(0, converted_value_entry)
            self.type_combobox.current(converted_type_combobox)
            self.converted_prefix_entry.insert(0, prefix_entry)
            self.converted_value_entry.insert(0, value_entry)
            self.converted_type_combobox.current(type_combobox)

            self.focus()

        def set_prefix(combobox_widget, prefix_widget):
            type = combobox_widget.get().strip()
            if type in Numconvert.prefix_conversion:
                clear(prefix_widget)
                prefix_widget.config(state = "enabled")
                prefix_widget.insert(0, Numconvert.prefix_conversion[type])
            elif type == "":
                clear(prefix_widget)
                prefix_widget.config(state = "enabled")
            else:
                clear(prefix_widget)
                prefix_widget.config(state = "disabled")

        def set_number_prefix(event):
            self.type_error_label.place_forget()
            self.type_combobox.configure(style = "TLabelframe.TCombobox")
            set_prefix(self.type_combobox, self.prefix_entry)

        def set_converted_number_prefix(event):
            self.converted_type_error_label.place_forget()
            self.converted_type_combobox.configure(style = "TLabelframe.TCombobox")
            set_prefix(self.converted_type_combobox, self.converted_prefix_entry)

        def combobox_change_style(event):
            combobox = event.widget
            combobox.configure(style = "choosing.TLabelframe.TCombobox")


        self.number_labelframe = LabelFrame(self, text = "Number", width = 380, height = 215)
        self.number_labelframe.grid_propagate(0)
        self.number_labelframe.place(x = 10, y = 10)

        self.type_error_label = Label(self.number_labelframe, style = "TLabelframe.TLabel", image = error_image)
        self.type_error_label.image = error_image
        Tooltip(self.type_error_label, "select a type", color = "#E03C31")

        self.type_string = StringVar()
        self.type_combobox = Combobox(self.number_labelframe, style = "TLabelframe.TCombobox", textvariable = self.type_string, width = 18, state = "readonly", exportselection = 0, values = ["", " binary", " octal", " decimal", " hexadecimal"], font = (font, 10))
        self.type_combobox.place(x = 190, y = 40, anchor = "center")
        self.type_combobox.bind("<Button-1>", combobox_change_style)
        self.type_combobox.bind("<<ComboboxSelected>>", set_number_prefix)
        Tooltip(self.type_combobox, "select type")

        self.value_error_label = Label(self.number_labelframe, style = "TLabelframe.TLabel", image = error_image)
        self.value_error_label.image = error_image
        self.value_error_tooltip = Tooltip(self.value_error_label, "enter a value", color = "#E03C31")

        self.prefix_string = StringVar()
        self.prefix_string.trace("w", lambda *args: character_limit(self.prefix_string, 2))
        self.prefix_entry = Entry(self.number_labelframe, style = "TLabelframe.TEntry", textvariable = self.prefix_string, width = 2, font = (entry_font, 11))
        self.prefix_entry.place(x = 90, y = 95, anchor = "center")
        self.prefix_label = Label(self.number_labelframe, style = "TLabelframe.TLabel", text = "Prefix")
        self.prefix_label.place(x = 90, y = 125, anchor = "center")

        self.value_string = StringVar()
        self.value_string.trace("w", lambda *args: character_limit(self.value_string, 15))
        self.value_entry = Entry(self.number_labelframe, style = "TLabelframe.TEntry", textvariable = self.value_string, width = 15, font = (entry_font, 11))
        self.value_entry.place(x = 190, y = 95, anchor = "center")
        self.value_label = Label(self.number_labelframe, style = "TLabelframe.TLabel", text = "Value")
        self.value_label.place(x = 190, y = 125, anchor = "center")

        self.copy_number_button = Button(self.number_labelframe, style = "TLabelframe.TButton", command = copy_number, image = copy_image, width = 5, cursor = "hand2")
        self.copy_number_button.image = copy_image
        self.copy_number_button.place(x = 310, y = 95, anchor = "center")
        Tooltip(self.copy_number_button, "copy number")

        self.clear_number_button = Button(self.number_labelframe, style = "clear.TLabelframe.TButton", command = clear_number, text = "\u274c", width = 5, cursor = "hand2")
        self.clear_number_button.place(x = 189, y = 170, anchor = "center")
        Tooltip(self.clear_number_button, "clear number")

        self.convert_button = Button(self, style = "convert.TButton", command = convert, text = "\u21ba", width = 5, cursor = "hand2")
        self.convert_button.place(x = 150, y = 253, anchor = "center")
        Tooltip(self.convert_button, "convert")

        self.switch_button = Button(self, style = "convert.TButton", command = switch, text = "\u21f5", width = 5, cursor = "hand2")
        self.switch_button.place(x = 250, y = 253, anchor = "center")
        Tooltip(self.switch_button, "switch")

        self.converted_number_labelframe = LabelFrame(self, text = "Converted Number", width = 380, height = 215)
        self.converted_number_labelframe.grid_propagate(0)
        self.converted_number_labelframe.place(x = 10, y = 275)

        self.converted_type_error_label = Label(self.converted_number_labelframe, style = "TLabelframe.TLabel", image = error_image)
        self.converted_type_error_label.image = error_image
        Tooltip(self.converted_type_error_label, "select a type", color = "#E03C31")

        self.converted_type_string = StringVar()
        self.converted_type_combobox = Combobox(self.converted_number_labelframe, style = "TLabelframe.TCombobox", textvariable = self.converted_type_string, width = 18, state = "readonly", exportselection = 0, values = ["", " binary", " octal", " decimal", " hexadecimal"], font = (font, 10))
        self.converted_type_combobox.bind("<Button-1>", combobox_change_style)
        self.converted_type_combobox.place(x = 190, y = 40, anchor = "center")
        self.converted_type_combobox.bind("<<ComboboxSelected>>", set_converted_number_prefix)
        Tooltip(self.converted_type_combobox, "select type")

        self.converted_prefix_string = StringVar()
        self.converted_prefix_string.trace("w", lambda *args: character_limit(self.converted_prefix_string, 2))
        self.converted_prefix_entry = Entry(self.converted_number_labelframe, style = "TLabelframe.TEntry", textvariable = self.converted_prefix_string, width = 2, font = (entry_font, 11))
        self.converted_prefix_entry.place(x = 90, y = 95, anchor = "center")
        self.converted_prefix_label = Label(self.converted_number_labelframe, style = "TLabelframe.TLabel", text = "Prefix")
        self.converted_prefix_label.place(x = 90, y = 125, anchor = "center")

        self.converted_value_string = StringVar()
        self.converted_value_string.trace("w", lambda *args: character_limit(self.converted_value_string, 15))
        self.converted_value_entry = Entry(self.converted_number_labelframe, style = "TLabelframe.TEntry", textvariable = self.converted_value_string, width = 15, font = (entry_font, 11))
        self.converted_value_entry.place(x = 190, y = 95, anchor = "center")
        self.converted_value_label = Label(self.converted_number_labelframe, style = "TLabelframe.TLabel", text = "Value")
        self.converted_value_label.place(x = 190, y = 125, anchor = "center")

        self.copy_converted_number_button = Button(self.converted_number_labelframe, style = "TLabelframe.TButton", command = copy_converted_number, image = copy_image, width = 5, cursor = "hand2")
        self.copy_converted_number_button.image = copy_image
        self.copy_converted_number_button.place(x = 310, y = 95, anchor = "center")
        Tooltip(self.copy_converted_number_button, "copy converted number")

        self.clear_converted_number_button = Button(self.converted_number_labelframe, style = "clear.TLabelframe.TButton", command = clear_converted_number, text = "\u274c", width = 5, cursor = "hand2")
        self.clear_converted_number_button.place(x = 189, y = 170, anchor = "center")
        Tooltip(self.clear_converted_number_button, "clear converted number")


class Tooltip:

    def __init__(self, widget, text, color = "#555555", wait_time = 1000, wraplength = 180):
        self.__widget = widget
        self.__text = text
        self.__color = color
        self.__wait_time = wait_time
        self.__wraplength = wraplength
        cursor_type = str(self.__widget["cursor"])
        if cursor_type == "" or cursor_type == "arrow":
            self.__padding = (0, 22)
        elif cursor_type == "hand2":
            self.__padding = (-6, 27)
        self.__widget.bind("<Enter>", self.__enter)
        self.__widget.bind("<Leave>", self.__leave)
        self.__widget.bind("<Motion>", self.__check)
        self.__widget.bind("<ButtonPress>", self.__leave)
        self.__timestamp = None
        self.__window = None
        self.__x, self.__y = None, None

    def destroy(self):
        if self.__window:
            self.__window.destroy()

    def __enter(self, event):
        self.__timestamp = time.time()
        self.__widget.after(self.__wait_time, self.__show_tip)

    def __leave(self, event):
        self.__timestamp = None
        self.__x, self.__y = None, None
        if self.__window:
            self.__window.destroy()
            self.__window = None

    def __check(self, event):
        if (self.__x and self.__y) and (abs(self.__x - self.__widget.winfo_pointerx()) > 10 or abs(self.__y - self.__widget.winfo_pointery()) > 10):
            self.__leave(event)

    def __show_tip(self):
        if not self.__timestamp or self.__timestamp > time.time() - (self.__wait_time-100)/1000:
            return
        self.__x, self.__y = self.__widget.winfo_pointerx(), self.__widget.winfo_pointery()
        self.__window = Toplevel(self.__widget)
        self.__window.wm_overrideredirect(True)
        self.__window.wm_geometry(f"+{self.__x+self.__padding[0]}+{self.__y+self.__padding[1]}")
        self.__window.config(highlightthickness = 1)
        self.__window.config(highlightbackground = "#555555")
        label = Label(self.__window, text = self.__text, justify = "left", foreground = self.__color, background = "#fefefe", relief = "solid", borderwidth = 0, wraplength = self.__wraplength)
        label.pack(padx = 2, pady = 2)


if __name__ == "__main__":
    numconvert = Numconvert().mainloop()
