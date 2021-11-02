from setuptools import setup
from pip._internal.req import parse_requirements

setup(
    name='commander',
    version='0.1.0-pre-release',
    description='Map command line arguments to method/class methods',
    scripts=[],
    url='',
    author='Ram',
    author_email='heath.raman@gmail.com',
    license='MIT',
    install_requires=[str(ir.requirement) for ir in parse_requirements("requirements.txt", session="hack")],
    packages=['commander'],
    package_data={},
    zip_safe=False
)
