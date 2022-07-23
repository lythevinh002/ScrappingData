# ScrappingData

Libraries

```
python -m pip install pytest
```

or

```
pip install -r requirements.txt
```

the main source is ScrappingData
and the testing source is ScrappingData/UnitTest

## Running the loginModel
```
python .\loginModel.py
```
## Running the UnitTest
First we move to Unit Test folder first, then run the test

```
cd UnitTest
```

we can run all the test by
```
pytest
```
or specific test file
```
pytest test_file_name.py
```

## Build Script

located: ScrappingData/.github/workflows/python-package.yml

the step of the automation is from "steps" section.

```
run: |
        cd UnitTest
        pytest
```
With the code above, the build script will move to folder UnitTest first then run "pytest" to test all the exist unit test files.

The Unit Test of the library "pytest" shoould has the name start with test_* or _test. In this project, *_test.py is used for unit test files.
