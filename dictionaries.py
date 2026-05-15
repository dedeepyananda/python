Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict
a={"name":"pooja","year":2026,"month":5}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 5}
type(a)
<class 'dict'>
#diff btw set and dict
a={"name","pooja","year",2026,"month",5}
a
{'month', 'pooja', 5, 'year', 2026, 'name'}
#accessing
a["name"
  ]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a["name"
TypeError: 'set' object is not subscriptable
a["name"]
      
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a["name"]
TypeError: 'set' object is not subscriptable
>>> b={"name":"pooja","year":2026,"month":5}
...       
>>> print(b)
...       
{'name': 'pooja', 'year': 2026, 'month': 5}
>>> type(b)
...       
<class 'dict'>
>>> b["name"]
...       
'pooja'
>>> b[2026]
...       
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b[2026]
KeyError: 2026
>>> b.keys()
...       
dict_keys(['name', 'year', 'month'])
>>> b.values()
...       
dict_values(['pooja', 2026, 5])
>>> b.items()
...       
dict_items([('name', 'pooja'), ('year', 2026), ('month', 5)])
