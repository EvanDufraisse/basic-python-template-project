# How to create a new project

remove ".git" folder

```bash
rm -rf .git
```

run `python set_new_project.py` and answer the instructions.

# How to use conversion of jupyter notebooks for the project

Jupyter notebooks are a pain with git. The script convert_jupyter.py will duplicate and remove all cells outputs of jupyter notebooks to make versionable.

- You need to install pandoc
- You need to install nbconvert
