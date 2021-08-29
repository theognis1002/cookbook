### Config

1. Edit git credentials in `~/.gitconfig`
    - `git config --global user.name "theognis1002"`
    - `git config --global user.email "theognis1002@gmail.com`

### Fetch

1. `git fetch --prune`
    - Marks branches as 'gone' locally that were removed remotely
    - Can set in config by doing `git config --global fetch.prune true`
1. `git fetch -p && for branch in $(git branch -vv | grep ': gone]' | awk '{print $1}'); do git branch -D $branch; done`
    - Does above + removes branches locally

### Rebase

1. Checkout to new branch that will be placed/configured onto the target branch
    - `git checkout <new_branch>`
1. Rebase in interactive mode to target branch (typically master branch)
    - `git rebase -i origin/master`
    - `pick`, `squash`, `amend`, `fix`

### Reset

1. `git reset --soft HEAD~1`
    - undo last commit but keep changes in staging
1. `git reset --soft HEAD~^`
    - undo last commit but keep changes in staging
1. `git reset --hard HEAD~2`
    - undo commit and discard changes for 2 previous commits
1. `git update-ref -d HEAD`
    - reset everything including initial commit
1. `git reset <commit_id>`
    - reset specific commit by id#
1. `git reset <file>`
    - unstages the file, but preserves the file contents.

### Squash

1. `git reset --soft HEAD~5`
    - last 5 commits
1. `git add .`
1. `git commit -m "Update"`
1. `git push -f`

### Stash

1. `git stash`
1. `git stash list`
1. `git stash apply <stash #>`
1. `git stash drop <stash #>`
1. `git stash clear`

### Undo Merge

1. Checkout to the master branch: `$ git checkout master`
1. Run git log and get the id of the merge commit: `$ git log --oneline`
1. Revert merge by commit id: `$ git revert -m 1 <merge-commit-id>`
1. Commit the revert and push changes to the remote repo.

### Credentials

1. `git config --global user.name <username>`
1. `git config --global user.email <email>`

### Miscellanous

1. `git reflog`
    - Reference log
1. `git branch -m <new_branch_name>`
    - Rename current branch
1. `git diff [source branch] [target branch]`
    - Preview changes before merging
