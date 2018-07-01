import os


def GetFilenames(data_dir):
    """Get filenames for Garfield comics in .gif format.

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


def main():
    print GetFilenames("./data/")


if __name__ == "__main__":
    main()
