import tkinter as tk
from tkinter import Menu, Text, Scrollbar, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import random
import string
import webbrowser

# Global variables
text_widget = None
original_content = ""
randomize_enabled = False
numerals_enabled = False

# Function to open a file
def open_file():
    global text_widget, original_content
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            original_content = file.read()
            lines = original_content.split('\n')[:50]
            truncated_content = '\n'.join(lines)
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, truncated_content)

# Function to export the content to a file
def export_file():
    global text_widget
    text_content = text_widget.get("1.0", tk.END)
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_content)

# Function to toggle randomization
def toggle_randomize():
    global randomize_enabled
    randomize_enabled = not randomize_enabled
    manipulate_text()

# Function to toggle numerals
def toggle_numerals():
    global numerals_enabled
    numerals_enabled = not numerals_enabled
    manipulate_text()

# Function to manipulate the text based on settings
def manipulate_text():
    global text_widget, original_content, randomize_enabled, numerals_enabled
    text_content = original_content
    manipulated_content = ""
    for line in text_content.splitlines():
        modified_line = line
        if randomize_enabled:
            modified_line = ''.join(random.sample(modified_line, len(modified_line)))
        if numerals_enabled:
            random_numbers = ''.join(random.choice(string.digits) for _ in range(4))
            if random.randint(0, 1) == 0:
                modified_line = random_numbers + modified_line
            else:
                modified_line = modified_line + random_numbers
        manipulated_content += modified_line + '\n'
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, manipulated_content)

# Function to open GitHub profile in a web browser
def github():
    github_url = "https://github.com/tea5122"
    webbrowser.open(github_url)

# Main function to create and run the GUI
def main():
    global text_widget
    root = tk.Tk()
    root.title("AliasGenerator v1.0")
    root.geometry("800x600")
    root.resizable(False, False)
    root.configure(background="#1e1e1e")

    # Set a custom font for the Text widget
    text_font = ("Arial", 12)  # You can adjust the font family and size here

    full_path = os.path.realpath(__file__)
    current_working_directory = os.path.dirname(full_path)
    root.iconbitmap(r"{0}\Icon.ico".format(current_working_directory))

    window_width = 800
    window_height = 600
    window_size = root.winfo_screenwidth()
    height_size = root.winfo_screenheight()
    x = (window_size / 2) - (window_width / 2)
    y = (height_size / 2) - (window_height / 2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

    for i in range(3):
        root.columnconfigure(i, weight=1)
    root.rowconfigure(1, weight=1)

    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(menubar, tearoff=False)
    settings_menu = Menu(menubar, tearoff=False)
    help_menu = Menu(menubar, tearoff=False)

    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_command(label='Export', command=export_file)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=root.destroy)

    settings_menu.add_checkbutton(label="Randomize", onvalue=1, offvalue=0, command=toggle_randomize)
    settings_menu.add_checkbutton(label="Numerals", onvalue=1, offvalue=0, command=toggle_numerals)

    help_menu.add_command(label='Github', command=github)

    menubar.add_cascade(label="File", menu=file_menu)
    menubar.add_cascade(label="Options", menu=settings_menu)
    menubar.add_cascade(label="Help", menu=help_menu)

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Use the custom font for the Text widget
    text_widget = Text(frame, bg="#1e1e1e", fg="#f1f1f1", font=text_font)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.config(yscrollcommand=scrollbar.set)

    root.mainloop()

if __name__ == "__main__":
    main()
