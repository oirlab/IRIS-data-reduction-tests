import os

from jwst.pipeline import Image2Pipeline
from iris_pipeline.pipeline import Image2Pipeline
Image2Pipeline.call("asn_subtract_bg_flat.json", config_file="image2_iris.cfg")
