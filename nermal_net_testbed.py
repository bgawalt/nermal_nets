"""A scratch pad of sorts, for testing whatever's on my mind."""


import imageio
import nermal_net_lib as nrm


def main():
    giffile = nrm.GetFilenames("./data/")[0]
    print giffile
    arr = nrm.LoadGIF(giffile)
    print arr.shape


if __name__ == "__main__":
    main()
