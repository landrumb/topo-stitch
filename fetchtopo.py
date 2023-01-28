"""takes coordinates of a bounding box and returns a topographical map of the area in the form of a numpy array"""
import numpy as np

"""Given a bounding box, returns a numpy array of elevation data"""

import numpy as np
import requests

def fetch_topo(bbox):
    """Given a bounding box, returns a numpy array of elevation data.

    Parameters
    ----------
    bbox : list of floats
        A list of floats in the form [xmin, ymin, xmax, ymax].

    Returns
    -------
    numpy array
        A numpy array of elevation data.

    """
    raise NotImplementedError()