import md
import os
from ase.io import read
md.run_md()
traj_file = "cu.traj"
atoms = read(traj_file)
assert os.path.exists(traj_file) # Check if file exists
assert os.path.getsize(traj_file) # Check if file is not empty
assert len(atoms) == 4000

print("Integration test completed, traj file exsists and number of atoms are correct.")