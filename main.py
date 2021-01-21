from lark import Lark
from traverse import *

with open("./grammer.lark") as f:
   grammer = f.read()
lark = Lark(grammer, start='program', parser='lalr')


lines = []
while True:
   try:
      line = input()
      lines.append(line)
   except EOFError:
      break

lisp_text = '\n'.join(lines)

try:
   tree = lark.parse(lisp_text)
except Exception as e:
   print("syntax error")
   # print(e)
   exit()

traverse(tree)