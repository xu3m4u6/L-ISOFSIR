import sys
import os
from PIL import Image

# grab first and second argument
try:
	source = sys.argv[1]
	result = sys.argv[2]
except IndexError as err:
	print('Please enter the source folder name and result folder name.')
	raise err

# check if result folder exists, if not create one
if os.path.isdir(result):
	print(f'The images are going to be converted into PNG in {result}')
else:
	os.mkdir(result)
	print(f'A New folder {result} has been created to save the converted images.')

# loop through pokedex
# convert images into png
# save to the new folder
for file in os.listdir(source):
	if file.endswith(".jpg"):
		img = Image.open(source + file)
		img.save(result + file[:-4] + '.png','png')

print('All of the JPG images have been converted! Go check for it!')

