"""Generates image intensity histograms as a CSV.

Usage:

  $ python image_intensity_hist.py output.csv


Output format: first column is intensity value, subsequent columns represent
one random comic and their pixel-counts for each intensity.
"""


import imageio
import nermal_net_lib as nrm
import numpy
import random
import sys


def main(args):
    outfilename = args[1]
    random.seed(12345)
    sample_files = random.sample(nrm.GetFilenames("./data/"), 30)
    arrs = [nrm.LoadGIF(giffile) for giffile in sample_files]

    hist = nrm.Histogram()

    all_hists = []
    for arr in arrs:
        hist.AddPanel(arr)

    counts = hist.Counts()
    s = 0
    total = sum(counts)
    for pixel_val, count in enumerate(counts):
        s += count
        if count < 0.01 * total:
            continue
        print "%d\t%0.3f\t%0.3f" % (
            pixel_val, float(count) / total, float(s) / total)


if __name__ == "__main__":
    main(sys.argv)
