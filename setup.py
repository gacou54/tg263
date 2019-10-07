import subprocess

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

TG263_FLAKE8_COMMAND = ['./venv/bin/flake8', 'tg263']
TESTS_FLAKE8_COMMAND = ['./venv/bin/flake8', '--ignore=E501', 'tests']
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
        _run_command(TG263_FLAKE8_COMMAND)
        _run_command(TESTS_FLAKE8_COMMAND)
        _run_command(MYPY_COMMAND)


class AllTests(TestCommand):
    description = 'run tests and linters'
    user_options = []

    def run_tests(self):
        _run_command(TESTS_COMMAND)
        _run_command(TG263_FLAKE8_COMMAND)
        _run_command(TESTS_FLAKE8_COMMAND)
        _run_command(MYPY_COMMAND)


with open('./README.md', 'r') as file_handler:
    long_description = file_handler.read()


setup(
    name='tg263',
    version='0.1.0',
    packages=find_packages(),
    url='https://gitlab.physmed.chudequebec.ca/gacou54/tg263',
    license='MIT',
    author='Gabriel Couture',
    author_email='gabriel.couture.4@ulaval.ca',
    description='TG263 implementation',
    cmdclass={
        'lint': LintTests,
        'unit': Tests,
        'test': AllTests
    },

)
