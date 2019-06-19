# Useful Tools

* debye_frequency.py is used to calculate debye frequency of materials. (Debye temperature should be known first)

* jogInteraction.py is used to calculate elastic interaction energy of a jog pair using anisotropic properties.

* coulomb_vs_elastic.py is used to compare the coulomb force and elastic interaction force.

* jogInteraction_isotropic.py is used to calculate elastic interaction energy of jog pair by using isotropic properties.

* rotation.py is used to rotate atoms along x axis by a specified degree. Details information see the code.

* deleteUselessFolderDumpfile.py is used to delete useless dumpfiles in seperate folders (useful in calculating point distribution energy)

* zeus2my.py is used to copy files in subfolders between hpc and my computer.

* zip_unzip.py is used to zip or zip files in folders v_mg and/or v_o (including subfolders in v_mg and/or v_o).

# Useful commands

* gzip name_of_file (gzip initial.lmp)

* gunzip name_of_file (gunzip initial.lmp.gz)

* tar -czvf final_file.tar.gz file1 file2 ... filen (tar -czvf results.tar.gz initial.lmp dump.relax* build_noclimb.sh)

* tar -xzvf final_file.tar.gz (tar -xzvf results.tar.gz)

* zip final_file.zip file1 file2 ... filen (zip results.zip initial.lmp dump.relax* )

* unzip final_file.zip (unzip results.zip)
