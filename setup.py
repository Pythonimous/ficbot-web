from setuptools import find_packages, setup

setup(
    name='ficbotweb',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'ficbot @ git+https://github.com/Pythonimous/ficbot.git@main',
    ],
)
