Blog
https://wangonya.com/blog/publishing-package-on-test-pypi/

# install dependencies
pip install pipdeptree
pip install twine 

# build your python codebase
python setup.py sdist bdist_wheel

# publist to testpypi
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# publish to pypi
twine upload dist/*


RUNNING UNIT TESTS 

# To run unit tests - goto src directory - make sure you are in parent of tests (where all the test file resides)

Run the following command

python -m unittest discover
