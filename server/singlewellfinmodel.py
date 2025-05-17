import numpy as np
import pandas as pd
import json
from dateutil.relativedelta import relativedelta
import datetime

from app import app
from models import Well, Assumptions, ProductionCurve, Project, Pricing


def get_typecurve(id):
    """
    Get the type curve for a given well ID.
    """

    well_to_get = Well.query.filter_by(id=id).first()
    well_to_dict = well_to_get.to_dict()
    type_curve = well_to_dict['production_curve']['type_curve']

    type_curve_data = json.loads(type_curve)
    type_curve_df = pd.DataFrame(type_curve_data)

    # covert the 'Date' column to datetime
    production_start_date = datetime.datetime.strptime(
        well_to_dict['assumptions']['prod_start_date'], "%Y-%m-%d"
    )

    number_of_rows = len(type_curve_df)

    # Create a list of dates incremented by one month for each entry
    dates = pd.date_range(start=production_start_date, periods=number_of_rows, freq='MS')
    type_curve_df.insert(0, "Date", dates.strftime("%m/%d/%Y"))

    # month number of the date
    # year number of the date

    type_curve_df.insert(1, "Month_Number", dates.month)
    type_curve_df.insert(2, "Year_Number", dates.year)

    # fixing the formatting of production figures
    type_curve_df.iloc[:,-2] = type_curve_df.iloc[:,-2].str.replace(',', '').astype(float)
    type_curve_df.iloc[:,-1] = type_curve_df.iloc[:,-1].str.replace(',', '').astype(float)

    return type_curve_df


def working_interest(id):
    """
    Get the working interest for a given well ID.
    """

    assumptions_to_get = Assumptions.query.filter_by(id=id).first()
    assumptions_to_dict = assumptions_to_get.to_dict()
    working_interest_before = assumptions_to_dict['wi_before_payout']
    working_interest_after = assumptions_to_dict['wi_after_payout']
    net_working_interest_before = assumptions_to_dict['nri_before_payout']
    net_working_interest_after = assumptions_to_dict['nri_after_payout']


    return working_interest_before, working_interest_after, net_working_interest_before, net_working_interest_after


with app.app_context():   
        print(working_interest(1))

