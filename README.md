<h1 align="center">iphub - IPhub.info API wrapper.</h1>

<br>

<h1 align="center"> -How to use?- </h1>

```python
import iphub

s = iphub.getSession('login', 'password') #Authirization
key = iphub.generateKey(s) #Generate/Get key
iphub.setKey(key) #Set key for use
print(iphub.checkIP(s, '127.0.0.1')) #Check ip and print result (note: Auto regenerate key if expired)
```