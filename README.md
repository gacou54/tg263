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

result = tg263.is_structure_name_allowed('Prostate')
# Result is `True`
```

### Finding a structure
```python
import tg263

result = tg263.find_structure('SpinalCord_PRV12')

print(result.description)
print(result.anatomic_group)
print(result.target_type)
print(result.major_category)
print(result.minor_category)
print(result.fmaid)
```

## Acknowledgements

This work is a basic implementation of the __TG263__
(https://www.aapm.org/pubs/reports/RPT_263.pdf)

The allowed structure names (and corresponding information) were taken from
https://www.aapm.org/pubs/reports/RPT_263_Supplemental/ .

The initial allowed structure names were taken from the __ESAPIX__
project (https://github.com/rexcardan/ESAPIX), made by __Rex Cardan__.
The ESAPIX license is included in the LICENSE file.
