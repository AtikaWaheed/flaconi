

# Flaconi-e2e-tests

Pre reqs:

1- Install chrome and chrome driver.

2- Install python `brew install python3` (pip3 will already installed)

2- Install selenium `pip3 install selenium`

Running Tests
1- To run all the tests: nosetests -v

2- To run all tests in a file: nosetests test_cases/file_name.py -v

3- To run all tests in a class: nosetests test_cases/file_name.py:ClassName -v

4- To run a single test: nosetests test_cases/file_name.py:ClassName.test_name -v