import os
from os import listdir

from PIL import Image, ImageDraw, ImageFont


image_types = ['jpg', 'jpeg', 'png']


# Creating output folder if doesn't exist
try:
	os.makedirs('output-images')
except OSError as e:
	pass

# Reading all files in the directory
for image in listdir('./source-images'):
	splitted = image.split('.')

	# Checking the type of file
	if splitted[-1].lower() in image_types:

		# Deleting the termination to make sure to work in a case like 'downey-jr.-robert.png'
		del splitted[-1]

		#creating the string of the final name. 
		name = ''
		for x in splitted:
			name += x
		name = name.split('-')
		f_name = ''
		counter = 1
		for x in name:
			f_name += x.capitalize()
			counter += 1
			if counter == len(name):
				f_name += ' '

		# Manipulating with Pillow
		img = Image.open('./source-images/'+image).convert("RGB")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("./fonts/Roboto-Light.ttf", 30)
		size = draw.textsize(f_name, font)
		draw.text((img.width - size[0]-15, img.height-size[1]-15), f_name, (255,255,255), font=font)
		img.save('./output-images/'+image)