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
First, we move to the Unit Test folder first, then run the test.

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
### run dependencies

to import more dependencies

```
 - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install pytest
```

Can simply run requirement.txt. However, this is run by the CI, so it should be clear.

### Run test



The step of the automation is from "steps" section.

```
run: |
        cd UnitTest
        pytest
```
With the code above, the build script will move to the folder UnitTest first then run "pytest" to test all the existing unit test files.

The Unit Test of the library "pytest" should has the name start with test_* or _test. In this project, *_test.py is used for unit test files.
