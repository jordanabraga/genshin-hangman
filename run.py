import random
import sys
import time
import simple_colors

# Function to display text as if typed

def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(6./90)
