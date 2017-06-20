"""
A small utility for the *not-git-aware* to commit and push changes to a git-aware repository

## Functions
:save   git commit
:upload git push
"""

import subprocess
from datetime import datetime


def _system(cmd):
    ret = subprocess.Popen(cmd, shell=True, stdin = subprocess.PIPE,
    stdout = subprocess.PIPE, stderr = subprocess.PIPE, close_fds = True)
    out, err = ret.communicate()
    return out, err, ret.returncode


def sanityCheck():
    """
    Check if this is a git repo with some commits
    """
    # TODO Refine the purpose of this function
    out, err, retcode = _system('git log')
    if b"fatal" in err:
        return False
    else:
        return True


def save(msg = str(datetime.now())):
    """
    Commits the modified file in the repository
    """
    out, err, retcode = _system('git commit -a -m ' + '"' + msg + '"')
    if retcode == 0:
        pass
        # FLAG SUCCESS, ask push?
    else:
        print("ERROR: " + retcode)  # Not the best way to report errors


def upload(remote = 'origin', branch = 'master'):
    out, err, retcode = _system('git push -u ' + remote + branch)
    if retcode == 0:
        pass
        # FLAG SUCCESS?

    else:
        print("ERROR: " + retcode)
