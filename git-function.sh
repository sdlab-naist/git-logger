function git(){
	check=`command git rev-parse --is-inside-work-tree 2> /dev/null`

	if [ -z ${vcs} ] && [ "$check" = "true" ]; then
		timestamp=`date +"%Y%m%d-%H%M%S"`
		before_sha=`command git rev-parse --verify HEAD`
		echo LOG,"$timestamp,${PWD},$@,$before_sha" >> $HOME/.git_history
	fi
	command git "$@"
}
