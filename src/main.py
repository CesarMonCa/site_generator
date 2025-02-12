import os
import shutil
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive
import subprocess

# Directories
dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

# Use pythons built in server to open the files from public into the browser
def start_server():
    os.chdir(dir_path_public)  # This changes the directory
    subprocess.Popen(["python3", "-m", "http.server", "8888"])  # start the server
    webbrowser.open("http://localhost:8888")  # Open it in browser

# This function will convert a single md file to html
def convert_single_file():
    md_file = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])

    if not md_file:
        messagebox.showinfo("No file selected", "Please select a Markdown file to convert.")
        return

    output_dir = filedialog.askdirectory(title="Select Output Folder")

    if not output_dir:
        messagebox.showinfo("No folder selected", "Using default output folder: ./output")
        output_dir = "./output"

    os.makedirs(output_dir, exist_ok=True)

    generate_pages_recursive(md_file, template_path, output_dir)
    messagebox.showinfo("Conversion Complete", f"HTML file saved in {output_dir}")

# This function will convert all the files in public
def convert_all_and_serve():
    result = messagebox.askyesno("Run Default Mode", "Do you want to convert all Markdown files in the public directory and view them offline?")
    
    if result:
        if os.path.exists(dir_path_public):
            shutil.rmtree(dir_path_public)

        copy_files_recursive(dir_path_static, dir_path_public)
        generate_pages_recursive(dir_path_content, template_path, dir_path_public)

        messagebox.showinfo("Success", "Conversion complete! Opening the offline site...")
        start_server()  # Start server & open browser

# Use TKinter to to open a GUI
def run_gui():
    root = tk.Tk()
    root.title("Markdown to HTML Converter")
    root.geometry("400x300")

    label = tk.Label(root, text="Choose an option:", font=("Arial", 12))
    label.pack(pady=10)

    btn1 = tk.Button(root, text="Convert a Single Markdown File", command=convert_single_file, width=40, height=2)
    btn1.pack(pady=10)

    btn2 = tk.Button(root, text="Convert All & View Offline", command=convert_all_and_serve, width=40, height=2)
    btn2.pack(pady=10)

    btn_exit = tk.Button(root, text="Exit", command=root.quit, width=40, height=2)
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
