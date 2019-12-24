import h5py
import numpy as np
import matplotlib.pyplot as plt
import os

# path = '/Volumes/home/datasets/lodopab-ct/ground_truth_test/ground_truth_test_000.hdf5'
rootdir = '/Volumes/home/datasets/lodopab-ct/ground_truth_train'


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        file_path = subdir + os.sep + file

        if file_path.endswith(".hdf5"):
            print("processing...", os.path.basename(file_path))
            save_dir = os.path.dirname(file_path) + os.sep + os.path.basename(file_path)[:-5] + '_png'

            # 檢查目錄是否存在
            # 使用 try 建立目錄
            try:
                os.makedirs(save_dir)
            # 檔案已存在的例外處理
            except FileExistsError:
                print("檔案已存在。")

            # 開啟hdf5檔案
            hdf5 = h5py.File(file_path, 'r')
            hdf5_keys = hdf5.keys()
            # 獲得影像的長寬高
            data_buf = hdf5['data']
            img_shape_slices, img_shape_width, img_shape_height = np.shape(data_buf)
            print('there are', img_shape_slices, 'slices of', img_shape_width, 'x', img_shape_height, 'images')
            for i in range(0, img_shape_slices - 1):
                save_filename = save_dir + os.sep + "%d.png" % i
                plt.imsave(save_filename, data_buf[i, :, :], cmap='gray')
            hdf5.close()

