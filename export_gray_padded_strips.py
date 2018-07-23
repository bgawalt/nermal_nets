"""A scratch pad of sorts, for testing whatever's on my mind."""


import imageio
import nermal_net_lib as nrm
import numpy
import random


def main():
    random.seed(12345)
    found_small = False
    found_medium = False
    found_large = False
    found_too_large = False
    filenames = nrm.GetFilenames("./data/")
    random.shuffle(filenames)
    for filename in filenames:
        # Grayscale, but non-standard size:
        orig_gif = nrm.LoadGIF(filename, gray=True)
        if orig_gif is None:
            print "Bogus file:", filename
            continue
        # Row and column counts:
        rc, cc = orig_gif.shape
        output_file = ("results/export_gray_padded_strips/out" +
                       filename.split("/")[-1])
        if not found_small and rc < 170:
            found_small = True
            print "Found small:", filename, orig_gif.shape
            nrm.SaveGIF(nrm.PadGIF2D(orig_gif), output_file)

        if not found_medium and 170 < rc < 180:
            found_medium = True
            print "Found medium:", filename, orig_gif.shape
            nrm.SaveGIF(nrm.PadGIF2D(orig_gif), output_file)

        if not found_large and rc == 180:
            found_large = True
            print "Found large:", filename, orig_gif.shape
            nrm.SaveGIF(nrm.PadGIF2D(orig_gif), output_file)

        if not found_too_large and rc > 180:
            if nrm.PadGIF2D(orig_gif) is not None:
                raise ValueError("Wait, this was supposed to be too large")
            found_too_large = True
            print "Found too large:", filename, orig_gif.shape

        if found_small and found_medium and found_large and found_too_large:
            break


if __name__ == "__main__":
    main()
