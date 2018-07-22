"""A scratch pad of sorts, for testing whatever's on my mind."""


import imageio
import nermal_net_lib as nrm
import random


def main():
    random.seed(12345)
    sample_files = random.sample(nrm.GetFilenames("./data/"), 20)
    arrs = [nrm.LoadGIF(giffile) for giffile in sample_files]
    for fname, arr in zip(sample_files, arrs):
        print fname, ":", arr.shape


if __name__ == "__main__":
    main()
