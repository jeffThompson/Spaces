
import os, shutil

'''
SPACES
Jeff Thompson | 2018 | jeffreythompson.org

A conceptual art worm that changes the name of all your 
files and folders to whitespace. USE AT YOUR OWN RISK.

This...
  folder/
    file1.txt
    file2.txt
  anotherFolder/
    file3.wav
    file4.mp4

...will become this (no quotes, of course)
  '      '/
    '     '.'   '
    '     '.'   '
  '             '/
    '     '.'   '
    '     '.'   '

'''

# where to start from, should be a full path
# (this will run on the user's home directory - if we were
# to do it on the root folder for the system (os.path.abspath(os.sep))
# we'd wipe out system files and never get anywhere)
target_folder =   os.path.expanduser('~')

keep_extensions = False		# keep original file extensions?
							# otherwise, they become '.   '

rename_target =   False		# rename the target folder too when done?

print_info =      True		# let us know what's going on?

make_some_files = False		# optionally, make some files to work with
num_levels = 	  10		# how many subfolders to make?
num_files =  	  10		# how many files to make in each?


# make some files to play with
# (easier than copying a ton every time we want to test)
'''
if make_some_files:

	# remove previous version, if it exists
	prev_folder = os.path.join(__location__, ' ')
	if os.path.exists(prev_folder):
		shutil.rmtree(prev_folder)

	# make the directory, generate some files
	os.mkdir(target_folder)
	os.chdir(target_folder)
	for level in range(num_levels):
		
		# make some files here
		for i in range(num_files):
			with open(str(i) + '.txt', 'w') as f:
				f.write('')

		# make a folder here and go inside
		os.mkdir(str(level))
		os.chdir(str(level))
'''


# go to the starting folder
os.chdir(target_folder)


# do it
# (topdown walks us from the further-in dir towards the start,
# which lets us rename directories as we go)
for root, directories, files in os.walk(target_folder, topdown=False):
	if print_info:
		print root, directories, files

	# rename directories in the folder
	if len(directories) > 0:
		for i, directory in enumerate(directories):
			old = os.path.join(root, directory)
			new = os.path.join(root, (' '*(i+1)))
			shutil.move(old, new)

	# and all the files too
	if len(files) > 0:
		for i, file in enumerate(files):
			old = os.path.join(root, file)
			new = os.path.join(root, (' '*i))
			if keep_extensions:
				name, ext = os.path.splitext(old)
			else:
				ext = '.   '
			new += ext
			os.rename(old, new)


# when done, rename the main folder
if rename_target:
	old = os.path.join(target_folder)
	new = os.path.join(__location__, ' ')
	shutil.move(old, new)

