Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #ASCII(AMERICAN STANDARD CODE FOR INFO EXCHANGE
>>> chr(34)
'"'
>>> chr(98)
'b'
>>> chr(122)
'z'
>>> #ord
>>> ord("A")
65
>>> ord(90)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ord(90)
TypeError: ord() expected string of length 1, but int found
>>> chr("z")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    chr("z")
TypeError: 'str' object cannot be interpreted as an integer
>>> ord(90)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ord(90)
TypeError: ord() expected string of length 1, but int found
