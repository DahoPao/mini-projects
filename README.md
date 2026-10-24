# mini-projects

Small Python tools I built while studying computer engineering and working
on my CCNA. Each one lives in its own folder with its own short readme.
Everything is pure standard library, no pip installs needed.

## The tools

| Folder | What it does |
|---|---|
| [subnet-calculator](subnet-calculator/) | type an ip like `192.168.1.10/24`, get network, broadcast, hosts etc. |
| [log-analyzer](log-analyzer/) | counts failed ssh logins per ip and flags brute force attempts |
| [password-checker](password-checker/) | scores a password 0-5 and tells you what to improve |

## Running them

Each tool runs on its own, from its folder:

```
cd subnet-calculator
python subnet_calc.py
```

## Why

Subnetting practice for the CCNA turned into "why not make the computer do
it", and that turned into a habit of writing a tool whenever I catch myself
doing the same thing by hand twice. That's the idea behind this repo.
