# RCS-Calculator
This is a Python script to calculate radar cross section.

## Requirements

- python 3.8

## Getting Start

usage: main.py [-u] [--path] [--Ei] [--theta] [--phi] [--R]

*optional arguments*:

``-u, --unit``    The unit of angle, eg. degree, radian

``--path -p ``    Path to E-field.txt's folder

``--Ei -E``    Mode of incident electric field

``--theta -t``    Incidence theta angle

``--phi -p``    Incidence theta angle

``--R -R``    The distance between the far field point and the target

example:

```
python main.py -E 1 -theta 0 -phi 0 -R 1
```

## Contributors

- Zhang Yezheng
- Li Zhiwei
- Wei Yifan
- Chen Shuaifan
