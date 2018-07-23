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


def ToUnsignedByte(arr):
    """Convert a GIF array to one-byte-per-channel."""
    return numpy.minimum(numpy.maximum(arr.round(), 0), 255).astype(numpy.uint8)


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
    return ToUnsignedByte(numpy.dot(img[..., :3], [0.2989, 0.587, 0.144]))


def SaveGIF(gif_array, filename):
    imageio.imwrite(filename, gif_array, format="gif")


def PadGIF2D(gif_array):
    """Pads a 2-D array's rows out to 180.  Returns None if shape is off."""
    if gif_array.shape[1] != 600:
        return None
    if gif_array.shape[0] > 180:
        return None
    out = numpy.full((180, 600), 255, dtype=numpy.uint8)
    missing = 180 - gif_array.shape[0]
    start_row = missing / 2
    end_row = start_row + gif_array.shape[0]
    out[start_row:end_row , :] = gif_array
    return out
