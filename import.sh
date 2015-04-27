#!/bin/sh
# Install hook scripts
if [ $# == 1 ]; then
	arg=$1
	path="${arg%/}"
	git_path=$(eval cd "$path";git rev-parse --git-dir 2> /dev/null)
	if [[ ! -z $git_path ]]; then
		eval cp $(echo $(cd $(dirname $0);pwd))/hooks/* $path/.git/hooks/
	fi
else
	echo "usage: import.sh path_of_git_repo"
fi
