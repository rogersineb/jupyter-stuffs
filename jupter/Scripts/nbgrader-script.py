#!e:\jupyter-stuffs\jupter\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'nbgrader==0.6.1','console_scripts','nbgrader'
__requires__ = 'nbgrader==0.6.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('nbgrader==0.6.1', 'console_scripts', 'nbgrader')()
    )
