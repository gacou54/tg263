# TG263

Basic TG263 implementation. This library could be used as a
structure name filter in your program. 

## Installation

```bash
$ pip install tg263
```

Or from current master branch:

```bash
$ pip install git+https://github.com/gacou54/tg263
```

## Usage

### Validating the structure name
```python
import tg263

# Result is `True`
result = tg263.is_structure_name_allowed('Prostate')
```


## Acknowledgements

The allowed structure names were taken from the __ESAPIX__
project (https://github.com/rexcardan/ESAPIX), made by __Rex Cardan__.
The ESAPIX license is included in the LICENSE file.
