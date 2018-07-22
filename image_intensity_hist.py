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

    all_hists = []
    for arr in arrs:
        val_counts = [0 for _ in range(256)]
        for pixel in arr.ravel():
            val_counts[pixel] += 1
        all_hists.append(val_counts)

    with open(outfilename, "w") as outfile:
        outfile.write("Intensity," + ",".join(sample_files) + "\n")
        for i in range(256):
            row = ",".join([str(hist[i]) for hist in all_hists])
            outfile.write(str(i) + "," + row + "\n")


if __name__ == "__main__":
    main(sys.argv)
