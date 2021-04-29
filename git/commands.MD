### Config

1. Edit git credentials in `~/.gitconfig`
    - `git config --global user.name "theognis1002"`
    - `git config --global user.email "theognis1002@gmail.com`

### Fetch

1. `git fetch --prune`
    - Removes branches locally that were removed remotely
    - Can set in config by doing `git config --global fetch.prune true`

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

### Stash

1. `git stash`
1. `git stash list`
1. `git stash apply <stash #>`
1. `git stash drop <stash #>`
1. `git stash clear`

### Miscellanous

1. `git reflog`
    - Reference log
