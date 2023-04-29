from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='iphub',
    version='1.0.2',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='IPhub.info API wrapper.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/iphub',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/iphub/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=['iphub'],
    include_package_data = True,
    install_requires = ['requests'],
    python_requires='>=3.6'
)