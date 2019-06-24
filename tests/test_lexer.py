import os
import pytest
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_shader import ShaderLexer

def test_highlight():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'fixtures/example.shader')
    with open(path) as f:
        code = f.read()
    path = os.path.join(dirname, 'fixtures/example.html')
    with open(path) as f:
        html = f.read()

    highlighted = highlight(code, ShaderLexer(), HtmlFormatter())
    assert highlighted == html
