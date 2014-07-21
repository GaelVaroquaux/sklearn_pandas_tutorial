EuroPython 2014 Scikit-learn Tutorial
=======================================

This repository contains files and other info associated with the
EuroPython 2014 scikit-learn tutorial.

**Instructor**: Gael Varoquaux
[@GaelVaroquaux](https://twitter.com/GaelVaroquaux) |
http://gael-varoquaux.info

Installation Notes
------------------

This tutorial will require recent installations of *numpy*, *scipy*,
*matplotlib*, *scikit-learn*.

For users who do not yet have these  packages installed, a relatively
painless way to install all the requirements is to use a package such as
[Anaconda CE](http://store.continuum.io/ "Anaconda CE"), which can be
downloaded and installed for free.

Reading the training materials
-------------------------------

**Not all the material will be covered at the EuroPython training**:
there is not enough time available. However, you can follow the material
by yourself.


### With the IPython notebook

The recommended way to access the materials is to execute them in the
IPython notebook. If you have the IPython notebook installed, you should
download the materials (see below), go the the `notebooks` directory, and
type:

    ipython notebook

in your terminal window. This will open a notebook panel load in your web
browser.

### On Internet

If you don't have the IPython notebook installed, you can browse the
files on Internet:

* For the instructions without the solutions:

  http://nbviewer.ipython.org/github/GaelVaroquaux/sklearn_europython_2014/tree/master/notebooks/

* For the instructions and the solutions:

  http://nbviewer.ipython.org/github/GaelVaroquaux/sklearn_europython_2014/tree/master/rendered_notebooks/

Downloading the Tutorial Materials
----------------------------------

I would highly recommend using git, not only for this tutorial, but for the
general betterment of your life.  Once git is installed, you can clone the
material in this tutorial by using the git address shown above:

If you can't or don't want to install git, there is a link above to download
the contents of this repository as a zip file.  I may make minor changes to
the repository in the days before the tutorial, however, so cloning the
repository is a much better option.

Data Downloads
--------------

The data for this tutorial is not included in the repository.  We will be
using several data sets during the tutorial: most are built-in to
scikit-learn, which includes code which automatically downloads and
caches these data.  Because the wireless network at conferences can often
be spotty, it would be a good idea to download these data sets before
arriving at the conference. You can do so by using the `fetch_data.py`
included in the tutorial materials. 

Original material from the Scipy 2013 tutorial
----------------------------------------------

This material is adapted from the scipy 2013 tutorial:

    http://github.com/jakevdp/sklearn_scipy2013

Original authors:

- Gael Varoquaux [@GaelVaroquaux](https://twitter.com/GaelVaroquaux) | http://gael-varoquaux.info
- Olivier Grisel [@ogrisel](https://twitter.com/ogrisel) | http://ogrisel.com
- Jake VanderPlas [@jakevdp](https://twitter.com/jakevdp) | http://jakevdp.github.com



