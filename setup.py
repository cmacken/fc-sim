from setuptools import setup, find_packages

setup(
    name="fcsim",
    version="0.1.0",
    description="FCSim - Football Simulation.",
    author="Cameron Mackenzie",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
    ],
    package_data={
        'fcsim': ['data/*'],
    },
    include_package_data=True,    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.11.10",
    # entry_points={
    #     'console_scripts': [
    #         'fcdb=fcdb.interface.cli:main',  # This defines the CLI call
    #     ],
    # },
)