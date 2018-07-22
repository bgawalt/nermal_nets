"""Check out the distribution of image sizes in the comics dataset.

What's here is what comes from a handful of iterations, including trying to
account for the variety of image widths (i.e., num. columns in the image matrix)
before realizing image width was extremely consistent:

```
COL COUNTS:
600 , 14158
604 , 1
```

Overall results: Most comics are between 170 and 180 rows tall, with the overly
tall ones being Sunday strips.

The weirdos -- the 143 comics having between 262 and 275 rows -- all seem to be
Sunday strips from '79 to '81.
"""


import imageio
import nermal_net_lib as nrm
import random


def main():
    random.seed(12345)
    row_counts = {}
    err_count = 0
    small_rows = []
    weirdo_rows = []
    large_rows = []
    for fileid, giffile in enumerate(nrm.GetFilenames("./data/")):
        if fileid % 1000 == 0:
            print "...", fileid, "files"
        img = nrm.LoadGIF(giffile)
        if img is None:
            err_count += 1
            continue
        shp = img.shape
        if len(shp) != 2:
            err_count += 1
            continue
        rc, cc = shp
        row_counts[rc] = row_counts.get(rc, 0) + 1
        if cc != 600:
            # Expect this exactly once:
            print "Weird column count!", cc, ":", giffile
        if rc < 170:
            small_rows.append(giffile)
        if rc > 180:
            large_rows.append(giffile)
        if rc > 250 and rc < 300:
            weirdo_rows.append(giffile)
    print err_count, "Errors"
    print "ROW COUNTS:"
    for k in range(min(row_counts.keys()), max(row_counts.keys()) + 1):
        print k, ",", row_counts.get(k, 0)

    print "TOO FEW ROWS: (", len(small_rows), " total)"
    for fname in random.sample(small_rows, 10):
        print fname
    print "\nTOO MANY ROWS: (", len(large_rows), " total)"
    for fname in random.sample(large_rows, 10):
        print fname
    print "\nWEIRDO MEDIUM ROWS: (", len(weirdo_rows), " total)"
    for fname in random.sample(weirdo_rows, 10):
        print fname




if __name__ == "__main__":
    main()
