from setuptools import setup, find_packages

setup(
    name='moodfetch',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psutil>=5.9.0',
    ],
    entry_points={
        'console_scripts': [
            'moodfetch=moodfetch.__main__:main',
        ],
    },
    author='Seraphina',
    description='A quirky system monitoring tool that displays system mood',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sudo-seraphina/moodfetch',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)
