"""Locate the data files in the eggs to open"""

"Special thanks to https://github.com/OrkoHunter/ping-me/tree/master/ping_me/data"
import os
import sys

def we_are_frozen():
    return hasattr(sys, "frozen")

def modeule_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname(unicode(sys.executable, encoding))
    return os.path.dirname(unicode(__file__, encoding))