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
    net_revenue_interest_before = assumptions['nri_before_payout']
    net_revenue_interest_after = assumptions['nri_after_payout']

    return working_interest_before, working_interest_after, net_revenue_interest_before, net_revenue_interest_after


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


def calc_net_productions(id):
    """
    Calculate the net productions for a given well ID.
    """

    type_curve_df = calc_productions(id)
    working_interest_before, working_interest_after, net_revenue_interest_before, net_revenue_interest_after = working_interest(id)

    # Working interest
    type_curve_df['Working_Interest'] = working_interest_before 
    # Net Revenue Interest 
    type_curve_df['Net_Revenue_Interest'] = net_revenue_interest_before 


    # Net oil production
    type_curve_df['Net_Oil_Production (Mbbl)'] = type_curve_df['Total_Oil_Production (Mbbl)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']

    # Net nat gas production
    type_curve_df['Net_Methane (MMcf)'] = type_curve_df['Methane (MMcf)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']

    # Net ethane production
    type_curve_df['Net_Ethane (Mgal)'] = type_curve_df['Ethane (Mgal)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']

    # Net propane production
    type_curve_df['Net_Propane (Mgal)'] = type_curve_df['Propane (Mgal)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']
    
    # Net i-butane production
    type_curve_df['Net_i-Butane (Mgal)'] = type_curve_df['i-Butane (Mgal)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']
    
    # Net n-butane production
    type_curve_df['Net_n-Butane (Mgal)'] = type_curve_df['n-Butane (Mgal)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']
    
    # Net i-pentane production
    type_curve_df['Net_i-Pentane (Mgal)'] = type_curve_df['i-Pentane (Mgal)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']
    
    # Net n-pentane production
    type_curve_df['Net_n-Pentane (Mgal)'] = type_curve_df['n-Pentane (Mgal)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']
    
    # Net hexane+ production
    type_curve_df['Net_Hexane+ (Mgal)'] = type_curve_df['Hexane+ (Mgal)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']
    
    # Net helium production
    type_curve_df['Net_Helium (Mcf)'] = type_curve_df['Helium (Mcf)']*type_curve_df['Working_Interest']*type_curve_df['Net_Revenue_Interest']

    return type_curve_df


def get_pricing(id):
    """
    Get the pricing for a given well ID.
    """
    
    prices = Pricing.query.filter_by(id=id).first().to_dict()

    oil_price = prices['oil_price']
    methane_price = prices['methane_price']
    ethane_price = prices['ethane_price']
    propane_price = prices['propane_price']
    i_butane_price = prices['i_butane_price']
    n_butane_price = prices['n_butane_price']
    i_pentane_price = prices['i_pentane_price']
    n_pentane_price = prices['n_pentane_price']
    hexane_plus_price = prices['hexane_plus_price']
    helium_price = prices['helium_price']

    return oil_price, methane_price, ethane_price, propane_price, i_butane_price, n_butane_price, i_pentane_price, n_pentane_price, hexane_plus_price, helium_price


def production_cost_assumptions(id):
    '''
    Get the well related production cost assumptions for a given well ID.
    '''
    well_to_get = (Well.query.filter_by(id=id).first()).to_dict()
    assumptions = well_to_get['assumptions']

    primary_pipeline_fee = assumptions['primary_pipeline_fee']
    secondary_pipeline_fee = assumptions['secondary_pipeline_fee']  
    inlet_gas_fee = assumptions['inlet_gas_fee']

    methane_processor_share = assumptions['nat_gas_processor_share']
    helium_processor_share = assumptions['helium_processor_share']
    ngl_processor_share = assumptions['ngl_processor_share']   

    return primary_pipeline_fee, secondary_pipeline_fee, inlet_gas_fee, methane_processor_share, helium_processor_share, ngl_processor_share


