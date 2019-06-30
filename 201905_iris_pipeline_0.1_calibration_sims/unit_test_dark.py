import numpy as np

import iris_pipeline

darksub= iris_pipeline.datamodels.IRISImageModel( "raw_science_frame_sci_dark_current.fits")
dark=iris_pipeline.datamodels.IRISImageModel("/home/azonca/crds_cache/references/tmt/iris/tmt_iris_dark_0001.fits")
dark
orig=iris_pipeline.datamodels.IRISImageModel("v2/raw_science_frame_sci.fits")
np.testing.assert_allclose(darksub.data, orig.data-dark.data)
