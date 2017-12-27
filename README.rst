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

* Source: https://github.com/kuberlytics/kubelaunch

This is a work in progress, but the goal is to make

Installation
------------

.. code-block:: bash

    pip install kubelaunch

Usage
-----
Create a new empty directory for your cluster.

.. code-block:: bash

    kubel init gcp --jupyter

This will create .

Docker Image
-----
This is a Jupyter Singleuser container with Google Cloud Platform and Azure CLI installed.

Build locally:
```
docker build -t kuberlytics/kubelaunch:latest -t kuberlytics/kubelaunch:v0.0.1 .
```
### To use Locally for example.
```
docker run -it --rm -p 8888:8888  -v /Users/<yourpath>/launch:/home/jovyan/work kuberlytics/kubelaunch:latest /bin/bash
```
### Launch a docker container configured to control.
```
docker run -it --rm -p 8888:8888  kuberlytics/kubelaunch:latest /bin/bash
```
