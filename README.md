# HDF5 Extractor
extract CT images from HDF5 file for LoDoPaB-CT Dataset

- `ex2png-single-core.py` extract images with single core
- `ex2png-multi-core.py` extract images with multi core

## Parsing
    -i  :   prompt input directory
## Syntax
change `YOUR_INPUT_DIRECTORY` as you need.
```
 python ex2png-single-core.py -i `YOUR_INPUT_DIRECTORY`
 python ex2png-multi-core.py -i `YOUR_INPUT_DIRECTORY`
 ```

## Environment Dependencies
Using Anaconda virtual environment as `environment.yml` file.
#### Non built-in Libraries

| Library Name              | version | description      |
|----------------------|---------|------------------|
| [h5py](www.h5py.org)         | 2.9.0 | decode HDF5     |
| [tqdm](github.com/tqdm/tqdm) | 4.40.2| progress bar    |
| [numpy](numpy.org/)          | 1.17.4| matrix operation|
| [matplotlib](matplotlib.org/)| 3.1.1 | image I/O       |

###Log
First commit on Dec24, 2019