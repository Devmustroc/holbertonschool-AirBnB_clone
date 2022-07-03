![Logo](https://github.com/Devmustroc/holbertonschool-AirBnB_clone/raw/main/files/logo_HBNB.png)

# Airbnb Clone - The Console

**Airbnb** is an online platform that connects people who have a home to offer, with people who need a place to stay temporarily.

## Objectives

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is \*args and how to use it
- What is \*\*kwargs and how to use it
- How to handle named arguments in a function

![Logo](https://github.com/Devmustroc/holbertonschool-AirBnB_clone/raw/main/files/Based_Project.png)

### `models/` directory contains classes used for this project:

[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived

- `def __init__(self, *args, **kwargs)` - Initialization of the base model
- `def __str__(self)` - String representation of the BaseModel class
- `def save(self)` - Updates the attribute `updated_at` with the current datetime
- `def to_dict(self)` - returns a dictionary containing all keys/values of the instance## File Description

| Command       | Description                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `EOF`         | exits console                                                                                                            |
| `quit`        | exits console                                                                                                            |
| `<emptyline>` | overwrites default emptyline method and does nothing                                                                     |
| `create`      | Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id                                      |
| `destroy`     | Deletes an instance based on the class name and id (save the change into the JSON file).                                 |
| `show`        | Prints the string representation of an instance based on the class name and id.                                          |
| `update`      | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). |

### Classes inherited from Base Model:

- [amenity.py](/models/amenity.py)
- [city.py](/models/city.py)
- [place.py](/models/place.py)
- [review.py](/models/review.py)
- [state.py](/models/state.py)
- [user.py](/models/user.py)

#### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`.
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- Files must be executable.
- The length of your files will be tested using `wc`.

## More Info

### Execution

## Run Locally

Clone the project

```bash
  $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

Running also in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Authors

- [@Mustapha Abourar](https://github.com/Devmustroc)

#### TECH used

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/p?style=plastic)
