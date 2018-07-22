"""Generates aggregates of image intensity histograms as a CSV.

Usage:

  $ python image_intensity_hist.py output.csv


Output format: first column is intensity value, subsequent columns
each represent a percentiles on the number of pixels with that intensity across
a large sample of comics.  I.e., what's the median value of a comics' count of
pixels with intensity K, aggregated across all comics?
"""


import imageio
import nermal_net_lib as nrm
import numpy
import random
import sys


def main(args):
    outfilename = args[1]
    random.seed(12345)
    sample_files = random.sample(nrm.GetFilenames("./data/"), 1500)
    all_arrs = [nrm.LoadGIF(giffile) for giffile in sample_files]
    # Remove too-tall Sunday strips
    arrs = [arr for arr in all_arrs if arr.shape[0] > 190]

    all_hists = []
    for arr in arrs:
        val_counts = [0 for _ in range(256)]
        for pixel in arr.ravel():
            val_counts[pixel] += 1
        all_hists.append(val_counts)

    with open(outfilename, "w") as outfile:
        outfile.write("Intensity,2.5%%,25%%,50%%,75%%,97.5%%,Mean\n")
        for i in range(256):
            hist_vals = [hist[i] for hist in all_hists]
            pctiles = numpy.percentile(hist_vals,
                                       [2.5, 25, 50, 75, 97.5])
            row = ",".join([str(p) for p in pctiles])
            mean = numpy.mean(hist_vals)
            outfile.write(str(i) + "," + row + "," + str(mean) + "\n")


if __name__ == "__main__":
    main(sys.argv)
