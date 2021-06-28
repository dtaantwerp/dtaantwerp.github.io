class: impact 

# The Error quiz

---

### Which of these examples has the most incorrect lines.

.col-6[
#### 1
```python
from numpy import mean
mean(3,5)
print(mean)
```

#### 2
```python
from numpy import mean
mean([3,5])
print(mean)
```
]

.col-6[
#### 3
```python
import mean from numpy
m = mean([3,5])
print(m)
```

#### 4
```python
from numpy import mean
m = mean([3,5])
print(m)
```
]

---


### Which comination of errors does this code contain.

.col-12[
.col-6[
```python
import mean from numpy

np.mean([3,5])

print(mean)

string = 'hello world'
print(string[100])
```
]
]


.col-6[
#### 1
```bash
SyntaxError: invalid syntax
FunctionError: name 'np' is not defined
NameError: name 'mean' is not defined
IndexError: string index out of range
```

#### 2

```bash
ImportError: invalid syntax
NameError: name 'np' is not defined
IndexError: name 'mean' is not defined
IndexError: string index out of range
```
]
.col-6[
#### 3

```bash
SyntaxError: invalid syntax
NameError: name 'np' is not defined
IndexError: name 'mean' is not defined
IndexError: string index out of range
```

#### 4

```bash
SyntaxError: invalid syntax
NameError: name 'np' is not defined
NameError: name 'mean' is not defined
IndexError: string index out of range
```
]

