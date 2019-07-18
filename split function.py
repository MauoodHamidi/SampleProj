x='Python is a open source language'
print(x)
words=x.split()
for w in words:
    print(w)
y='Python@is@a@open@source@language'
print(y)
res=y.split('@')
for q in res:
    print(q.lower(),q.upper(),len(q))
