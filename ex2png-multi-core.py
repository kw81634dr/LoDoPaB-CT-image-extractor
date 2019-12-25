#!/usr/bin/env python

"""
Description: Extract images from HDF5 file then save as PNG image with Multi-core supported.
To-Do: make hdf5 keys customizable
"""
__author__ = "Kevin Wang"
__copyright__ = "Copyright 2019, The Proposal"
__license__ = "MIT"
__version__ = "1.2"
__date__ = "2019/12/24"
__status__ = "Production"


import os
import sys
import argparse
from pathlib import Path
import multiprocessing as mp
import h5py
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


def walk_and_grab_files(path, extension=''):
    temp_list = []
    # --Recursively 'glob' all files with given extension under the current directory--
    for hdf5file in Path(path).rglob('*.' + extension):
        temp_list.append(hdf5file)
    return temp_list


def convert2png(arg1):
    with h5py.File(arg1, 'r') as h5file:
        data_buf = h5file['data']
        img_shape_slices, img_shape_width, img_shape_height = np.shape(data_buf)
        for imgSlice in range(img_shape_slices):
            # --get one slice from stack then transpose the matrix.--
            temp = np.transpose(data_buf[imgSlice, :, :])
            save_dir = Path(arg1.parent).joinpath("png", arg1.stem)
            if not (Path(save_dir).expanduser().exists()):
                os.makedirs(save_dir)
            new_filename = Path(save_dir).joinpath('{}.png'.format(imgSlice))
            # --save image as PNG file.--
            plt.imsave(str(new_filename), temp, cmap='gray')
        h5file.close()


if __name__ == '__main__':
    # --parser--
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', help='Input Directory')

    # --show help info if no argument given--
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # --parse arguments--
    args = parser.parse_args()
    given_path = Path(args.input).expanduser()

    # --check the given directory exists or not--
    try:
        checked_path = given_path.resolve(strict=True)
    except FileNotFoundError:
        print('cannot find the directory:"', given_path, '"')
    else:
        # --walk through the directory to find all eligible files--
        file_list = walk_and_grab_files(checked_path, 'hdf5')
        print('will process', len(file_list), 'files...')
        # --process with multi-core & progress bar--
        with mp.Pool(mp.cpu_count()-2) as p:
            list(tqdm(p.imap(convert2png, file_list), total=len(file_list)))
    print("Done.")
