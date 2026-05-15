Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #fstring
>>> #format method
>>> a="motu"
>>> b="patlu"
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> print("hello {}\n hello {}".format(a,b))
hello motu
 hello patlu
>>> #fstring
...  
>>> a="chota"
>>> b="bheem"
>>> print(f"hello {a}{b}")
hello chotabheem
>>> print(f"hello {a} {b}")
hello chota bheem
>>> print(f"hello {a} hello {b}")
hello chota hello bheem
