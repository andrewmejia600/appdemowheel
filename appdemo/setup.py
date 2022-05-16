import setuptools

with open("README.md", "r") as fh: 
    long_description = fh.read()

setuptools.setup(
    name="appfunctionlibrary", 
    version = "0.0.1", 
    author= "Andrew Mejia", 
    author_email= "mejiaa@smu.edu", 
    long_description= long_description, 
    long_description_content_type="text/markdown", 
    packages=setuptools.find_packages(), 
    include_package_data=True, 
    classifiers=[
        "Prgramming Language :: Python ::3", 
        "License :: OSI Approved :: MIT License",
        "Operating SYstem :: OS Independent",
    ],
    python_requires=">=3.5"

    )
