Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #split
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="i am learning python"
>>> b.split()
['i', 'am', 'learning', 'python']
>>> #join
>>> a="python java c c++"
>>> "".join(a)
'python java c c++'
>>> b="python java c++"
>>> "".join(b)
'python java c++'
>>> b="python","java","c++"
>>> "".join(b)
'pythonjavac++'
>>> " "join(a)
SyntaxError: invalid syntax
>>> b="python","java","c++"
>>> " ".join(b)
'python java c++'
