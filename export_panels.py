"""A scratch pad of sorts, for testing whatever's on my mind."""


import imageio
import nermal_net_lib as nrm
import numpy
import random


def main():
    random.seed(12345)
    filenames = random.sample(nrm.GetFilenames("./data/"), 10)
    for filename in filenames:
        orig_gif = nrm.LoadGIF(filename, gray=True)
        if orig_gif is None:
            print "Bogus file:", filename
            continue
        pad_gif = nrm.PadGIF2D(orig_gif)
        if pad_gif is None:
            print "Trouble with", filename, "; orig shape", orig_gif.shape
            continue
        panels = nrm.GetPanels(pad_gif)
        if panels is None:
            raise ValueError("Error fetching panels: %s; shape %s" %
                             (filename, str(pad_gif.shape)))
        for panel_id, panel in enumerate(panels):
            print panel.shape
            panel_filename = ("results/export_panels/out_" +
                              nrm.GetPanelFilename(filename, panel_id))
            nrm.SaveGIF(panel, panel_filename)


if __name__ == "__main__":
    main()
