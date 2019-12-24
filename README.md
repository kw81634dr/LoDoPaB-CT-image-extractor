# HDF5 Extractor
extract CT images from HDF5 file for LoDoPaB-CT Dataset

###### `ex2png-single-core` extract images with single core
###### `ex2png-multi-core` extract images with multi core

## Parsing
##### -i `YOUR_INPUT_DIRECTORY`:give input directory
## Syntax
- python ex2png-single-core.py -i `YOUR_INPUT_DIRECTORY`
- python ex2png-multi-core.py -i `YOUR_INPUT_DIRECTORY`
- change `YOUR_INPUT_DIRECTORY` as you need.
## Environment Dependencies
Using Anaconda virtual environment as `environment.yml` file.

* tqdm
* numpy
* matplotlib

###Log
First commit on Dec24, 2019