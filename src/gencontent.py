import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if filename.endswith(".md"):  # Only convert Markdown files
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path)
        else:
            # Ensure the destination directory is created
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")

    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Ensure `dest_path` is a file, not a directory
    if os.path.isdir(dest_path):
        dest_path += ".html"

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as to_file:
        to_file.write(template)

def extract_title(md):
    for line in md.split("\n"):
        if line.startswith("# "):
            return line[2:]
    return "Untitled"
