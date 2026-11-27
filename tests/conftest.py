import os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path: sys.path.insert(0,ROOT)
ENGINE=os.path.join(ROOT,'app','engine')
SETTINGS=os.path.join(ENGINE,'settings')
for path in (ENGINE,SETTINGS):
    if path not in sys.path: sys.path.insert(0,path)
