# my-first-app 🧮

My first learning project - Python calculator + Git practice.
Built by bouzidbouhafs while learning Git, GitHub and Python.

## What is inside?

- `app.py` - my very first Python file (Hello World)
- `calculator.py` - small calculator with 4 operations + interactive mode
- `TIPS.md` - notes about good Git habits

## Features

- Add, subtract, multiply, divide
- Safe divide by zero message
- Interactive mode (type numbers from keyboard)
- Small clean commits (v1 -> v4)

## How to run?

```bash
cd my-first-app
python3 app.py
python3 calculator.py
```

Example:
```
=== My Calculator ===
2 + 3 = 5
5 - 2 = 3
4 * 3 = 12
10 / 2 = 5.0

Enter first number: 10
Enter operation (+ - * /): +
Enter second number: 5
Result: 15.0
```

## How I built it?

1. v1 - `add()` only
2. v2 - added `subtract()`
3. v3 - added `multiply()` + `divide()` with zero check
4. v4 - added interactive menu with `input()`

Each step = one commit. Then pushed all with `git push`.

## Git commands I learned

```bash
git clone <url>
git add .
git commit -m "message"
git pull origin main
git pull --rebase origin main
git push origin main
git status
git log --oneline
```

## Author

- GitHub: [bouzidbouhafs](https://github.com/bouzidbouhafs)
- Repo: [my-first-app](https://github.com/bouzidbouhafs/my-first-app)
