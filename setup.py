

from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            ##Process Each Line
            for line in lines:
                requirements = line.strip()
                # ignore empty lines and -e.
                if requirements and requirements!= '-e .':
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Bhumireddy",
    author_email="bhumireddyvamsinathreddy@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)