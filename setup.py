from setuptools import find_packages, setup

with open("app/README.md", 'r') as f:
    long_description = f.read()

setup(
    name="mario_utils",
    version="0.0.1",
    description="Utils library for DB connection and logging",
    packages=find_packages(),
    package_data={'app':['databasemanagement/*'],'app':['logger/*']},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="NA",
    author="Mario Hernandez",
    author_email="mariohertu@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved : MIT License",
        "Programming Language :: Python :: 3.10.12",
        "Operating System :: OS Independent" 
    ],
    install_requires=["pymssql >= 2.2.11","sqlalchemy >= 2.0.25"],
    extras_require={
        "dev": ["pytest>=8.0.0"]
    },
    python_requires=">=3.10.12",
    include_dirs=True
)