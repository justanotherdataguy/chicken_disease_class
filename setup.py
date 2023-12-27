import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "chicken_disease_class"
AUTHOR_USER_NAME = 'nitish'
SRC_REPO = 'cnnclassifier'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description='A chicken disease classifier app',
    url='https://github.com/justanotherdataguy/chicken_disease_class',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)