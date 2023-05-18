# intake_warning

This is just an experiment! Things are failing!

## The idea

When an intake catalog is used by a larger community changes to catalog entries need to be communicated. 
Because an email list with all users rarely exists, information needs to be provided in a different manner.

A natural place to include information are the intake catalog entries themselves.
However, writing a deprecation warning into the `description` attribute can easily be overlooked, especially
when the user has written its script and is just reexecuting it. Sometimes the dataset has disappeared from the server
and a new location is unknown. In such a case, intake would through an error that does not contain any information
about why a dataset is not available any more.

The idea of `intake_warning` is to provide a proxy-intake driver that allows the addition of a message and will either
raise a warning and continue opening the dataset or raise an error with the provided message.

```diff
 plugins:
   source:
-    - module: intake_xarray
+    - module: intake_xarray, intake_warning
 
 sources:
   great_dataset:
-    driver: opendap
+    driver: error
     args:
       urlpath: https://observations.ipsl.fr/thredds/dodsC/EUREC4A/PRODUCTS/MERGED-MEASUREMENTS/RADIOSOUNDINGS/v3.0.0/level2/EUREC4A_Atalante_Meteomodem-RS_L2_v3.0.0.nc
+      message: "Unfortunately, this dataset is now longer available. A newer version can be accessed with X.Y.Z"
       auth: null
       chunks: null
       engine: netcdf4
     description: Some dataset
```

When accessing the dataset, the error gets raised:

```ipython
In [3]: cat.great_dataset.to_dask()
---------------------------------------------------------------------------
DatasetError                              Traceback (most recent call last)
Cell In [3], line 1
----> 1 cat.great_dataset.to_dask()

File ~/Documents/GitProjects/intake-warning/intake_warning/error.py:20, in ErrorSource.to_dask(self)
     19 def to_dask(self):
---> 20     raise DatasetError(self.message)

DatasetError: Unfortunately, this dataset is now longer available. A newer version can be accessed with X.Y.Z
```

## Installation
```
pip install git+https://github.com/observingClouds/intake_warning.git
```
