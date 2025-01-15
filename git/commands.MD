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

### Checkout

1. `git checkout -b feature/my_branch`
   - Switch to new local branch
1. `git checkout -t origin/feature/remote_branch`
   - Switch to remote branch
1. `git checkout -`
   - Switch to last checked-out branch

### Rebase

1. Checkout to new branch that will be placed/configured onto the target branch
   - `git checkout <new_branch>`
1. Rebase in interactive mode to target branch (typically main branch)
   - `git rebase -i origin/main`
   - `pick`, `squash`, `amend`, `fix`
1. Rebase specific commit range to target branch (typically main branch)
   - `git rebase -i main <commit_id>`

### Cherry Pick

1. Move specific commit onto new branch (will create assign new commit hash)
   - `git cherry-pick <commit_id>`
1. Cherry pick specific commit range to target branch
   - `git cherry-pick <start_commit_id>^..<end_commit_id>`

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

Merge:

1. `git merge --squash`
   Rebase:
1. `git rebase -i <commit|branch>`
   Manual:
1. `git reset --soft HEAD~5`
   - last 5 commits
1. `git add .`
1. `git commit -m "Update"`
1. `git push -f`

### Stash

1. `git stash`
1. `git stash list`
1. `git stash apply <stash #>` or `git stash pop <stash #>`
   - apply stash to work dir but keeps in stash
   - pop stash to work dir and remove from stash
1. `git stash drop <stash #>`
1. `git stash clear`

### Undo Merge

Method #1

1. Checkout to the main branch: `$ git checkout main`
1. Run git log and get the id of the merge commit: `$ git log --oneline`
1. Revert merge by commit id: `$ git revert -m 1 <merge-commit-id>`
1. Commit the revert and push changes to the remote repo.
   Method #2
1. `git reflog`
1. `git reset HEAD{1} --hard`

### Config/Credentials

1. `git config --global user.name <username>`
1. `git config --global user.email <email>`
1. `git config --global core.editor "vim"`
1. `git config --global credential.useHttpPath true`
   - setup credentials on a per repo basis

### Debugging

1. `git bisect` - Use binary search to find the commit that introduced a bug
   - `git bisect <start|good|bad|new|reset>`

### Miscellanous

1. `git reflog`
   - Reference log
1. `git branch -m <new_branch_name>`
   - Rename current branch
1. `git diff [source branch] [target branch]`
   - Preview changes before merging
1. Accidentally creating commit on main branch instead of a separate branch. Courtesy of `https://ohshitgit.com/`
   - create a new branch from the current state of master
     - `git branch <new_branch>`
   - remove the last commit from the master branch
     - `git reset HEAD~ --hard`
   - `git checkout <new_branch>`
1. `git log --all --decorate --oneline --graph`
   - View commit history with branches
   - `git checkout -b <branch-name> <commit-hash>`
     - Create (restore) a new branch from a specific commit
