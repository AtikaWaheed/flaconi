

# Flaconi-e2e-tests

## Pre reqs

- Python 3.6+

## Installations

1- `pip3 install -r requirements.txt`

## Running Tests

1- To run all the tests: nosetests -v

2- To run all tests in a file: nosetests tests/file_name.py -v

3- To run all tests in a class: nosetests tests/file_name.py:ClassName -v

4- To run a single test: nosetests tests/file_name.py:ClassName.test_name -v