from enum import StrEnum

class TextUtil:
    class TEXT_COLOR(StrEnum):
        Red = '\033[91m'
        Green = '\033[92m'
        Blue = '\033[94m'
        Cyan = '\033[96m'
        White = '\033[97m'
        Yellow = '\033[93m'
        Magenta = '\033[95m'
        Grey = '\033[90m'
        Black = '\033[90m'
        Default = '\033[99m'
    @staticmethod
    def dedent(s):
        # textwrap dedent is not working with this. It uses the first line to understand the number of indents.
        # import textwrap
        # return textwrap.dedent(s)
        return '\n'.join([line.lstrip() for line in s.split('\n')])

    @staticmethod
    def get_colored_text(text: str, color: TEXT_COLOR):
        reset = '\033[0m'
        return color + text + reset
    
def cast(s: str, type_cast, default=None, supress_error:bool=True):
    try:
        return type_cast(s)
    except ValueError as e:
        if supress_error:
            return default
        raise e
    
def get_safe_filename(filename: str, timed:bool=False, extension:str|None=None):
    import time
    keepcharacters = (' ','.','_', '-')
    filename = "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()
    if timed:
        filename += f"_{int(time.time())}"
    if extension is not None:
        extension = "".join(c for c in extension if c.isalnum() or c in keepcharacters).rstrip()
        filename += f".{extension}"
    return filename