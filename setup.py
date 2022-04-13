from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()
    
setup(
    name='Hazzard Mouse Jiggler',
    version='0.1.0',
    description='Python based Mouse Jiggler',
    long_description=readme,
    author='Evan Hazzard',
    author_email='ewhazzard@gmail.com',
    url='https://github.com/ewhazzard/Hazzard-Mouse-Jiggler/',
    packages=find_packages(exclude=('tests', 'docs'))
)
