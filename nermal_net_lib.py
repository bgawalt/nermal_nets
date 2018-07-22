import imageio
import numpy
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
    """Returns a 2- or 3-D numpy array of the GIF (or None on fail)"""
    # This should be of shape (num rows, num cols, 4)
    try:
        img = imageio.imread(gif_filename, format="gif")
    except ValueError:
        return None
    if len(img.shape) != 3 or img.shape[2] != 4 or img[:, :, 3].mean() != 255:
        return None
    if not gray:
        return img
    return numpy.dot(img[..., :3], [0.2989, 0.587, 0.144])
