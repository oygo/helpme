---
title: and Github 
nav_order: Git 
---

# Git and Github 

{: .no_toc } 
<details open markdown="block"> 
  <summary> 
    Table of contents 
  </summary> 
  {: .text-delta } 
1. TOC 
{:toc} 
</details> 

## Resources:
- Coursera Git/Github course: https://www.coursera.org/learn/introduction-git-github
- Git book: https://git-scm.com/book/en/v2
- Git tutorial: https://git-scm.com/docs/gittutorial

## Getting started: version control and Git
- The purpose of version control: to keep track of your changes
	- this also includes: keeping historical copies
	- this also means: being able to 

#### Before version control
when we call the `diff` command (which takes as parameters to files names), we get the differences between two files
- i.e. `diff file1.py file2.py`
	- we see the lines which differ: diff tells us which line numbers these are in both files, and what happened between these lines: 'c' for change, 'a' for addition
	- i.e. '5c5,6' means there was a change in line 5 in the old file, and this is now in lines 5 and 6 in the new file
- `diff -u file1.py file2.py` outputs the differences in a different format
- `diff -u file1.py file2.py > change.diff` outputs as above the differences, but now saves them in a (so-called 'patch' file)
- `patch` then applies the changes from a `diff`-file to a (code) file.
	- example: `patch file1.py < change.diff` takes the changes listed in the file `change.diff` and applies them to `file1.py`

on a sidenote:
`sys.exit` in python lets you return a code from a script (called an exit code); with this, the script could report back (i.e. to the shell) messages, such as whether it ran successfully

documentation on diff and patch:
- https://man7.org/linux/man-pages/man1/diff.1.html
- https://man7.org/linux/man-pages/man1/patch.1.html


#### Version control
A version control system keeps track of the changes we make in our files
- we can also make edits to several files, and treat that collection of edits as a single change: this is called a commit. 
- the author of a commit can also record _why_ a change was made (i.e. which bugs were fixed etc.)
- a version control makes it also very easy to roll back our code to previous versions (when errors occur)


#### Getting started with Git
- Git can work as a server, a stand-alone machine, or a client
- Two ways to start working with repositories:
	- use a new one: `git init`. This makes the current folder a respository (and adds the subfolder .git, which has all of git's 'behind-the-scenes'-files, which we'll never edit directly; it stores the changes and the change history).
	- use an existing one: `git clone`
- the current folder (i.e. the folder, which houses the .git folder) is called the 'working tree': this is where the current version of our files is. 

- to make Git track a file, we need to tell Git to start tracking it; we add it to the files that Git "watches" by using the `git add` command
	- `git add file1.py` adds file1.py to the files that git tracks.
	- the 'staging area' aka 'the index' is a file maintained by Git that contains all of the information about what files and changes are going to go *into the next commit*
- `git status` gives us information about which changes have not been committed yet. These are the changes which are in the 'staging area.'
	- how to enter the commit message in Windows: https://stackoverflow.com/questions/13239368/git-how-to-close-commit-editor

- how git operates
	- there's three areas in Git:
		- [insert the picture here]
		- git directory: contains the history of all the files and changes
		- working tree contains the current state of the project, including any changes we've made
		- staging area: changes we've marked to be included in the next commit
	- so there's three different "states" a file can be in
		- modified: we made changes, which haven't been committed yet (i.e. we've made changes to a file in a text editor)
		- staged: our modified files have become staged files. all files which are staged will be part of the next snapshot (= commit we make)
			- we stage files with `git add file1.py`
		- committed: 
			- we commit with `git commit`, specifically  `git commit -m 'Added documentation to the file'`, or whatever we want our commit message to be (if we just write `git commit` the text editor opens to type a longer commit message there)
	- so in summary: we work on modified files on our working tree. Whent they are ready, we stage these files, by adding them to the staging area. Finally, we commit the stages on the staging area, which takes a snapshot (figueratively)/adds the files to the git directory (literally)
	
- the basic git workflow:
	- generally: all the files we want to manage with git, must be part of a git repository
		- we create a new git repository with `git init`
	- we make changes to our files (with our IDE), we stage them with `git add`, and then we commit them with `git commit`
- commit messages
	- writing good and clear commit messages is important, to understand later on what changes why and when. 
	- the "standard" format for writing a good Git commit message:
		- 1-line summary of the commit (usually max. 50 characters)
		- blank line
		- full descirption of the changes: why are they necessary, what's interesting about them. (this can be a lengthy text, but usually max 72 characters per line)
		- Git commit messages can contain references/links to documentation or tickets
	- there's a git command to display commit messages: `git log` (git log does not do any line wrapping. this is why we need to do the line wrapping when writing the messages)

## Advanced Git interaction
In this section: 
- advanced Git commands
- revert previous changes
- branches: for example, this allows us to work on an experimental feature while leaving the main code intact

#### Advanced Git commands
- **Skipping the changing area:** a shortcut to stage any changes to tracked files and commit them in one step: `git commit -a`
	- the separate step between staging and committing allows us to add/combine several modified files into one commit (or alternatively leave out some changed files from the commit).
	- but if we just want to do these two steps in one (for example, when we've just made a one-file edit, or we want to commit everything we've worked on), we can use `git commit -a`
		- this only applies to tracked files
		- if the modified file has not been added to the repo, we need to add it first (so it gets tracked)
