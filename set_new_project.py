#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 

@Author: Evan Dufraisse
@Date: Tue May 30 2023
@Contact: e[dot]dufraisse[at]gmail[dot]com
@License: MIT License
"""
import os



default_string_readme = """
# PROJECT_NAME - SHORT_DESCRIPTION

DESCRIPTION

## Installation

Create an environment with the following command:

```bash
conda create -n <name_of_your_choice> python=3.10 %version of python you want to use
```
Then activate
```bash
conda activate <name_of_your_choice>
```

Then install the package with the following command in the root folder of the project:

```bash
pip install -e ./
# -e stems for editable, meaning that you can modify the code and the changes will be taken into account dynamically
```

## Usage

#### CLI usage

```bash
python ./src/name_of_package/main.py "John Doe"
```
prints "Hello John Doe!"

#### Python usage

```python
import name_of_package
# or
from name_of_package.backend.hello import print_hello_name

## Miscellaneous

This repo also contains a handy script to convert jupyter notebooks to easy versionnable versions.
Jupyter notebooks are a pain with git. The script convert_jupyter.py will duplicate and remove all cells outputs of jupyter notebooks to make them versionable.

- You need to install pandoc
- You need to install nbconvert
"""

if __name__ == "__main__":
    root_folder_of_project = os.path.abspath(os.path.dirname(__file__))
    print("Root folder of project: {}".format(root_folder_of_project))

    # Ask name of the package
    package_name = input("Name of the package (the thing you'll be importing, i.e. 'import numpy'): ")
    print("Package name: {}".format(package_name))

    # Ask for name of the project
    project_name = input("Name of the project: ")
    print("Project name: {}".format(project_name))

    # Ask for description
    description = input("Description of your project: ")
    print("Description: {}".format(description))

    # Ask name
    name = input("Your name (i.e. John Doe): ")
    print("Name: {}".format(name))

    # Ask mail
    mail = input("Your mail: ")
    print("Mail: {}".format(mail))

    # Ask for python version
    python_version = input("Min python version (default: 3.8): ")
    if python_version == "":
        python_version = "3.8"

    # Ask for packages:
    packages = input("Packages you know you'll need (separated by ','): ")
    packages = packages.split(",")
    packages = [package.strip() for package in packages]

    # file = "setup.py"
    file = "pyproject.toml"
    with open(os.path.join(root_folder_of_project, file), "r") as f:
        setup_file = f.read()

    with open(os.path.join(root_folder_of_project, "src", "PACKAGE", "main.py"), "r") as f:
        main_file = f.read()
    main_file = main_file.replace("PACKAGE", package_name)

    with open(os.path.join(root_folder_of_project, "src", "PACKAGE", "main.py"), "w") as f:
        f.write(main_file)
    
    os.rename(os.path.join(root_folder_of_project, "src", "PACKAGE"), os.path.join(root_folder_of_project, "src", package_name))

    setup_file = setup_file.replace("PACKAGE_NAME", package_name)
    setup_file = setup_file.replace("PROJECT_NAME", project_name)
    setup_file = setup_file.replace("DESCRIPTION", description)
    setup_file = setup_file.replace("FIRST_LAST_AUTHOR", name)
    setup_file = setup_file.replace("CONTACT_MAIL", mail)
    setup_file = setup_file.replace("PYTHON_VERSION", python_version)
    default_packages = ['"tqdm"', '"loguru"', '"ipykernel"']
    set_already_added_packages = set([elem.strip('"') for elem in default_packages])
    packages_str = ",\n    ".join(default_packages)
    packages_str = "\n    " + packages_str

    for pkg in packages:
        if pkg not in set_already_added_packages:
            packages_str += ',\n    "{}"'.format(pkg)
            set_already_added_packages.add(pkg)
    packages_str += "\n"

    setup_file = setup_file.replace("PACKAGES", packages_str)

    with open(os.path.join(root_folder_of_project, file), "w") as f:
        f.write(setup_file)

    # with open(os.path.join(root_folder_of_project, "README.md"), "r") as f:
    #     readme_file = f.read()
    readme_file = default_string_readme
    readme_file = readme_file.replace("PROJECT_NAME", project_name)
    readme_file = readme_file.replace("DESCRIPTION", description)
    readme_file = readme_file.replace("name_of_package", package_name)

    with open(os.path.join(root_folder_of_project, "README.md"), "w") as f:
        f.write(readme_file)

    # Init git

    print("Initializing git...")
    os.system("git init")
    os.system("git add *")
    os.system('git commit -m "Initial commit"')
