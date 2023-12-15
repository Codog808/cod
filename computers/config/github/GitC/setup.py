from setuptools import setup, find_packages

setup(
    name="GitC",
    version="0.1",
    packages=find_packages(),
    package_data={
        'GitC': ['git_commands.json'],
    },
)

