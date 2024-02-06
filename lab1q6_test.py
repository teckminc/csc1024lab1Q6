import lab1q6
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('116.8\n5\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q6.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{27.24}') != -1


