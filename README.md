AutomationPractice Tests

End-to-end tests for Flaconi

Pre reqs:
1- Install chrome and chrome driver

2- Install Virtualenv `pip install virtualenv`

3- Create Virtualenv `virtualenv my_project`

4- Activate Virtualenv `source my_project/bin/activate`

5- cd into Store_Project_Selenium folder cd Store_Project_Selenium

Running Tests
1- To run all the tests: nosetests -v

2- To run all tests in a file: nosetests test_cases/file_name.py -v

3- To run all tests in a class: nosetests test_cases/file_name.py:ClassName -v

4- To run a single test: nosetests test_cases/file_name.py:ClassName.test_name -v