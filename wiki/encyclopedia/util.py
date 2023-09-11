import re, markdown2
from xml.dom import ValidationErr
from django.core.exceptions import ValidationError

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def render_markdown_to_html(markdown_content):
    return markdown2.markdown(markdown_content)  # Convierte Markdown a HTML


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    entry_list = list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))
    
    return entry_list


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it won't let you save it.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        raise ValidationError("This entry already exists.")
    else:
        default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
    
