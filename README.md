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

* Load GIFs in B/W, as Numpy arrays
* Save manipulated GIFs
* Histogram GIF sizes
* Standardize GIF size
* Split by panels
* Panel autoencoder via PCA
  * Reconstruction error: min and max
* Predict next column from previous columns
  * Across one panel
  * Across one strip
* Predict final panel from first two panels
