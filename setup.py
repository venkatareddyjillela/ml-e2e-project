
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """Reads the requirements.txt file and returns a list of requirements"""
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]

    return requirements
    
setup(
    name='mlproject',
    version='0.1.0',
    author= 'venkatareddy',
    author_email= 'venkatareddyjillela47842@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)
