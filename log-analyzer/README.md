# log analyzer

Reads an ssh style log file, counts failed login attempts per ip and marks
the ones doing too many attempts. Comes with `sample_auth.log` so you can
try it immediately.

```
log file (enter = sample_auth.log):
attempts to count as suspicious (enter = 5):

4 ip(s) with failed logins:
  203.0.113.5      9 failed attempts  <-- suspicious
  192.0.2.140      7 failed attempts  <-- suspicious
  198.51.100.77    4 failed attempts
```

You can save the suspicious list to `suspicious.txt` to use somewhere else
(like a firewall block list).

This is the kind of thing a SOC analyst does all day, just usually with
fancy tools like Splunk instead of 60 lines of Python.
