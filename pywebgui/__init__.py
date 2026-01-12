from ._pywebgui import py_create_window
from os.path import dirname, join

__version__ = "0.1.0"
__author__ = "xzp"
__description__ = "A Python library for creating desktop applications with web technologies"

__all__ = ['create_window']


def create_window(
        win_title: str = "pywebgui app",
        win_width: int = 1200,
        win_height: int = 800,
        win_content: str = None,
        win_icon_path: str = None,
        win_is_decorations: bool = True,
        win_is_resizable: bool = True,
        win_is_devtools: bool = True
):
    if not win_content:
        win_content = join(dirname(__file__), 'statics', 'default_html.html')

    if not win_icon_path:
        win_icon_path = join(dirname(__file__), 'statics', 'default_icon.png')

    py_create_window(
        win_title,
        win_width,
        win_height,
        win_content,
        win_icon_path,
        win_is_decorations,
        win_is_resizable,
        win_is_devtools
    )
