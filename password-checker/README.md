# password strength checker

Scores a password 0-5 based on length, character types and whether it's in
the "most common passwords" hall of shame, then tells you what to improve.

```
password to check: hello

score: 2/5  ->  WEAK
 - longer is stronger, 12+ is a good goal
 - add an uppercase letter
 - add a number
 - add a special character like ! or #
```

Mode 2 checks a whole file of passwords at once (one per line), useful when
you want to check everything in some old list.
