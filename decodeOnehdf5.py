import h5py
import numpy as np
import matplotlib.pyplot as plt


def show_images(images, cols=1, titles=None):
    """Display a list of images in a single figure with matplotlib.

    Parameters
    ---------
    images: List of np.arradecodeOnehdf5.pyys compatible with plt.imshow.

    cols (Default = 1): Number of columns in figure (number of rows is
                        set to np.ceil(n_images/float(cols))).

    titles: List of titles corresponding to each image. Must have
            the same length as titles.
    """
    assert ((titles is None) or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1, n_images + 1)]
    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles)):
        a = fig.add_subplot(cols, np.ceil(n_images / float(cols)), n + 1)
        if image.ndim == 2:
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    plt.show()


path = '/Volumes/home/datasets/lodopab-ct/ground_truth_test/ground_truth_test_000.hdf5'
path2 = '/Volumes/home/datasets/lodopab-ct/observation_test/observation_test_000.hdf5'

# 開啟hdf5檔案
hdf5 = h5py.File(path, 'r')
hdf5_keys = hdf5.keys()
print('keys=', hdf5_keys)

# 獲得影像的長寬高
data_buf = hdf5['data']
img_shape_slices, img_shape_width, img_shape_height = np.shape(data_buf)
print('there are', img_shape_slices, 'slices of', img_shape_width, 'x', img_shape_height, 'images')

img_buf_2d = []

img_buf_2d.append(data_buf[128, :, :])
hdf5.close()

show_images(img_buf_2d)
