from io import StringIO
from contextlib import redirect_stdout
from hello import say_hello

def test_prints_hello_10_times():
    buf = StringIO()
    with redirect_stdout(buf):
        say_hello(10)
    lines = [ln for ln in buf.getvalue().splitlines() if ln.strip()]
    assert lines == ["Hello"] * 10
