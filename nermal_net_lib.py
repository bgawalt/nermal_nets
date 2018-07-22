import imageio
import os


def GetFilenames(data_dir):
    """Returns filenames for Garfield comics in .gif format in given directory.

    (Doesn't actually check if they *are* gifs, just if they *end* in 'gif'.)
    """
    subdir_candidates = [os.path.join(data_dir, candidate)
                         for candidate in os.listdir(data_dir)]
    subdirs = [sd for sd in subdir_candidates if os.path.isdir(sd)]
    gifs = []
    for subdir in subdirs:
        gifs.extend([os.path.join(subdir, gif)
                     for gif in os.listdir(subdir) if gif.endswith("gif")])
    return gifs


def LoadGIF(gif_filename, gray=True):
    """Returns a numpy array of the GIF."""
    return imageio.imread(gif_filename, format="gif")
