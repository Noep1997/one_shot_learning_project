# Philippe M. Noel
# Renaming jpg file names for machine learning purposes
# This file was used to rename the Omniglot files for training
import os

def renaming(directory, folder):
	""" Renames all the files in directory to from directoryname_filename.png """
	# rename every file in the directory
	for file in sorted(os.listdir(directory)):
		# rename the file
		os.rename(os.path.join(directory, file), os.path.join(directory, str(folder) + '_' + str(file)))
	print("Finished folder " + str(folder)) # progress track

# function call
dir = '/Users/Philippe/Downloads/images/'
for folder in sorted(os.listdir(dir)): # skip DS_store
	renaming(os.path.abspath(dir + str(folder) + '/'), folder)

print("All done!")
