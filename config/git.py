# Python script for comparing git dirs. It's basically bash but with easier vars.
from subprocess import call
dir = "gitdir" 

def compare():
	call(["git", "-C", dir, "fetch"])
	LOCAL = call(["git", "-C", dir, "rev-parse", "@"])
	BASE = call(["git", "-C", dir, "merge-base", "@", "master"])
	if LOCAL == BASE:
		call(["git", "-C", dir, "pull"])
compare()

