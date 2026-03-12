# Intro:
```bash
# Machine 1: Init and First Commit
git init
git branch -M main # using main, cause society hates masters
git status

echo "Hello World" > file-a
git status
git diff

git add file-a
git status
git diff --staged

git commit # or: git commit -m "init: Hello World"
git status
git log --oneline --graph --all

git remote add origin git@github.com:example_user/example_repo_name.git
git push -u origin main # in gitlab it creates the repo for you here, in github we must go to their website to create it manually

git config user.name "example_username" # you can add the '--global' flag if you only have one provider
git config user.email "example_email" # not verified (fix: digital signatures)

# Example Mistake
echo "dont commit this" >> ignorethisfile
git status

echo "ignorethisfile" >> .gitignore
git status # notice ignorethisfile is missing

# Machine 1: Setup Branches
git checkout -b dev
git push -u origin dev

git checkout -b feature-audio
git push -u origin feature-audio

# Machine 2: Clone and Feature Video
git clone git@github.com:example_user/example_repo_name.git
cd example_repo_name
git checkout dev
git checkout -b feature-video
git push -u origin feature-video

git log --oneline --graph --all

# Machine 1: Dev Work
git checkout dev
echo "feature base" >> file-a
git add file-a
git commit

# Machine 1: Audio Feature Work
git checkout feature-audio
echo "feature audio 1" >> file-a
git add file-a
git commit

echo "feature audio 2" >> file-a
echo "feature audio 3" >> file-a

git add -p # show how to edit hunks
git diff --staged
git commit

git add -p
git commit

git push

# Machine 2: Video Feature Work
git checkout feature-video
echo "feature video" >> file-a
git add file-a
git commit
git push
git log --oneline --graph --al
git branch --all

# Machine 1: Merge Audio into Dev
git log --oneline --graph --all
git fetch # this gets the metadata from the server
git log --oneline --graph --all
git checkout dev
git merge feature-audio
git diff --check
git diff --diff-filter=U
git diff --ours
git diff --theirs
git log --oneline --left-right --merge
# [resolve conflict]
git add file-a
git status
git commit
git log --oneline --graph --all

# Machine 1: Rebase Video
git checkout feature-video
git pull # this is very similar to `git fetch` and then a `git merge`
git rebase -i dev feature-video
git diff --diff-filter=U
# [resolve conflict]
git add file-a
git status
git rebase --continue

git checkout dev
git merge feature-video
git log --oneline --graph --all
git push

git push -d origin feature-video # delete the remote branch (not required, but makes the graph nicer)
git log --oneline --graph --all

# development, feature and hotfix branches are the traditional way
# There are more ways. My favourite being the identity way.
git checkout main
git push -d origin dev
git push -d origin feature-audio
git push -d origin feature-video
git checkout -b dev

git checkout dev
git checkout -b example_username-work-laptop
# do work here

git checkout dev
git checkout -b example_username-home-computer
# do work here
git merge example_username-work-laptop # we can also just merge horizontally, since we dont care about a 'sane' graph
# do work here
# since we have our own workspace now, we have 0 chance of a conflict, meaning we can optimize our workflow
alias gsync='git fetch && git commit -a && git push'
gsync

git checkout dev
git merge example_username-work-laptop
git merge example_username-home-computer
```
# TODO: gotta convert this into more presentable form, and reverify correctness
- cmdline explain

- aliases

- ssh
- ssh-agent

# Advanced
```bash
# .gitignore
echo '*.exe' >> .gitignore # dont add '*.exe' files to git

# the list of numbers&letters that appear on our commits are hashes
# hashes are just math scrambled versions of our data so that we can
# refer to a commit with a name
# the reason we don't just keep a running total number is that:
# 1. users may be editing the repo offline at different times (distributed systems)
# 2. maybe we don't want to be able to enumerate commits for security reasons
# 3. it is unique based on the content (and time), so it is easier to tell commits apart

# worktrees
git clone git@github.com:example_user/example_repo_name.git example_repo_name_worktree # only clones the '.git/*'
cd example_repo_name_worktree
# worktree(./) -add> staging(./.git/index) -commit>  repository(./.git/objects)
# repository(./.git/objects) -checkout> worktree(./)
# we have '.git/*' (staging and repository), so we need worktree; we can have more than one
# which lets us work on multiple branches at the same time
git worktree add example_username-work-laptop
git worktree add example_username-home-computer

# git tags
git tag -a "v0.0.1" # semantic versioning for releases (semver.org)
# i dont work at a company that *really* cares about this, so i have my own variation
# `<version> = v<major>.<minor>.<patch>-<type>`
# `<type>` is a suffix letter, normally placed if i want to notify myself about weird things
# u = unstable (i think the code could be better tested, or i just made a big change)
# f = hotfix (i quickly threw this together trying to fix things)
```
