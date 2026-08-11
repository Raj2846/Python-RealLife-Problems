"""
| Symbol | Meaning                    | Example              |      |      |
| ------ | -------------------------- | -------------------- | ---- | ---- |
| `.`    | Any single character       | `c.t` → cat, cot     |      |      |
| `*`    | 0 or more                  | `ab*` → a, ab, abb   |      |      |
| `+`    | 1 or more                  | `ab+` → ab, abb      |      |      |
| `?`    | 0 or 1 / optional          | `colou?r`            |      |      |
| `[]`   | One character from choices | `[abc]`              |      |      |
| `^`    | Start of string            | `^Hello`             |      |      |
| `$`    | End of string              | `world$`             |      |      |
| `\d`   | A digit                    | `\d` → 0–9           |      |      |
| `\w`   | Word character             | letters, digits, `_` |      |      |
| `\s`   | Whitespace                 | space, tab           |      |      |
| `()`   | Group/capture              | `(abc)`              |      |      |
| `      | `                          | OR                   | `cat | dog` |


^[bh][aiu]t$

of ^ is for start of the string
[bh] string should start with b or h
[aiu] after than either a,i or u
then followed by t
$ for end of the string 
"""


import re



