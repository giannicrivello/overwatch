# overwatch
A dev build server that monitors file changes in a specifed directory, changes your Makefile and runs make to keep dependancies in sync.

Built for the use of using with a Java project but will work great with C/C++ project or any project using make and need some automation.

## TODO:
- [] Clean up the CLI (ideally the command should be:
```
overwatch <path> <dest> 
```
- [] The installer NEEDS to be easier (it needs to just work)
- [] Make will run for every change to the **file system**, ideally I would like it to run only when the file's contents has been changed (hashing?)
- [] I might take out the "pretty output" dependency (it's really just useless)

## CURRENT WORKFLOW:
before cloning, make sure you are in the directory where your source files are (currently overwatch only looks in the top directory for source files)
- [] change this to be able to feed overwatch a source_path

clone into /src:
```
git clone <this_repo>
```

run:
```
<this_repo>/src/overwatch.py
```
