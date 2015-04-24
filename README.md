# git-tracker
shellscript and git hook script for tracking git command

## Install
1. fix **original git** path at ./git file
```
<path of your original git> $@
```
1. allow git scripts
```
chmod +x ./git
```
1. allow git scripts
```
cp ./git /usr/local/bin/
```
1. allow hook scripts
```
chmod +x hooks/*
```
1. copy hook scripts to .git/hook
```
cp hooks/* .git/hooks
```
