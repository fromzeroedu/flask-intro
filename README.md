### Step #18

Replacing cookies with sessions. Show cookies in Chrome inspector. Sessions are more secure.

To generate a good session, you need a good app secret. Here's a good way to generate it:

```python
>>> import os
>>> os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
```
