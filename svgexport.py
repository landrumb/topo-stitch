"""Given a list of lists of points describing isolines, a bounding box, and a filename, writes an SVG file containing the isolines."""

import numpy as np

def write_svg(isolines, bbox, filename):
    """Given a list of lists of points describing isolines, a bounding box, and a filename, writes an SVG file containing the isolines.
    
    Parameters
    ----------
    isolines : list of lists of points
        A list of lists of points describing isolines.
    bbox : list of floats
        A list of floats in the form [xmin, ymin, xmax, ymax].
    filename : str
        The name of the file to write.
    
    Returns
    -------
    None
    
    """
    raise NotImplementedError()