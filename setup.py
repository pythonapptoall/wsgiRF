from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read()

setup(
    name="wsgiRF",
    version="1.0.5",
    author="Sergey Sobakin",
    author_email="info@python.reviews",
    description="Configurable WSGI REST framework",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pythonapptoall/wsgiRF/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)