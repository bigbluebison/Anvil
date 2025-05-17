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

def refinery_efficiencies(id):
    """
    Get the refinery efficiencies for a given well ID.
    """

    well_to_get = (Well.query.filter_by(id=id).first()).to_dict()
    refinery_efficiencies = well_to_get['assumptions']['refinery_assumptions']
    refinery_efficiencies = json.loads(refinery_efficiencies)

    ethane_efficiency =  refinery_efficiencies["ethane_efficiency"]
    propane_efficiency =  refinery_efficiencies["propane_efficiency"]
    i_butane_efficiency  = refinery_efficiencies["ibutane_efficiency"]
    n_butane_efficiency = refinery_efficiencies["nbutane_efficiency"]
    i_pentane_efficiency = refinery_efficiencies["ipentane_efficiency"]
    n_pentane_efficiency = refinery_efficiencies["npentane_efficiency"]
    hexane_plus_efficiency = refinery_efficiencies["hexaneplus_efficiency"]
    helium_efficiency = refinery_efficiencies["helium_efficiency"]
  
    return ethane_efficiency, propane_efficiency, i_butane_efficiency, n_butane_efficiency, i_pentane_efficiency, n_pentane_efficiency, hexane_plus_efficiency, helium_efficiency

    # return refinery_efficiencies

def calc_productions(id):

    type_curve_df = get_typecurve(id)
    methane, ethane, propane, i_butane, n_butane, i_pentane, n_pentane, hexane_plus, helium = gas_concentrations(id)
    ethane_efficiency, propane_efficiency, i_butane_efficiency, n_butane_efficiency, i_pentane_efficiency, n_pentane_efficiency, hexane_plus_efficiency, helium_efficiency = refinery_efficiencies(id)
    
    # Gallons per Mcf factor 
    ethane_factor = 26.745
    propane_factor = 27.555
    i_butane_factor = 32.714
    n_butane_factor = 31.529
    i_pentane_factor = 36.606
    n_pentane_factor = 36.219
    hexane_plus_factor = 43.295

    # Total oil production
    type_curve_df['Total_Oil_Production (Mbbl)'] = type_curve_df['Oil_Production (Bbl)']/(1000.0)

    # Total nat gas production
    type_curve_df['Methane (MMcf)'] = type_curve_df['Total_Gas_Production (Mcf)']*(methane)/(1000.0)

    # Total ethane production
    type_curve_df['Ethane (Mgal)'] = type_curve_df['Total_Gas_Production (Mcf)']*(ethane)*(ethane_factor)*(ethane_efficiency)/(1000.0)

    # Total propane production
    type_curve_df['Propane (Mgal)'] = type_curve_df['Total_Gas_Production (Mcf)']*(propane)*(propane_factor)*(propane_efficiency)/(1000.0)
    # Total i-butane production
    type_curve_df['i-Butane (Mgal)'] = type_curve_df['Total_Gas_Production (Mcf)']*(i_butane)*(i_butane_factor)*(i_butane_efficiency)/(1000.0)
    # Total n-butane production
    type_curve_df['n-Butane (Mgal)'] = type_curve_df['Total_Gas_Production (Mcf)']*(n_butane)*(n_butane_factor)*(n_butane_efficiency)/(1000.0)
    # Total i-pentane production
    type_curve_df['i-Pentane (Mgal)'] = type_curve_df['Total_Gas_Production (Mcf)']*(i_pentane)*(i_pentane_factor)*(i_pentane_efficiency)/(1000.0)
    # Total n-pentane production
    type_curve_df['n-Pentane (Mgal)'] = type_curve_df['Total_Gas_Production (Mcf)']*(n_pentane)*(n_pentane_factor)*(n_pentane_efficiency)/(1000.0)
    # Total hexane+ production
    type_curve_df['Hexane+ (Mgal)'] = type_curve_df['Total_Gas_Production (Mcf)']*(hexane_plus)*(hexane_plus_factor)*(hexane_plus_efficiency)/(1000.0)
    # Total helium production
    type_curve_df['Helium (Mcf)'] = type_curve_df['Total_Gas_Production (Mcf)']*(helium)/(1000.0)


    return type_curve_df


with app.app_context():   
        print(calc_productions(1))

