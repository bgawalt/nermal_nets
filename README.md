# Nermal Nets

I'm gonna try and predict the pixel values of Garfield comics.

(I'm not sharing *how* I got the Garfield comics I used for training data,
but I did get 'em, all the decades and decades worth.)

Things I can try that spring to mind:

1. Autoencoder for panels, to generate new panels
2. Predict final panel pixels given the opening two panels
3. Predict the next column of pixels given the preceding `k` columns
