import tkinter as tk
from tkinter import filedialog
import markdown

def convert_markdown_to_html(input_md_file):
    # Read the markdown file
    with open(input_md_file, 'r') as md_file:
        md_content = md_file.read()
    
    # Convert markdown content to HTML
    html_content = markdown.markdown(md_content)
    
    return html_content

def save_html_to_file(html_content):
    # Initialize Tkinter root (hidden window)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Ask the user to choose a location and filename for the HTML output
    output_file = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
    
    # Check if the user provided a valid output path
    if output_file:
        # Write the HTML content to the chosen file
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)
        print(f"HTML file saved to: {output_file}")
    else:
        print("No file selected, HTML not saved.")

def main():
    # choose the markdown file
    input_md_file = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    
    if input_md_file:
        html_content = convert_markdown_to_html(input_md_file)
        save_html_to_file(html_content)
    else:
        print("No markdown file selected.")

if __name__ == "__main__":
    main()
