import sys
import os
from types import ModuleType

# Create complete pygit2 mock
pygit2 = ModuleType('pygit2')
pygit2.GIT_FILTER_CLEAN = 0
pygit2.GIT_FILTER_SMUDGE = 1  
pygit2.GIT_REPOSITORY_OPEN_NO_SEARCH = 0
pygit2.GitError = type('GitError', (Exception,), {})
pygit2.Filter = type('Filter', (), {})
pygit2.Repository = type('Repository', (), {})
sys.modules['pygit2'] = pygit2

# Run DVC
from dvc.cli import main
main()