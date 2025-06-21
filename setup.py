'''
 Thet setup.py file is an essentail part of packaging and distribution python projects.
 It is used by setuptools
 to define configure of our project such as metadata,dependencies and more
 '''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this funcation is help to return requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read line from the file 
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines & -e. available in requirements.txt
                if requirement and requirement !='-e .':
                        requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print('requirement.txt file not found')

    return requirement_lst

print(get_requirements())

setup(
     name='NetworkSecurity',
     version="0.0.1",
     author="Atul Yadav",
     author_email='yatul247@gmail.com',
     packages=find_packages(),
     install_requirements=get_requirements()
     )