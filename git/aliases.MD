1. `gcln='git remote prune origin; git for-each-ref --format '\''%(refname:short)'\'' refs/heads | grep -v "master\|main" | xargs git branch -D; git pull'`
