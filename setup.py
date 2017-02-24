from setuptools import setup, find_packages

from balloons import __version__

setup(
    name='lift-balloons',
    version=__version__,
    description='A collection of helpful Django template tools for front-enders.',
    long_description=open('README.rst').read(),
    author='Lift Interactive',
    author_email='dev+pypi@liftinteractive.com',
    url='https://github.com/l1f7/lift-balloons',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    )
)
