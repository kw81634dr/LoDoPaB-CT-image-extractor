# HDF5 Extractor for LoDoPaB-CT

[![md-py-ver](https://img.shields.io/badge/python-v3.7-blue?style=flat-square&logo=appveyor)](http://commonmark.org)
[![md-py-ver](https://img.shields.io/badge/license-MIT-green?style=flat-square&logo=appveyor)](http://commonmark.org)

Extract CT images from HDF5 file for [LoDoPaB-CT Dataset](https://arxiv.org/abs/1910.01113)

LoDoPab-CT Dataset [Download Link](https://zenodo.org/record/3384092#.XgMFfRczby0)

 `ex2png-single-core.py` extract images with single CPU core

 `ex2png-multi-core.py` extract images with multi CPU core


### Parser
    -i  :   prompt input directory which contains Hdf5 files
### Syntax
change `YOUR_INPUT_DIRECTORY` as you need.

The script will walk through all sub-directories to find out all eligible HDF5 files, 
extract CT images then save as PNG file in the same directory.

```
 python ex2png-single-core.py -i `YOUR_INPUT_DIRECTORY`
 python ex2png-multi-core.py -i `YOUR_INPUT_DIRECTORY`
 ```

## Environment & Dependencies
Using Python version == 3.7.5

With Anaconda virtual environment as **environment.yml** file,
which can be install by script 

`conda env create -f environment.yml`.
See [How to](https://www.anaconda.com/moving-conda-environments/)

#### Non built-in Dependent Libraries

| Library Name              | version | description      |
|----------------------|---------|------------------|
| [h5py](www.h5py.org)         | 2.9.0 | decode HDF5     |
| [tqdm](github.com/tqdm/tqdm) | 4.40.2| progress bar    |
| [numpy](numpy.org/)          | 1.17.4| matrix operation|
| [matplotlib](matplotlib.org/)| 3.1.1 | image I/O       |


### Disclaimer
For research only, use at your own risk.

Feel free to give your comments. Thanks!
###Log
First commit on Dec24, 2019