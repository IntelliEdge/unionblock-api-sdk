from setuptools import setup, find_packages

version = '1.0.0'
setup(
    name='unionblock-sdk',
    version=version,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Milivoj Bozic',
    author_email='milivoj.bozic@unionblock.com',
    maintainer='Milivoj Bozic',
    maintainer_email='milivoj.bozic@unionblock.com',
    url='https://github.com/unionblock/unionblock-sdk',
)

