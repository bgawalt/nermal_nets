# Nermal Nets

I have an archive of Garfield comics in GIF format; let's goof around with them.
We can draw new Garfield comics by studying the existing collection, or try
any way.

## Dependencies

Here's the actual PIP commands I ran in my fresh virtual environment:

* `pip install --upgrade pip`
* `pip install numpy`
* `pip install scipy`
* `pip install imageio`

The SciPy was probably premature -- I was planning to use it to read and write
images, but its
[documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imread.html)
now suggests you use [ImageIO](http://imageio.readthedocs.io/en/latest/index.html)
instead.

## TODO

Organizationally, I should probably set up a `scripts/` directory which can link
back to and make use of `nermal_net_lib.py` -- something like
[this](https://docs.python-guide.org/writing/structure/#test-suite).

* Write up image size exploration results
* Build image-size-standardizer
  * Ignore all images that don't have exactly 600 columns
  * Ignore all images with over 180 rows or under 170 rows
  * Pad remaining images with whitespace up to exactly 180 rows, centering image
* Save manipulated GIFs
* Split by panels
* Panel autoencoder via PCA
  * [IncrementalPCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn-decomposition-incrementalpca)
  * Reconstruction error: min and max
* Predict next column from previous columns
  * Across one panel
  * Across one strip
* Predict final panel from first two panels

### Done!

* Load GIFs in B/W, as Numpy arrays
* Histogram GIF sizes
