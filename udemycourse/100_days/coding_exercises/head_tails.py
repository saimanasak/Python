'''
******************** Problem Statement ***********************

Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

'''

import random

toss = random.randint(0, 1)

if toss == 0:
    print("\n{} - Tails\n".format(toss))
else:
    print("\n{} - Heads\n".format(toss))