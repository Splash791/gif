import imageio.v3 as iio

filenames = ['IMG_1288.jpg', 'IMG_1293.jpg']
images = [iio.imread(fname) for fname in filenames]

iio.imwrite('disney.gif', images, plugin='pillow', duration=500, loop=0)
