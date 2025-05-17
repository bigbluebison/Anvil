import numpy as np
import pandas as pd



def get_typecurve(id):
    """
    Get the type curve for a given well ID.
    """

    well_to_get = Well.query.filter_by(id=id).first()
    well_to_dict = well_to_get.to_dict()

    return well_to_dict

print(get_typecurve(1))

