from setuptools import setup, find_packages
def get_requirements(file_path:str)->List[str]:
    get_requirements=[]
    with open(file_path) as file_obj:
        get_requirements=file_obj.readlines()
        get_requirements=[req.replace("\n","") for req in get_requirements]
        if '-e .' in get_requirements:
            get_requirements.remove('-e .')
    return get_requirements
    

setup(    name='mlproject',
    version='0.1.0',
    author='Armaan Makkar',
    author_email="armaanmakkar416@gmail.com", 
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
