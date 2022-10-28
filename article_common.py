def reduce_nondeterminism():
    import os
    os.environ['TF_CUDNN_DETERMINISTIC']='1'
    import tensorflow as tf
    import random as rn
    import numpy as np
    tf.random.set_seed(42)
    os.environ['PYTHONHASHSEED'] = '0'
    np.random.seed(42)
    rn.seed(42)