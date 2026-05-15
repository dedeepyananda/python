Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict update
>>> a={"year":2026,"month":"may"}
>>> a.update({"date":12})
>>> a
{'year': 2026, 'month': 'may', 'date': 12}
>>> a={"year":2026,"month":"may"}
>>> a.update({"date":12},{"time":7})
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.update({"date":12},{"time":7})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"date":12,"time":7})
>>> a
{'year': 2026, 'month': 'may', 'date': 12, 'time': 7}
>>> #------to insert element in dict we use update------
>>> #set default
>>> a={"mobileno":123456,"mail":"d@gmail.com"}
>>> a.setdefault("name","pooja")
'pooja'
>>> a
{'mobileno': 123456, 'mail': 'd@gmail.com', 'name': 'pooja'}
>>> #get
>>> a={"colour":"black";"food":"biriyani"}
SyntaxError: invalid syntax
>>> a={"colour":"black","food":"biriyani"}
>>> a
{'colour': 'black', 'food': 'biriyani'}
>>> a.get("colour")
'black'
#copy
a.copy()
{'colour': 'black', 'food': 'biriyani'}
a.pop("colour")
'black'
a={"mobileno":123456,"mail":"d@gmail.com"}
a.popitem()
('mail', 'd@gmail.com')
a
{'mobileno': 123456}
a.clear()
a
{}
a={}
a.update({"name":"pooja"})
a
{'name': 'pooja'}
a={"name":"pooja","city":"vij","name":"pooja"}
a
{'name': 'pooja', 'city': 'vij'}
a={"name":"pooja","city":"vij","name":"priya"}
a
{'name': 'priya', 'city': 'vij'}
a={"name":"pooja","city":"vij","name1":"priya"}
a
{'name': 'pooja', 'city': 'vij', 'name1': 'priya'}
#single key with number of values-------
a={"idnos":[10,20,30],"names":["pooja","priya","prasanna"],"marks":[60,70,80]}
a
{'idnos': [10, 20, 30], 'names': ['pooja', 'priya', 'prasanna'], 'marks': [60, 70, 80]}
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['pooja', 'priya', 'prasanna']), ('marks', [60, 70, 80])])
a.values()
dict_values([[10, 20, 30], ['pooja', 'priya', 'prasanna'], [60, 70, 80]])
a.keys()
dict_keys(['idnos', 'names', 'marks'])
