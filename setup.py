from setuptools import setup

setup(
    name='commander',
    version='0.1.0-pre-release',
    description='Map command line arguments to method/class methods',
    scripts=[],
    url='',
    author='Ram',
    author_email='heath.raman@gmail.com',
    license='MIT',
    install_requires=[
        "patterns@git+https://github.com/raman4793/patterns.git@develop#egg=patterns"
    ],
    packages=['commander'],
    package_data={},
    zip_safe=False
)
