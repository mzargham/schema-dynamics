import os
os.chdir("/Users/zargham/Documents/GitHub/cadcad-ri")
from cadcad.spaces import EmptySpace
from copy import deepcopy
spaceType = type(EmptySpace)

def drop_dimension(input:spaceType, dropkey:str)->spaceType:

    output = deepcopy(input)
    schema = output.__annotations__

    schema.pop(dropkey)

    return output


import urllib3
#import numpy as np

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

# response = urllib3.urlopen(word_site)
# txt = response.read()
# WORDS = txt.splitlines()
WORDS = ["apples", "bananas", "hi", "ho","byebye"]