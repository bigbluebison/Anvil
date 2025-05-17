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

    well_to_get = (Well.query.filter_by(id=id).first()).to_dict()
    assumptions = well_to_get['assumptions']

    working_interest_before = assumptions['wi_before_payout']
    working_interest_after = assumptions['wi_after_payout']
    net_working_interest_before = assumptions['nri_before_payout']
    net_working_interest_after = assumptions['nri_after_payout']


    return working_interest_before, working_interest_after, net_working_interest_before, net_working_interest_after

def gas_concentrations(id):
    """
    Get the gas concentrations for a given well ID.
    """

    well_to_get = (Well.query.filter_by(id=id).first()).to_dict()
    gas_concentrations = well_to_get['assumptions']['gas_concentrations']
    gas_concentrations = json.loads(gas_concentrations)


    methane =  gas_concentrations["methane"]
    ethane =  gas_concentrations["ethane"]
    propane =  gas_concentrations["propane"]
    i_butane  = gas_concentrations["i-butane"]
    n_butane = gas_concentrations["n-butane"]
    i_pentane = gas_concentrations["i-pentane"]
    n_pentane = gas_concentrations["n-pentane"]
    hexane_plus = gas_concentrations["hexane+"]
    helium = gas_concentrations["helium"]

    # return gas_concentration
    return methane, ethane, propane, i_butane, n_butane, i_pentane, n_pentane, hexane_plus, helium

def calc_productions(id):

    type_curve_df = get_typecurve(id)
    methane, ethane, propane, i_butane, n_butane, i_pentane, n_pentane, hexane_plus, helium = gas_concentrations(id)

    # type_curve_df['total_oil_production (Mbbl)'] = type_curve_df['Total Oil Production (bbl)'].astype(float)

    pass


with app.app_context():   
        print(get_typecurve(1))

