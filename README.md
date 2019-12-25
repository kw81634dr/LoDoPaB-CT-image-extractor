# HDF5 Extractor for LoDoPaB-CT

[![md-py-ver](https://img.shields.io/badge/python-v3.7-blue?style=flat-square&logo=appveyor)](http://commonmark.org)

extract CT images from HDF5 file for [LoDoPaB-CT Dataset](https://arxiv.org/abs/1910.01113)

LoDoPab-CT Dataset [Download Link](https://zenodo.org/record/3384092#.XgMFfRczby0)

 `ex2png-single-core.py` extract images with single core

 `ex2png-multi-core.py` extract images with multi core

### Parser
    -i  :   prompt input directory
### Syntax
change `YOUR_INPUT_DIRECTORY` as you need.
```
 python ex2png-single-core.py -i `YOUR_INPUT_DIRECTORY`
 python ex2png-multi-core.py -i `YOUR_INPUT_DIRECTORY`
 ```

## Environment & Dependencies
Python version == 3.7.5

With Anaconda virtual environment as `environment.yml` file.
#### Non built-in Libraries

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