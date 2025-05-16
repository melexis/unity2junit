from setuptools import find_namespace_packages, setup

requires = [
]

setup(
    name='mlx.unity2junit',
    url='https://github.com/melexis/unity2junit',
    license='Apache License Version 2.0',
    author='Anton Manzhelii',
    author_email='amz@melexis.com',
    description='Python script for converting Unity test framework log file to xUnit/JUnit XML',
    long_description=open("README.rst").read(),
    long_description_content_type='text/x-rst',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_namespace_packages(where=".", exclude=("doc.*", "doc", "tests.*", "tests", "build*")),
    package_dir={"": "."},
    package_data={
    },
    include_package_data=True,
    install_requires=requires,
    python_requires='>=3.8',
    keywords=['xUnit', 'JUnit', 'XML', 'Unity test framework', 'testing'],
    entry_points={
        'console_scripts': [
            'mlx.unity2junit = mlx.unity2junit.unity2junit:main',
            'unity2junit = mlx.unity2junit.unity2junit:main',
        ]
    },
)
