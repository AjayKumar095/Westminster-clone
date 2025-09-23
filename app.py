from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

code = '''def greet(name):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, world!")

    '''

print(highlight(code, PythonLexer(), TerminalFormatter()))
