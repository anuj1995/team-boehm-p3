
'''
    NMF model using test dataset to calculate the neuor coordinates and return a json file.
    Reference:
    NMF example for neuron images in thunder: https://gist.github.com/freeman-lab/330183fdb0ea7f4103deddc9fae18113
    How to run: python NMF.py -d '/Users/leixian/Downloads/test/' -o '/Users/leixian/Downloads/'
	python NMF.py -d '/Users/leixian/Downloads/test/' -o '/Users/leixian/Downloads/'
'''
import json
import os
from glob import glob
import argparse
import thunder as td
from extraction import NMF

def main(arg):
    datasets = os.listdir(arg.test)
    submission = []
    for dataset in datasets:
        if dataset.startswith('neuro'):
            if '00.00' in dataset:
                k_param = 10
                percentile_param=95
                max_iter_param=60
                chunk_size_param=50
            elif '00.01' in dataset:
                k_param = 10
                percentile_param=95
                max_iter_param=60
                chunk_size_param=50
            elif '01.00' in dataset:
                k_param = 5
                percentile_param=95
                max_iter_param=70
                chunk_size_param=50
            elif '01.01' in dataset:
                k_param = 10
                percentile_param=95
                max_iter_param=40
                chunk_size_param=50
            elif '02.00' in dataset:
                k_param = 5
                percentile_param=99
                max_iter_param=30
                chunk_size_param=50
            elif '02.01' in dataset:
                k_param = 5
                percentile_param=99
                max_iter_param=30
                chunk_size_param=50
            elif '03.00' in dataset:
                k_param = 10
                percentile_param=95
                max_iter_param=70
                chunk_size_param=45
            elif '04.00' in dataset:
                k_param = 5
                percentile_param=97
                max_iter_param=60
                chunk_size_param=50
            elif '04.01' in dataset:
                k_param = 5
                percentile_param=95
                max_iter_param=60
                chunk_size_param=50
            print('processing dataset:' + dataset)
            print('loading')
            data = td.images.fromtif(arg.test + dataset + '/images', ext='tiff')
            print('analyzing')
            algorithm = NMF(k=k_param, percentile=percentile_param, max_iter=max_iter_param, overlap=0.1)
            model = algorithm.fit(data, chunk_size=(chunk_size_param,chunk_size_param), padding=(25,25))
            merged = model.merge(0.1)
            print('found %g regions' % merged.regions.count)
            regions = [{'coordinates': region.coordinates.tolist()} for region in merged.regions]
            result = {'dataset': dataset, 'regions': regions}
            submission.append(result)

    print('writing results')
    with open(arg.outputDir + 'submission.json', 'w') as f:
    	f.write(json.dumps(submission))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This is CSCI8360 project 3, implemented NMF methods')

    parser.add_argument('-d','--test',required = True,
                        help='The test dataset directory which is the input for our NMF model')
    parser.add_argument('-o', '--outputDir', default = '..',
                        help = 'Path to store the json results of coordinates of neurons')
    args = parser.parse_args()
    main(args)

