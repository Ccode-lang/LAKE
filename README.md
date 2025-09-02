# LAKE `Letter Alphabet Key Encryption`  
Symmetric encryption for letters.
## Howto
To import, use `import LAKE` when the LAKE.py file is in your scripts directory.  
To encrypt use `LAKE.encrypt(<plaintext>, <letterkey>)`, example:  
```python
import LAKE
# prints fnpjx
print(LAKE.encrypt("hello", "key"))
```
To decrypt use `LAKE.decrypt(<cyphertext>, <letterkey>)`, example:
```python
import LAKE
#prints hello
print(LAKE.decrypt("fnpjx", "key"))
```
