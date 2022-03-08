## Overview

This Flask application contains the basic  get and port demonstration with pytest for testing the code.

## App structure


```
http_app/app.py
tests/test_get_post.py
README
requirement.txt
```

## Installation
Install the python packages specified in requirements.txt:

```
$ pips install -r requirements.txt
```

## Run 

```
$ python3 http_app/app.py
```
# Debug mode
```
$ python3 http_app/app.py -d
$ python3 http_app/app.py --debug
```
Sample log
```
2022-03-08 16:13:59,125  Request-URI: /testpath
2022-03-08 16:14:03,919  Request-URI: /
```

## pytest

```
$ pytest
# for code coverage
$ python3 -m pytest --cov-report term-missing --cov=.
```