- Git uses the head alias to represent the currently checked out snapshot of your project (this becomes relevant, once we start talking about branches)
- **Getting more information about changes:** `git log -p` shows us all commits, in patch format (so it's very easy to see what was changed in each commit). This is very useful to track what happened during commits.
	- to show what changed during a specific commit use `git show {commit id}`, i.e. `git show b7d2eeb607e349c1f4a52bf80cff132692540da5` 
	- to get commit ids, use `git log`, which shows all the commits (in short format)
		- use `git log --stat` to show more information about each commit (i.e. how many lines were added in how many files during each commit)
- **showing changes which have not been staged yet (and selecting which ones to stage):** 
	- `git diff` shows changes which have not been staged
	- `git add -p` also shows changes which have not been staged, and then asks - for every file - if we want to commit this change now
	- to show the changes which have been staged, but not yet commited use `git diff --staged`
- **deleting and renaming files:**
	- `git rm file2.py` removes file2.py from the Git directory (it also deletes the file in the file system) and stages it for the next commit.
		- git commit -m 
	- `git mv file2.py file_newname.py` renames files
- the file .gitignore can be .

#### Revert changes
- undo changes before staging:
	- when a file has not staged yet, `git checkout file1.py` restores file1.py to the status from the previous commit
	- this can also be done more finely grained - change by change - with `git checkout -p file1.py` this will ask - change by change - which changes to keep and which ones to undo.
- undoing changes after staging:
	- unstage changes with `git reset` (this is the counterpart to git add * )
	- alternatively, to just remove them for one file `git restore --staged file1.py`
	- both just undo changes from staging, but the changes are still in the working bench. so, to undo them in the working bench, we still need to run the `git checkout file1.py` from above.
- amending commits (i.e. fix a commit retrospectively):
	- the `git commit` option `--amend`  just adds things to the last commit (it also allows to update/change the commit message)
	- But `git commit --amend` should not be used on commits which have already been made public (i.e. on shared repos). This is because `git commit --amend` changes the Git history and replace the last commit with the current one. When working with others, this can lead to some confusing situations.
- undoing the last commit and returning to the previous commit version:
	- say you've just made a commit (say commit 5), which had a bug. you want to return to commit 4 (the version before you introduced the bug). This can be done with `git revert`. The command `git revert` creates a new commit (i.e. commit 6), which contains the opposite of all the previous changes. I.e. it returns to the state of commit 4 (now as commit 6), by reversing all the changes that were made in commit 5. But this way, the commit history is kept clear. 
	- `git revert` reverts the last commit
- to undo any previous (given) previous commit, use `git revert {commit id}`
	- we can also revert to a further-back commit by using the commit `git revert {commit id}`. This undoes the changes of this specific commit (while leaving the changes from commits after the specified one in place).
	-  we can look up commit ids through `git log`

#### Branching and merging
- a branch represents an independent line of development in a project
	- on a technical level, a branch is a pointer to a particular commit (which represents the last commit in that development line)
	- the default branch that Git creates is called "master"; it's commonly used to represent the known 'good' state of the project
	- it's good practice to work on new features in a branch (and test it properly there), and then only merge it back into the master branch later
- how to work with branches in practice
	- create a new branch (called 'new feature'): `git branch new-feature`
	- show existing branches `git branch`
	- go to an existing branch: `git checkout {branch name}` to go to a branch (= check out the latest shapshot this branch): for example `git checkout new-feature` goes to the branch `new-feature`
		- on a side note: `git checkout` is used for both files and for branches
			- to create a new branch and use it (= check it out) immediately, we can use the shortcut `git checkout -b {branch name}` does these two in one step: it creates a new branch (called 'branch name' and switches to it)
	- to delete a branch we don't need anymore use `git branch -d new-feature` 
		- if there are changes in the branch, which haven't been merged into the master branch, Git will let us know (and give an error)
- a typical workflow is to create a new branch to develop a new feature; once the feature is in good shape, we merge it back into the master branch
	- if we're in the master branch (get there with `git checkout master`), we merge the `new-feature` branch in with `git merge new-feature`
	- there's two different kinds of merges (Git automatically picks):
		- a fast forward merge, for the situation: 'while we've been developing the branch `new-feature`, nothing has changed on the master branch'. So all Git has to do, in order to merge the `new-feature` branch into the development branch is to apply all the changes (= all the commits) to the branch 
		- a threeway merge: while we've been developing the branch `new-feature`, the `master` branch has changed as well (i.e. the master branch has had additional commits since the time we've started the `new-feature` branch). Git now has to merge the `new-feature` branch back into the now-updated `master` branch. Git tries to do this automatically
- merge conflicts:
	- merge conflicts arise when both branches have edits on the same file
	- in this case, we might have to deal with them manually
	- i.e. if we've run `git merge new-feature` (while on the master branch), and there is a merge conflict between the branches, the merge will stop, and git will tell us which files have a merge conflict, and highlight the conflicting lines/merges in all the files. We then have to go through all the files in our editor and fix the conflicts. Afterwards we type `git commit` to commit with the resolved changes.
		- we can also abort this merge with `git merge --abort`; in this case both branches revert to the pre-merge commit state (so if merging a development branch into the master, it's got to have commited the development branch on its own before, just in case something goes wrong during the merge)
- we can look at the commit history with branches: `git log --graph --oneline`


## Working with Remotes
- there are some additional changes when working with remote repositories
	- when there is an update on the master repository, git will let us know
	- then the process has the following steps
		- *fetch* remote changes from repo
		- if there are conflicts, then manually merge
		- and only then *push* our changes to the repo
- commands for syncing the local repository with github:
	- `git push` sends the local data to the server
	- `git pull` gets the updated data from the server (and automatically merges it to the current branch). `git pull` is actually a shortcut for running `git fetch`, followed by `git merge`:
		- `git fetch` gets the updated data from the server, but does not automatically merge it into our local (master) branch; we have to do this manually (using `git merge`)