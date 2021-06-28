class: impact

# Really Enjoyable Quiz

---

Which one of these examples will return all of the words beginning with 's' and containing 'ing':

e.g. `['seeing', 'sprawling', 'settling', 'settling', 'singing', 'sing']`

.col-6[
#### 1
```python
import re

with open('prufrock.txt', 'r') as f:
    text = f.read()
    
ing = re.compile('\s.*ing')
ing.findall(text)
```

#### 2
```python
import re

with open('prufrock.txt', 'r') as f:
    text = f.read()
    
ing = re.compile('[s]\S*ing')

ing.findall(text)
```

]

.col-6[
#### 3
```python
import re

with open('prufrock.txt', 'r') as f:
    text = f.readlines()
    
ing = re.compile('.*ing')
ing.findall(text)
```

#### 4
```python
import re

with open('prufrock.txt', 'r') as f:
    text = f.read()
    
ing = re.compile('[s].ing')
ing.findall(text)
```
]



---

### What does this code do?


.col-6[
```python
sentences =  ['After the sunsets ...', 
              'After the novels, ...']

vowels = 'aeiou'
d = {}

for s in sentences:
    for w in s.split():
        if w[0] in vowels:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
```
]

.col-6[
#### 1

Create a frequency distribution of vowels.

#### 2
Create a frequency distribution of words beginning with a vowel for all sentences.

#### 3

Create a frequency distribution of words with multiple vowels.

#### 4

Create a frequency distribution of words beginning with a vowel for each sentence.

]
