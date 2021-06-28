class: impact

# Yet Another Quiz

---

### Which one of these returns the average age for all adult men in the titanic dataset

#### 1


```python
df[(df["Sex"] == 'male') & (df["Age"] > 18)]['Age'].mean()
```
#### 2


```python
df[df["Sex"] == 'male' & df["Age"] > 18]['Age'].mean()
```


#### 3


```python
df[(df["Sex"] == 'male') & (df["Age"] > 18)]['Age'].mean.plot()
```

#### 4


```python
df[(df("Sex") is 'male'df("Age") > 18)].Age.mean()
```
---

