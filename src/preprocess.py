import os, shutil
import zipfile
import matplotlib.pyplot as plt
from numpy import array, zeros
from scipy.misc import imread
from glob import glob


testset = [
    'neurofinder.00.00.test', 'neurofinder.00.01.test', 'neurofinder.01.00.test',
    'neurofinder.01.01.test', 'neurofinder.02.00.test','neurofinder.02.01.test',
    'neurofinder.03.00.test', 'neurofinder.04.00.test', 'neurofinder.04.01.test'
]

trainset = [
    'neurofinder.00.00', 'neurofinder.00.01', 'neurofinder.00.02',
    'neurofinder.00.03', 'neurofinder.00.04','neurofinder.00.05',
    'neurofinder.00.06', 'neurofinder.00.07','neurofinder.00.08',
    'neurofinder.00.09','neurofinder.00.10', 'neurofinder.01.00',
    'neurofinder.01.01'
]


base_dir = '/Users/leixian/anaconda2/CSCI8360/project3/data'

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

for test in testset:
    src = os.path.join(base_dir, 'neurofinder.'+ test + '.zip')
    dst = os.path.join(test_dir, 'neurofinder.'+ test + '.zip')
    shutil.copyfile(src, dst)
    zip_ref = zipfile.ZipFile(dst, 'r')
    zip_ref.extractall(test_dir)
    zip_ref.close()
for train in trainset:
    src = os.path.join(base_dir, 'neurofinder.'+ train + '.zip')
    dst = os.path.join(train_dir, 'neurofinder.'+ train + '.zip')
    shutil.copyfile(src, dst)
    zip_ref = zipfile.ZipFile(dst, 'r')
    zip_ref.extractall(train_dir)
    zip_ref.close()


# load the images for one sample
files = sorted(glob(train_dir+'/neurofinder.00.00/images/*.tiff'))
imgs = array([imread(f) for f in files])
#standard normalization to scale pixel to 0 mean and 1 std.
scaled_imgs = array([(img-img.mean())/img.std() for img in imgs])
