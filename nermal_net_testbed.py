"""A scratch pad of sorts, for testing whatever's on my mind."""


import imageio
import nermal_net_lib as nrm
import numpy
import random


def main():
    random.seed(12345)
    sample_files = random.sample(nrm.GetFilenames("./data/"), 20)
    arrs = [nrm.LoadGIF(giffile) for giffile in sample_files]

    arr = arrs[0]
    int_arr = nrm.ToUnsignedByte(arr)
    for arr_i, int_arr_i in random.sample(zip(arr.ravel(), int_arr.ravel()), 100):
        print arr_i, int_arr_i
    pairs = sorted([(a, i) for a, i in zip(arr.ravel(), int_arr.ravel())],
                   key=lambda t: abs(t[1] - t[0]))
    for p in pairs[:10]:
        print p
    for p in pairs[-10:]:
        print p

    arrs = [nrm.LoadGIF(giffile, gray=False) for giffile in sample_files]
    for a in arrs:
        print a.dtype

if __name__ == "__main__":
    main()
