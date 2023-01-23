# Eric/a Seyden's Python Homework
## for University of Montana's CSCI 151

### Book

[Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/home/)

By Robert Sedgewick, Kevin Wayne, and Robert Dondero

### Unit Testing

### Program Layout

To facilitate unit testing all programs use this pattern:
```python
import stdio


def main():
    stdio.writeln('Hello, World')

if __name__ == '__main__':
    main()
```
This allows the content to be called programmatically
and  respond on the command line in the same way
as the book examples.

#### Visual Studio Code Testing

.vscode/settings.json
```json
{
  "python.testing.unittestArgs": ["-v", "-s", "./tests", "-p", "test_*.py"],
  "python.testing.pytestEnabled": false,
  "python.testing.unittestEnabled": true,
  "python.envFile": "${workspaceFolder}/.env"
}
```

.env
```ini
PYTHONPATH=src
```

#### Testing just works in PyCharm

[Check out JetBrain's Free Education Licenses](https://www.jetbrains.com/community/education/#students)

#### Development Note
I learned the hard way
you can't name your test package folders
the same thing as your code package folders.
It just looks in the first matching package
folder it finds rather than merging.

