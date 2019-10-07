import subprocess

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

FLAKE8_COMMAND = ['./venv/bin/flake8', '--ignore=E501', 'tg263', 'tests']
MYPY_COMMAND = ['./venv/bin/mypy', 'tg263']
TESTS_COMMAND = ['./venv/bin/python', '-m', 'unittest', 'discover', '-s', './tests/']


def _run_command(command: str) -> None:
    try:
        subprocess.check_call(command)

    except subprocess.CalledProcessError as error:
        print('Command failed with exit code', error.returncode)
        exit(error.returncode)


class Tests(TestCommand):
    description = 'run unit tests'
    user_options = []

    def run_tests(self):
        _run_command(TESTS_COMMAND)


class LintTests(TestCommand):
    description = 'run linters'
    user_options = []

    def run_tests(self):
        _run_command(FLAKE8_COMMAND)
        _run_command(MYPY_COMMAND)


class AllTests(TestCommand):
    description = 'run tests and linters'
    user_options = []

    def run_tests(self):
        _run_command(TESTS_COMMAND)
        _run_command(FLAKE8_COMMAND)
        _run_command(MYPY_COMMAND)


with open('./README.md') as file_handler:
    long_description = file_handler.read()

setup(
    name='tg263',
    version='0.1.0',
    packages=find_packages(),
    url='https://gitlab.physmed.chudequebec.ca/gacou54/tg263',
    license='MIT',
    author='Gabriel Couture',
    author_email='gacou54@gmail.com',
    description='TG263 implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    cmdclass={
        'lint': LintTests,
        'unit': Tests,
        'test': AllTests
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
