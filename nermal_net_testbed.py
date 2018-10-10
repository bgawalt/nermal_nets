"""A scratch pad of sorts, for testing whatever's on my mind."""


import imageio
import nermal_net_lib as nrm
import numpy
import random

import pickle
import base64


def main():
    random.seed(12345)
    sample_files = random.sample(nrm.GetFilenames("./data/"), 4)

    nrm.SaveAllPanelsToDB("./data", "nermal.db")

    return

    for giffile in sample_files:
        int_arr = nrm.LoadGIF(giffile)
        if int_arr is None:
            continue
        pad_arr = nrm.PadGIF2D(int_arr)
        if pad_arr is None:
            continue
        for panel in nrm.GetPanels(pad_arr):
            print base64.encodestring(pickle.dumps(panel))
            print ''

    return



    arr = arrs[0]
    int_arr = nrm.ToUnsignedByte(arr)
    lucky_pairs = random.sample(zip(arr.ravel(), int_arr.ravel()), 100)
    for arr_i, int_arr_i in lucky_pairs:
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
