# Exploring Github API
Developing various tools/apps using the Github API

## Objective List
* [x] Create a repostiory through command line
* [ ] Profile fetch using command line
* [ ] Overview generator application
* [ ] ...
## 1. Create Repository Through Command Line 

While creating a new repository there are multiple pitfalls for novice developers like problems with setting up remote connection, exporting an already existing repository to a newly created repository on Github.

In order to aid this process, the ```createRepo.py``` is a simple tool that initialises a repository both on Github and clones it into a local folder in the specified location so that one can start development in a hassle-free manner.

### Instructions
1. Clone this repository in your local system.
2. Generate a github authentication token and update the ```GITHUB_TOKEN``` in the ```createRepo.py``` file.
3. Add the path to the master directory which would contain all of your github repositories created henceforth to ```REPO_PATH``` in ```createRepo.py```. The folder structure would eventually look as follows -

```
.
├── REPO_PATH
    ├── Repository-1
    ├── Repository-2
    └── Repository-3
    ...
```
4. Add your Github username to ```GITHUB_USER``` to ```createRepo.py```

You are all setup now. Now, to create repositories from your command line simply open CMD/Terminal in the current folder and follow the syntax given below -

**For creating a public repository -**

```python3 createRepo.py --name <Name of the new repository>```

**For creating a private repository -**

```python3 createRepo.py --name <Name of the new repository> --private```

Your repository would be created after this process and you would have a local version of the repository in ```REPO_PATH/NewRepositoryName```
***