from setuptools import setup, find_packages


with open('readme.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requires = f.read()
    requires = requires.split('\n')

setup(
    name='pyndustry',
    version='0.1',
    author='Nawot',
    author_email='Nawot001@gmail.com',
    description='description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Nawot/pyndustry',
    keywords = ['mindustry'],
    install_requires=requires,
    project_urls={
        'Bug Tracker': 'https://github.com/Nawot/pyndustry/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    package_dir={'': 'pyndustry'},
    packages=find_packages(where='pyndustry'),
    python_requires='>=3.6',
)