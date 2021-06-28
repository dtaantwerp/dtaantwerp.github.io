class: impact

# A tricky pandas quiz

---

## Which one of these does not equal 4?


.col-6[```python
df = pd.DataFrame({'a':[3,8],'b':[5,7]})
df
```
```bash
   a  b
0  3  5
1  8  7
```

]

.col-6[
#### 1

```python
df.loc[0].mean()
```

#### 2

```python
df.iloc[0]['a'] + 1
```

#### 3

```python
df['a'].mean()
```

#### 4

```python
df.iloc[1]['a']/2
```
]
---

## How many of these line return the string 'hello world'?

.col-6[
```python
df = pd.DataFrame({'a':['hello','world'],
                    'b':['world','hello']})
```

```bash
       a      b
0  hello  world
1  world  hello
```

#### These lines:
```python
df.iloc[0]['a'] + ' world'

df['a'].apply(lambda x: x + ' world')[0]

df['b'].str.replace('world', 'hello world')[0]

df['a'][0] + ' ' + df['a'][1]
```

]


.col-6[

#### 1
all of them
#### 2
none of them
#### 3
two of them
#### 4
one of them

]

