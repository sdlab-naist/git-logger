#!/bin/sh
# Install hook scripts
echo "Type the path of your git repository: "
read path
path="${path%/}"
git_path=$(eval cd "$path";git rev-parse --git-dir 2> /dev/null)
if [[ ! -z $git_path ]]; then
	eval cp $(echo $(cd $(dirname $0);pwd))/hooks/* $path/.git/hooks/
fi
