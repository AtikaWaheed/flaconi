

# Flaconi-e2e-tests

Pre reqs:

- Python 3.8
- Browser Chrome
- Chrome Driver

Installations:

1- Install selenium `pip3 install selenium`

2- Install nose for execution of tests `pip3 install nose`

# Running Tests

1- To run all the tests: nosetests -v

2- To run all tests in a file: nosetests tests/file_name.py -v

3- To run all tests in a class: nosetests test_cases/file_name.py:ClassName -v

4- To run a single test: nosetests test_cases/file_name.py:ClassName.test_name -v