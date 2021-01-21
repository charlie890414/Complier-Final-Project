import subprocess

def ans(path, result1 = None):
    if not result1:
        cmd = f"./provide/smli < {path}" 
        result1 = subprocess.check_output(cmd, shell=True).decode()
    cmd = f"python3 main.py < {path}"
    result2 = subprocess.check_output(cmd, shell=True).decode()
    assert result1 == result2

def test_1_1():
    ans("hidden1/01_1_hidden.lsp", "syntax error\n")

def test_1_2():
    ans("hidden1/01_2_hidden.lsp", "syntax error\n")

def test_2_1():
    ans("hidden1/02_1_hidden.lsp")

def test_2_2():
    ans("hidden1/02_2_hidden.lsp")

def test_3_1():
    ans("hidden1/03_1_hidden.lsp")

def test_3_2():
    ans("hidden1/03_2_hidden.lsp")

def test_4_1():
    ans("hidden1/04_1_hidden.lsp")

def test_4_2():
    ans("hidden1/04_2_hidden.lsp")

def test_5_1():
    ans("hidden1/05_1_hidden.lsp")

def test_5_2():
    ans("hidden1/05_2_hidden.lsp")

def test_6_1():
    ans("hidden1/06_1_hidden.lsp")

def test_6_2():
    ans("hidden1/06_2_hidden.lsp")

def test_7_1():
    ans("hidden1/07_1_hidden.lsp", "2\n1\n")

def test_7_2():
    ans("hidden1/07_2_hidden.lsp", "0\n10\n")

def test_8_1():
    ans("hidden1/08_1_hidden.lsp", "32\n")

def test_8_2():
    ans("hidden1/08_2_hidden.lsp", "22\n")

def test_b1_1():
    ans("hidden1/b1_1_hidden.lsp", "39916800\n479001600\n6227020800\n87178291200\n1\n3\n8\n89\n10946\n")

def test_b1_2():
    ans("hidden1/b1_2_hidden.lsp", "5\n7\n55\n")

def test_b2_1():
    ans("hidden1/b2_1_hidden.lsp", "Type Error: Expect 'number' but got 'boolean'.\n")

def test_b2_2():
    ans("hidden1/b2_2_hidden.lsp", "Type Error: Expect 'number' but got 'boolean'.\n")

def test_b3_1():
    ans("hidden1/b3_1_hidden.lsp", "136\n")

def test_b3_2():
    ans("hidden1/b3_2_hidden.lsp", "5\n5\n")

def test_b4_1():
    ans("hidden1/b4_1_hidden.lsp", "15\n")

def test_b4_2():
    ans("hidden1/b4_2_hidden.lsp", "10\n")
