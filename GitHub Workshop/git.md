# Intro:
```bash
# NOTE: this is abridged and slightly abstracted, perhaps even incorrect at times

# goal for today:
# - understand some git words to debug in the future
# - understand the very basics on how to save your code
# - understand the purpose and idea of branching
# - understand the purpose and idea of merging

# git is a software, it lets you upload/download code snapshots to/from a server
# while also managing concurrent offline modifications.
# Github is a company that hosts git instances for you to upload your code to.

# install git (if you haven't done this, don't worry, the content is simple)

# remember, most command lines work by taking the first word as a command/binary name
# the rest of the text is space separated and given to the program at startup

# how git works:
# there is some central server that stores all the data for the repository
# users make copies of the repository and edit it offline (not live edit)
# users then submit changes to the server
# any changes that happened to the combination of *all* the following will cause a conflict
# when trying to merge the user's change with the current state:
# - and to the same branch # explained below
# - and to the same file
# - and to the same area
# a repository is a history of commits in a directed acyclic graph (a graph with no cycles, uni-directional; history only flows forwards)
# branches are ways to keep track of a commit position on the graph
#
# local git:
# state for files
# - untracked: files that are not being tracked
# state for repo:
# - unstaged: changes that are not tracked
# - staging: changes that are being tracked
# - remote: the changes from the server, you will add to the history and send it to the server
# the things you add to the history are called commits (package of a set of changes)



# GOAL: create a codebase
# Machine 1: Make a Codebase
    mkdir git_example
    cd git_example
    echo "Hello World" > file-a
# CONCLUDE: boom



# GOAL: we want to setup a backup system to remember previous versions of our code
# Machine 1: Init and First Commit
    git init
    git branch -M main # rename current branch to main, cause society hates the default name: 'master'
    git status

    git status # 'file-a' is untracked, nothing in staging, nothing ready to send to remote
    git diff

    git add file-a # add file to staging
    git status
    git diff --staged

    # save all tracked changes with a name
    # if you haven't configured git, this might put a commit under some user's name on your computer
    git commit # or: git commit -m "init: Hello World"

    # setup git user info, cause that didn't work
    git config user.name "example_username" # you can add the '--global' flag if you only have one provider
    git config user.email "example_email" # not verified (fix: digital signatures)

    git commit
    git status
    git log --oneline --graph --all

    git remote add origin git@github.com:example_user/example_repo_name.git
    # in gitlab it creates the repo for you here, in github we must go to their website to create it manually
    git push -u origin main # send to the server

    # setup git ssh keys, cause that didn't work
    # the reason that we need these is for verifying that you are actually who you say you are
    # and passwords alone are inherently insecure methods of protecting your account.
    # of course many people like me secure their ssh keys behind a password.
    cd ~/.ssh
    ssh-keygen -t ed25519 -f ~/.ssh/github # ed25519 is a public-private key cryptography protocol
    # linux
    eval "$(ssh-agent -s)" # put this in startup
    ssh-add ~/.ssh/github # github is the name of the private key that I made
    # windows
    Get-Service -Name ssh-agent | Set-Service -StartupType Manual
    Start-Service ssh-agent # does windows require admin??
    ssh-add ~/.ssh/github # github is the name of the private key that I made

    # copy the PUBLIC KEY '~/.ssh/github.pub'
    # go to github.com > settings > SSH & GPG Keys > Add Key
    # paste the PUBLIC KEY into the box and save

    git push -u origin main
# CONCLUDE: we have now just saved our code to the hoster (Github)



# GOAL: show how we avoid adding huge or irrelevant files
# Machine 1: Example Mistake
    echo "don't commit this" >> ignorethisfile # examples are: *.swap, *.o, *.exe
    git status

    echo "ignorethisfile" >> .gitignore
    git status # notice ignorethisfile is missing
# CONCLUDE: we can now ignore files


# GOAL: our coworker wants to setup their development environment
# Machine 2: Clone
    git clone git@github.com:example_user/example_repo_name.git
    cd example_repo_name
    git status
# CONCLUDE: the coworker now has the a *copy* of the repo



# GOAL: we want to create our own development environment
# Machine 1: Setup Branches
    git checkout -b dev
    git push -u origin dev

    git checkout -b feature-audio # we don't put spaces in the branch name,
    # in fact I would prefer if you never used spaces in files either please
    git push -u origin feature-audio
# CONCLUDE: we now have an unstable branch off the main branch, and a feature branch off the unstable branch



# GOAL: the coworker creates the feature branch
# Machine 2: Feature Video
    git fetch
    git checkout dev
    git pull # this is very similar to `git fetch` and then a `git merge` to the latest branch commit
    git checkout -b feature-video
    git push -u origin feature-video
    git log --oneline --graph --all
# CONCLUDE: wow



# GOAL: simulate someone else adding code into the dev branch
    # Machine 1: Dev Work
    git checkout dev
    echo "feature base" >> file-a
    git add file-a
    git commit
    git push # we do this just for the consistency with how it would appear if someone else added code.
    # on local changes, we don't actually need to push the commits until we are ready
    git log --oneline --graph --all
# CONCLUDE: we now have a dev branch that is ahead of our feature branches



# GOAL: do some work on the audio branch
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
    git log --oneline --graph --all
# CONCLUDE: we now have a commit on the desynced branches



# GOAL: coworker does some work on the video branch
# Machine 2: Video Feature Work
    git checkout feature-video
    echo "feature video" >> file-a
    git add file-a
    git commit
    git push
    git log --oneline --graph --all
    git branch --all
    git fetch
    git log --oneline --graph --all
# CONCLUDE: we now have some changes on the other desynced branch



# GOAL: we will now perform a merge to pull changes from the audio feature branch into the dev branch
# Machine 1: Merge Audio into Dev
    git log --oneline --graph --all
    git fetch # this gets the metadata from the server
    git log --oneline --graph --all
    git checkout dev
    git pull
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
# CONCLUDE: you can now see both changes reflected in the code and the history



# NOTE: skip if we are low on time, just merge the coworker in
# GOAL: we will now perform a rebase (another merge technique) to pull video feature branch into the dev branch
# Machine 1: Rebase Video
    # WARN: this rewrites history, and if you make a mistake, you could lose your (or someone else's) changes
    # it is fixable by looking at the `git reflog`, since that stores all the actions made locally
    # however if you push these changes, then the other users might *seem* to lose their changes if they pull yours.
    # NOTE: from what I remember, git will *never* delete your commits (unless you force push, *try not to force push*),
    # just sometimes it will get hidden from the
    # main history tree
    git checkout feature-video
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
# CONCLUDE: realistically, you probably don't want this, because the hassle is high, and it does not gain you toooo much



# GOAL: review and simplify
    # development, feature and hotfix branches are the traditional way
    # There are more ways. My favourite being the identity way.
    git checkout main
    # we delete the other branches to make this simpler to view
    git push -d origin dev
    git push -d origin feature-audio
    git push -d origin feature-video
    git checkout -b dev

# Machine 1: we setup our development environment
    git checkout dev
    git pull
    git checkout -b example_username-work-laptop
    # do work here

# Machine 2: the coworker also sets up their development environment
    git checkout dev
    git pull
    git checkout -b example_username-home-computer
    # do work here

    # we can also just merge horizontally, since we don't care about a 'sane' graph
    git merge example_username-work-laptop
    # do work here
    # the advantage of this is that users never need to worry about whether there was someone
    # else on the branch unless they are merging, because they own the entire branch.
    # often the users will be forced to communicate during many pushes or repeatedly fetch the new changes
    # if the branch is commited to by multiple people.
    # since we have our own workspace now, we have 0 chance of a conflict, meaning we can optimize our workflow
    function gsync_commit() { echo "Quicksave: $(date +%Y-%m-%d_%H:%M:%S)"; }
    # if you prefer naming things, remove the `-m "message"`
    alias gsync='git pull && git commit -am "$(gsync_commit)" && git push'
    alias gsync_all='git pull && git add -A && git commit -m "$(gsync_commit)" && git push'
    alias gsync_patch='git pull && git add -p && git commit -m "$(gsync_commit)" && git push'
    gsync

    git checkout dev
    git merge example_username-work-laptop
    git merge example_username-home-computer
# CONCLUDE: this is how my closest friends and I work, as well as the previous team I worked on
```



