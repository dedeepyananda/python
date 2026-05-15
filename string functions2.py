Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="hello"
>>> a.islower()
True
>>> a.isupper()
False
>>> a.isdigit()
False
>>> a.isalpha()
True
>>> 
>>> b="hello world"
>>> b.isalpha()
False
>>> c="helloworld"
>>> c.isalpha()
True
>>> d=1234
>>> d.isdigit()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> d="1234"
>>> d.isdigit()
True
>>> x="nanda@1234"
>>> x.isalnum()
False
x="nanda1234"
x.isalnum()
True
