# MemoryUnits

[![codecov](https://codecov.io/gh/mbhall88/MemoryUnits/branch/master/graph/badge.svg)](https://codecov.io/gh/mbhall88/MemoryUnits)
![GitHub](https://img.shields.io/github/license/mbhall88/MemoryUnits)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Build status](https://github.com/mbhall88/MemoryUnits/workflows/Python%20package/badge.svg)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/mbhall88/MemoryUnits/Python_package)](https://github.com/mbhall88/MemoryUnits/actions)

Python objects for working with memory units, file sizes, or even genome sizes.


[TOC]:#

# Table of Contents
- [Install](#install)
- [Usage](#usage)
  - [`Unit`](#unit)
  - [`Memory`](#memory)
- [Contributing](#contributing)
  - [Set up](#set-up)
  - [Tests](#tests)
  - [Linting](#linting)
  - [Formatting](#formatting)


## Install

This library is intended to be "headerless". That is, just copy and paste the code (and
test) into your project.  
No need to `pip install` anything.  
The only dependency is `pytest` if you include the test code in your project. The actual
library code requires no dependencies outside the Python standard library.

## Usage

Working with memory and file sizes becomes a little more elegant.

There are two main classes in this library: `Unit` and `Memory`

### `Unit`

`Unit` is the class is used for scaling your memory value. The units are the same as
[metric prefixes][metric] and go from Kilo up to Zetta (with Bytes as the base).

They can be constructed in two different ways or you can directly use one as the class
is just an [`Enum`][enum].

```python
from memory_units import Unit

# use directly
unit = Unit.KILO

# construct from a variety of strings
suffixes = ["MB", "M", "m", "mb", "Mb"]
for s in suffixes:
    unit = Unit.from_suffix(s)
    assert unit == Unit.MEGA
    
# construct from a power order
power = 3
unit = Unit.from_power(power)
assert unit == Unit.GIGA

# get the suffix and power easily
assert unit.suffix == "GB"
assert unit.power == 3
```

### `Memory`

This is the main attraction.

You can construct a `Memory` object in a couple of ways.

```python
from memory_units import Unit, Memory, InvalidMemoryString

# default construction specifying the value and unit
mem = Memory(20, Unit.TERA)
# empty initialisation is one byte
mem = Memory()
assert mem.bytes() == 1

# or you can construct one from a string
mem = Memory.from_str("12KB")
# the string can be formatted in many ways
strings = ["500MB", "500.0MB", "500M", "500mb", "500 mB"]
expected = Memory(500, Unit.MEGA)

for s in strings:
    actual = Memory.from_str(s)
    assert actual == expected
    
# if you try to initialise from a bad string, you will get an `InvalidMemoryString` exception.
s = "60LB"
try:
    mem = Memory.from_str(s)
except InvalidMemoryString as err:
    print(err)
# 60LB is an invalid memory string.
```

In the above examples you might have noticed that we used the equality operator (`==`)
to compare two `Memory` objects. The equality operator actually works by comparing the
number of bytes, rather than the value and unit. So, if I want to see if two memory
variables are the same, but they have different units. No problem!

```python
from memory_units import Unit, Memory

mem1 = Memory(500, Unit.MEGA)
mem2 = Memory(0.5, Unit.GIGA)

assert mem1 == mem2
```

Converting between different units is a pretty common need. Let's say we want to convert
50 kilobytes into megabytes.

```python
from memory_units import Unit, Memory

mem = Memory(2_500, Unit.KILO)
desired_units = Unit.MEGA

actual = mem.to(desired_units)
expected = Memory(2.5, desired_units)

assert actual == expected
```

Or we just want plain ol' bytes.

```python
from memory_units import Unit, Memory

mem = Memory(40, Unit.GIGA)

actual = mem.bytes()
expected = 40_000_000_000

assert actual == expected
```

Hmmm, but we want our resulting bytes to be in binary multiples i.e. 1024 instead of
1000\.

```python
from memory_units import Unit, Memory

mem = Memory(40, Unit.KILO)

actual = mem.bytes(decimal_multiples=False)
expected = 40_960

assert actual == expected
```

Want a pretty printed version of your memory?

```python
from memory_units import Unit, Memory

mem = Memory(50, Unit.KILO)

actual = str(mem)
expected = "50KB"

assert actual == expected
```

You also have access to some basic properties on the `Memory` object.

```python
from memory_units import Unit, Memory

mem = Memory(5.6, Unit.EXA)

assert mem.power == 6
assert mem.suffix == "EB"
```

#### Bioinformatics bonus

Lastly, if you work in bioinformatics (as I do), you might find your code will look a
little more relevant if you just rename the `Memory` class.

```python
from memory_units import Unit, Memory as GenomeSize

size = GenomeSize(4.4, Unit.GIGA)

actual_bases = size.bytes()
expected_bases = 4_400_000_000
assert actual_bases == expected_bases
```

## Contributing

I am very happy to recieve pull requests!

### Set up

```shell
pip install --pre -r dev-requirements.txt
```

### Tests

Ensure tests pass before pushing anything. Also, make sure you have not reduced the
[code coverage][codecov].

```shell
pytest
# or with coverage
pytest --cov=./
```

### Linting

Please ensure there are no errors.

```shell
flake8 .
```

### Formatting

Please make sure the code is formatted with [`black`][black] before pushing it.

```shell
black .
```

<!--References-->
[metric]: https://en.wikipedia.org/wiki/Metric_prefix
[enum]: https://docs.python.org/3/library/enum.html
[codecov]: https://codecov.io/gh/mbhall88/MemoryUnits
[black]: https://github.com/psf/black

