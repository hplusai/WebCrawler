# coding=utf-8
from __future__ import print_function
import threading
_print_lock=threading.RLock()
_print=print

#safe print
def print(*args,**kwargs):
    with _print_lock:
        _print(*args,**kwargs)
