```python
import re
s  = 'a string about something'
```


```python
print(re.findall('\s([s]\w*)', s)[:])
```

    ['string', 'something']



```python
print(re.findall('\s([\S]\w+)', s)[:])
```

    ['string', 'about', 'something']



```python
print(re.findall('\s[s]\w*', s)[:])
```

    [' string', ' something']



```python
print(re.findall('\s([s].*)', s)[:])
```

    ['string about something']



```python

```
