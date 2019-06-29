import os

#import jwst.datamodels
#import iris_pipeline.datamodels
#
#for class_name in iris_pipeline.datamodels.__all__:
#    jwst.datamodels._defined_models[class_name] = getattr(iris_pipeline.datamodels, class_name)

import iris_pipeline

iris_pipeline.monkeypatch_jwst_datamodels()

from jwst.pipeline import Image2Pipeline
iris_pipeline.pipeline.Image2Pipeline.call("asn_subtract_bg_flat.json", config_file="image2_iris.cfg")
