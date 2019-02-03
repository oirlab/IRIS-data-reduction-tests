import os
os.environ["CRDS_PATH"]="crds_cache"
os.environ["CRDS_CONTEXT"]="tmt_0001.pmap"
os.environ["CRDS_SERVER_URL"]="https://crds-serverless-mode.stsci.edu"

from jwst.pipeline import Image2Pipeline
from iris_pipeline.pipeline import Image2Pipeline
Image2Pipeline.call("asn_subtract_bg_flat.json", config_file="image2_iris.cfg")
