import customtkinter
from tkinter import filedialog
from CTkMenuBar import *
import github
from github import *



class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("255x250")
        self.label = customtkinter.CTkLabel(self, text="About Xdelta Py UI")
        self.label.pack(padx=20, pady=20)
        self.label2 = customtkinter.CTkLabel(self, text="This is a simple UI for Xdelta patching.")
        self.label2.pack(padx=20, pady=20)
        self.label3 = customtkinter.CTkLabel(self, text="version 1.0", font=("Arial", 10, "italic"))
        self.label3.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("400x450")
        self.title("Xdelta Py UI")
        self._set_appearance_mode("System")

        
        menu = CTkTitleMenu(master=self)
        button_1 = menu.add_cascade("File")
        button_2 = menu.add_cascade("About")

       
      


        dropdown1 = CustomDropdownMenu(widget=button_1)
        dropdown1.add_option(option="Open Source File", command=lambda: filedialog.askopenfilename(filetypes=[("GM Data Files", "*data.win")]))
        dropdown1.add_option(option="Open Patch File", command=lambda: filedialog.askopenfilename(filetypes=[("Xdelta Patch Files", "*.xdelta")]))
        dropdown1.add_separator()

        dropdown1.add_option(option="Exit", command=self.quit)


        dropdown2 = CustomDropdownMenu(widget=button_2)
        dropdown2.add_option("Open About Window", command=self.open_toplevel)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()






app = App()
app.mainloop()