def calc_net_revenues(id):
    '''
    calculate the net revenues for a given well ID
    '''
    type_curve_df = calc_net_productions(id)
    oil_price, methane_price, ethane_price, propane_price, i_butane_price, n_butane_price, i_pentane_price, n_pentane_price, hexane_plus_price, helium_price = get_pricing(id)
    primary_pipeline_fee, secondary_pipeline_fee, inlet_gas_fee, methane_processor_share, helium_processor_share, ngl_processor_share = production_cost_assumptions(id)

    # Net oil revenues
    type_curve_df['Net_Oil_Revenues'] = type_curve_df['Net_Oil_Production (Mbbl)']*(oil_price)
    # Net nat gas revenues
    type_curve_df['Net_Methane_Revenues'] = type_curve_df['Net_Methane (MMcf)']*(methane_price)
    # Net ethane revenues
    type_curve_df['Net_Ethane_Revenues'] = type_curve_df['Net_Ethane (Mgal)']*(ethane_price)
    # Net propane revenues
    type_curve_df['Net_Propane_Revenues'] = type_curve_df['Net_Propane (Mgal)']*(propane_price)
    # Net i-butane revenues
    type_curve_df['Net_i-Butane_Revenues'] = type_curve_df['Net_i-Butane (Mgal)']*(i_butane_price)
    # Net n-butane revenues
    type_curve_df['Net_n-Butane_Revenues'] = type_curve_df['Net_n-Butane (Mgal)']*(n_butane_price)
    # Net i-pentane revenues
    type_curve_df['Net_i-Pentane_Revenues'] = type_curve_df['Net_i-Pentane (Mgal)']*(i_pentane_price)
    # Net n-pentane revenues
    type_curve_df['Net_n-Pentane_Revenues'] = type_curve_df['Net_n-Pentane (Mgal)']*(n_pentane_price)
    # Net hexane+ revenues
    type_curve_df['Net_Hexane+_Revenues'] = type_curve_df['Net_Hexane+ (Mgal)']*(hexane_plus_price)
    # Net helium revenues
    type_curve_df['Net_Helium_Revenues'] = type_curve_df['Net_Helium (Mcf)']*(helium_price)
    
    # Production cost assumptions
    # Certain cost items in energy wells are usually deducted before net revenues are calculated

    type_curve_df['Gathering_And_Transportation_Fees'] =  (type_curve_df['Total_Gas_Production (Mcf)'] * type_curve_df['Working_Interest'] * (primary_pipeline_fee + secondary_pipeline_fee)) /1000
    type_curve_df['Gas_Processing_Fees'] =  (type_curve_df['Total_Gas_Production (Mcf)'] * type_curve_df['Working_Interest'] * (inlet_gas_fee)) /1000
    
    type_curve_df['Methane_Sharing_Cost'] =  (type_curve_df['Net_Methane_Revenues'] * (methane_processor_share)) 
    
    type_curve_df['Ngl_Sharing_Cost'] =  (
        (
        type_curve_df['Net_Ethane_Revenues']
        + type_curve_df['Net_Propane_Revenues']
        + type_curve_df['Net_i-Butane_Revenues']
        + type_curve_df['Net_n-Butane_Revenues']
        + type_curve_df['Net_i-Pentane_Revenues']
        + type_curve_df['Net_n-Pentane_Revenues']
        + type_curve_df['Net_Hexane+_Revenues']
    )  *  (ngl_processor_share))
    
    type_curve_df['Helium_Sharing_Cost'] =  (type_curve_df['Net_Helium_Revenues'] * (helium_processor_share))


    # Total revenues
    # Total revenues to the interest owner
    type_curve_df['Total_Net_Revenues'] = (
        type_curve_df['Net_Oil_Revenues'] 
        + type_curve_df['Net_Methane_Revenues'] 
        + type_curve_df['Net_Ethane_Revenues'] 
        + type_curve_df['Net_Propane_Revenues'] 
        + type_curve_df['Net_i-Butane_Revenues'] 
        + type_curve_df['Net_n-Butane_Revenues'] 
        + type_curve_df['Net_i-Pentane_Revenues'] 
        + type_curve_df['Net_n-Pentane_Revenues'] 
        + type_curve_df['Net_Hexane+_Revenues'] 
        + type_curve_df['Net_Helium_Revenues']
        - type_curve_df['Gathering_And_Transportation_Fees']
        - type_curve_df['Gas_Processing_Fees']
        - type_curve_df['Methane_Sharing_Cost']
        - type_curve_df['Ngl_Sharing_Cost']
        - type_curve_df['Helium_Sharing_Cost']
        )
    
    return type_curve_df



with app.app_context():   
        # print(calc_net_productions(1))
        # print(get_pricing(1))
        print(calc_net_revenues(1))

