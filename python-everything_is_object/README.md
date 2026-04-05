# Python - Everything is object

## Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let's pause and look a little bit closer at how Python works with different types of objects.

In Python, the behavior of variables depends on whether the object they refer to is **mutable** or **immutable**. 

### Examples:

**Immutable (Integers)**
```python
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
```

**Mutable (Lists)**
```python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
```

This project explores these specificities, focusing on how Python handles assignments, aliases, and object identities.

## Resources
Read or watch:
* [9.10. Objects and values](https://intranet.hbtn.io/rltoken/Uv9bi_pY3p_S8n_BHv_3Zg)
* [9.11. Aliasing](https://intranet.hbtn.io/rltoken/ba_tI76_Z8Zl_8l_8B_l_g)
* [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/v_8_l_8_l_8_l_8_l_8)
* [Mutation](https://intranet.hbtn.io/rltoken/v_8_l_8_l_8_l_8_l_8) (Only this chapter)
* [9.12. Cloning lists](https://intranet.hbtn.io/rltoken/v_8_l_8_l_8_l_8_l_8)
* [Python tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/v_8_l_8_l_8_l_8_l_8)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (memory address in CPython)
* What is mutable and immutable
* Built-in mutable types (list, dict, set, etc.)
* Built-in immutable types (int, float, bool, str, tuple, etc.)
* How Python passes variables to functions

## Requirements
### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file at the root of the project folder is mandatory
* Code should use `pycodestyle` (version 2.7.*)
* All files must be executable

### .txt Answer Files
* Only one line
* No Shebang (`#!`)
* All files should end with a new line
