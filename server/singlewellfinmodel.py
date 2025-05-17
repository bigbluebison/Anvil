import numpy as np
import pandas as pd
import json
from dateutil.relativedelta import relativedelta


from app import app
from models import Well


def get_typecurve(id):
    """
    Get the type curve for a given well ID.
    """

    well_to_get = Well.query.filter_by(id=id).first()
    well_to_dict = well_to_get.to_dict()
    type_curve = well_to_dict['production_curve']['type_curve']

    type_curve_data = json.loads(type_curve)
    type_curve_df = pd.DataFrame(type_curve_data)

    production_start_date = well_to_dict['assumptions']['prod_start_date']

    number_of_rows = len(type_curve_df)

    # Create a list of dates incremented by one month for each entry
    dates = [(production_start_date + relativedelta(months=+i)).strftime("%m/%d/%Y") for i in range(number_of_rows)]
    type_curve_df.insert(0, "Date", dates)


    return type_curve_df




with app.app_context():   
        print(get_typecurve(1))

