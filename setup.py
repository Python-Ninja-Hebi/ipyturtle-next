from setuptools import setup
# To use a consistent encoding
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

requirements = [
    'ipycanvas',
]

setup(
    name='ipyturtlenext',
    version='0.1.1',
    description='Creating Turtle Graphics in IPython/Jupyter with ipycanvas',
    long_description=long_description,
    url='https://github.com/Python-Ninja-Hebi/ipython-turtle-next',
    author='python-ninja',
    author_email='hebi@python-ninja.com',
    py_modules= [
        'ipyturtlenext',
    ],
    #packages=[
    #    'ipyturtlenext',
    #],
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords= [
       'turtle',
       'graphics',
       'ipycanvas',
       'ipywidget',
    ],
    #setup_requires=setup_requirements,
)