# Advanced
```bash
# cooler git log
alias glog="git log --graph --all --pretty=format:'%C(auto)%h %C(blue)%ad%C(auto)%d %al: %C(green)%s%C(auto)' --date='format:%Y-%m-%d %Hh%M'"

# the list of numbers & letters that appear on our commits are hashes
# hashes are just math-scrambled versions of our data so that we can
# refer to a commit with a name
# the reason we don't just keep a running total number is that
# users may be editing the repo offline at different times (distributed systems)
# being unique dependent on many factors reduces the risk (so close to zero that no one ever has a problem)
# of collisions when two people make a commit referencing the same base and branch.
# the hashing ensures that we don't lose commits because the hash collided.
# secondary thoughts:

# worktrees: This is so "Expert" that I'm not sure if I'm actually going to talk about this
# I haven't used this anywhere but at companies that use feature branches. I'm like 90% sure that
# none of the students will care or get this.
git clone --bare git@github.com:example_user/example_repo_name.git example_repo_name_worktree # only clones the '.git/*'
cd example_repo_name_worktree
# worktree/work-directory(./) -add> staging(./.git/index) -commit>  repository(./.git/objects)
# repository(./.git/objects) -checkout> worktree(./)
# we have '.git/*' (staging and repository), so we need worktree; we can have more than one
# which lets us work on multiple branches at the same time
git worktree add example_username-work-laptop
git worktree add example_username-home-computer

# git tags: again, like who needs this?? if I have spare time, sure wtv.
git tag -a "v0.0.1" # semantic versioning for releases (semver.org)
# I don't work at a company that *really* cares about this, so I have my own variation
# `<version> = v<major>.<minor>.<patch>-<type>`
# `<type>` is a suffix letter, normally placed if I want to notify myself about weird things
# u = unstable (I think the code could be better tested, or I just made a big change)
# f = hotfix (I quickly threw this together trying to fix things)
```
