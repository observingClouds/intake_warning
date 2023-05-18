from intake.source.base import DataSource
import intake
import warnings

class DatasetError(Exception):
	pass

class ErrorSource(DataSource):
    name = 'error'

    def __init__(self, urlpath, message=None, metadata=None, **kwargs):
        self.urlpath = urlpath
        self.metadata = metadata or {}
        self.message = message
        self.kwargs = kwargs
        self._ds = None

    def _load_metadata(self):
        raise DatasetError(self.message)

    def to_dask(self):
        raise DatasetError(self.message)

class WarningSource(DataSource):
    name = 'warning'

    def __init__(self, data_driver, message=None, metadata={}, **kwargs):
        import pdb;pdb.set_trace()
        super(intake.registry.drivers.registered[data_driver], self).__init__(metadata=metadata, **kwargs)
        self.message = message

    def to_dask(self):
        warnings.warn(self.message)
        super(self.data_driver, self).to_dask()        
