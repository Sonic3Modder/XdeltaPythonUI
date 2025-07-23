import customtkinter
from tkinter import filedialog
from CTkMenuBar import *
import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def run_executable(source, patch, output):
    try:
        result = subprocess.run(
            ["xdelta3.exe", "-d", "-s", source, patch, output],
            capture_output=True,
            text=True
        )
        logging.info(result.stdout)
        logging.error(result.stderr)
        return result.returncode == 0
    except Exception as e:
        logging.error(f"Error running xdelta3: {e}")
        return False


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("255x250")
        self.title("About")
        customtkinter.CTkLabel(self, text="About Xdelta Py UI").pack(padx=20, pady=10)
        customtkinter.CTkLabel(self, text="This is a simple UI for Xdelta patching.").pack(padx=20, pady=10)
        customtkinter.CTkLabel(self, text="Version 1.0", font=("Arial", 10, "italic")).pack(padx=20, pady=10)


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("400x450")
        self.title("Xdelta Py UI")
        self._set_appearance_mode("System")

        self.sourcefile = None
        self.patchfile = None

        menu = CTkTitleMenu(master=self)
        file_button = menu.add_cascade("File")
        about_button = menu.add_cascade("About")

        file_menu = CustomDropdownMenu(widget=file_button)
        file_menu.add_option("Open Source File", command=self.open_source_file)
        file_menu.add_option("Open Patch File", command=self.open_patch_file)
        file_menu.add_separator()
        file_menu.add_option("Exit", command=self.quit)

        about_menu = CustomDropdownMenu(widget=about_button)
        about_menu.add_option("Open About Window", command=self.open_toplevel)

        self.toplevel_window = None

        self.file_entry = customtkinter.CTkEntry(self, placeholder_text="No source file selected")
        self.file_entry.pack(pady=10, padx=20, fill="x")
        self.file_entry.configure(state="disabled")

        self.source_button = customtkinter.CTkButton(self, text="Change Source File", command=self.open_source_file)
        self.source_button.pack(pady=10, padx=20, fill="x")

        self.patch_entry = customtkinter.CTkEntry(self, placeholder_text="No patch file selected")
        self.patch_entry.pack(pady=10, padx=20, fill="x")
        self.patch_entry.configure(state="disabled")

        self.patch_button = customtkinter.CTkButton(self, text="Change Patch File", command=self.open_patch_file)
        self.patch_button.pack(pady=10, padx=20, fill="x")

        self.output_entry = customtkinter.CTkEntry(self, placeholder_text="Output file name (e.g., patched.win)")
        self.output_entry.pack(pady=10, padx=20, fill="x")

        self.run_button = customtkinter.CTkButton(self, text="Apply Patch", command=self.run_patch)
        self.run_button.pack(pady=20, padx=20, fill="x")

    def open_source_file(self):
        self.sourcefile = filedialog.askopenfilename(filetypes=[("GM Data Files", "*data.win")])
        if self.sourcefile:
            self.file_entry.configure(state="normal")
            self.file_entry.delete(0, 'end')
            self.file_entry.insert(0, self.sourcefile)
            self.file_entry.configure(state="disabled")

    def open_patch_file(self):
        self.patchfile = filedialog.askopenfilename(filetypes=[("Xdelta Patch Files", "*.xdelta")])
        if self.patchfile:
            self.patch_entry.configure(state="normal")
            self.patch_entry.delete(0, 'end')
            self.patch_entry.insert(0, self.patchfile)
            self.patch_entry.configure(state="disabled")

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()

    def run_patch(self):
        output_path = self.output_entry.get()
        if not self.sourcefile or not self.patchfile or not output_path:
            logging.error("Missing source, patch, or output path.")
            return

        success = run_executable(self.sourcefile, self.patchfile, output_path)
        if success:
            logging.info("Patch applied successfully.")
        else:
            logging.error("Failed to apply patch.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
