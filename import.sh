#!/bin/sh
# Install hook scripts
if [ $# == 2 ] && [ "$1" == "install" ]; then
	arg=$2
	path="${arg%/}"
	git_path=$(eval cd "$path";command git rev-parse --git-dir 2> /dev/null)
	if [[ ! -z $git_path ]]; then
		eval cp $(echo $(cd $(dirname $0);pwd))/hooks/* $path/.git/hooks/
	fi
else
	echo "usage: install path/to/git/repo"
fi
