import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if 'BH18650' in f or '1042' in f:
            print(os.path.join(root, f))
