import tensorflow as tf
from tensorflow.python.training import checkpoint_utils as cp

x= cp.list_variables('"E:\ATSC\\reinf_traf_control_0.data-00000-of-00001"')
##y= cp.load_variable('/tmp/tensorflow/mnist/logs/fully_connected_feed/model.ckpt-1999', 'hidden1/biases')