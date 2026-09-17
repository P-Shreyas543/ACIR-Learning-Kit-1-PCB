# Let's inspect the exact solder mask geometry or parse the gerbers to understand the 28 warnings
import os, zipfile

zip_path = 'ACIR-Learning-Kit-1-PCB/production/ACIR_LEARNING_KIT_1_-_CHARACTERIZATION__EXPERIMENTATION_BOARD_v2.0.zip'
if os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        print("Files in production zip:")
        for name in z.namelist():
            print(" ", name)
