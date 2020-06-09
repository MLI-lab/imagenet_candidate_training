# Flickr Image Recognition

This repository provides code for reproducing the figures in the paper:

**"Image recognition from noisy labels collected without annotators"**, by Fatih Furkan Yilmaz and Reinhard Heckel.

# Downloading the dataset
The original ImageNet dataset can be downloaded from the official source given by [ILSVRC2012](http://www.image-net.org/challenges/LSVRC/2012/) or by using the [Kaggle mirror](https://www.kaggle.com/c/imagenet-object-localization-challenge/data).

The Flickr candidate dataset is currently not hosted online due to size constraints, however can be re-constructed by providing [this file](metadata/tiny_classes_to_search.json) as the positional argument to the [code for searching and downloading Flickr images](https://www.dropbox.com/s/6pp1z7zaogsyith/flickr_image_search.zip?dl=0).

# Training on the candidate dataset
While the results in the paper can be reproduced by the included log files, they can also be reproduced by training on the candidate dataset with a wide range of hyperparameters. 

In order to train on either the candidate dataset constructed from Flickr or the original ImageNet, the training script can be run with the following parameters:

- *root*: root directory (`pathlib`) where the training set is stored.
- *main*: name of the folder where either the original ImageNet training set or the candidate dataset is stored.
- *test*: name of the folder where the ImageNet validation set is stored.

The rest of the available CLI parameters can be queried by running `python train.py --help`.

It is also possible to train the model with the *same exact setup* used in generating the figures in the paper by using the provided configuration files. For example, the results of the main figure for the candidate dataset can be reproduced from scratch simply by running:

```bash
python train.py --config "./results/flickr_cls100/config.json"
```

# Visualizing training results
The code for plotting the training results from the log files is given in the `visualize_train_logs` notebook.

This notebook contains the code for reproducing Figure 2 and Figure 7 (Appendix) from the paper.

# Error Analysis
The code for the analysis of the test classification error for the 135-class problem is given in the `error_analysis` notebook.

This notebook contains the code for reproducing Figure 5-a, 5-b and Figure 8 (Appendix) from the paper.

## Source codes
Acknowledgements for PyTorch implementation is as follows:

**Training code**
- The code for training has been incorporated and modified from the _official_ PyTorch examples repository [https://github.com/pytorch/examples/...](https://github.com/pytorch/examples/tree/master/imagenet). The default hyperparameters has been used for fair experiments and comparison. Some additional details have been inspired from the [pytorch-image-models repository](https://github.com/rwightman/pytorch-image-models).