Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #upper
>>> #lower
>>> #captilize
>>> #title
>>> a="python"
>>> a.lower()
'python'
>>> a.upper
<built-in method upper of str object at 0x0000022C6F6FE940>
>>> b="HELLO"
>>> b.lower()
'hello'
>>> b="hello"
>>> b.upper()
'HELLO'
>>> c="python"
>>> c.captilize()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
>>> c="python"
>>> c.capitalize()
'Python'
>>> d="i am in class"
>>> d.title()
'I Am In Class'
