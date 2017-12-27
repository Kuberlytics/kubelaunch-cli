============
Kubelaunch
============


.. image:: https://img.shields.io/pypi/v/hugo_jupyter.svg
        :target: https://pypi.python.org/pypi/kubelaunch

.. image:: https://img.shields.io/travis/knowsuchagency/kubelaunch.svg
        :target: https://travis-ci.org/knowsuchagency/kubelaunch

.. image:: https://pyup.io/repos/github/knowsuchagency/kubelaunch/shield.svg
     :target: https://pyup.io/repos/github/knowsuchagency/kubelauch/
     :alt: Updates

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg



Making analytics-ops on Kubernetes easy.

* Documentation: https://kuberlytics.github.io/kubelaunch
* Source: https://github.com/kuberlytics/kubelaunch


Installation
------------

.. code-block:: bash

    pip install kubelaunch

Usage
-----

.. code-block:: bash

    kubel new-site

This will create a directory locally if it doesn't exist and initialize a config file.

Docker Image
-----
This is a Jupyter Singleuser container with Google Cloud Platform and Azure CLI installed.

Build locally:
```
docker build -t kuberlytics/kubelaunch:latest -t kuberlytics/kubelaunch:v0.0.1 .
```
### To use Locally for example.
```
docker run -it --rm -p 8888:8888  -v /Users/<yourpath>/launch:/home/jovyan/launch --user root -e GRANT_SUDO=yes kuberlytics/kubelaunch:latest
```
### To simulate online version without local sharing of volume.
```
docker run -it --rm -p 8888:8888  --user root -e GRANT_SUDO=yes kuberlytics/launch:latest
```
