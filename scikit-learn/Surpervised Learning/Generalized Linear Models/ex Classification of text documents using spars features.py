"""
This is an example showing how scikit-learn
can be used to classify documents by topics
using a bag-of-words approach. This example
uses a scipy.sparse matrix to store the
features and demonstrates various classifiers
that can efficiently handle sparse matrices.
"""

from __future__ import print_function

import logging
import numpy as np
from optparse import OptionParser
import sys
from time import time
import matplotlib.pyplot as plt
