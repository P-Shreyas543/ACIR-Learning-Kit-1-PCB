import os

step_file = 'ACIR-Learning-Kit-1-PCB/footprints.3dshapes/BatteryHolder_Keystone_1042_1x18650.step'
if os.path.exists(step_file):
    print("STEP file exists, size:", os.path.getsize(step_file))
else:
    print("STEP file not found at path.")
