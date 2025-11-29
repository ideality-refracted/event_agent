import os


def read_markdown_file_as_string(file_name):
    """
    Reads a Markdown file and returns its content as a string.

    Args:
        file_name (str): The name the Markdown file.

    Returns:
        str: The content of the Markdown file as a string.
    """
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        return markdown_content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None