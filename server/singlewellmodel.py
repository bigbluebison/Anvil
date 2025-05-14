
# Sample Type Curve Generator
# Create type curves for the model

import numpy as np
import pandas as pd

# seed for consistency for this project
np.random.seed(999)

num_months = 120

months = [i for i in range(num_months)]

# oil productiom monthly
# bbls per month

oil_base = 1000
oil_decline = 35

oil_prod = [oil_base]
for i in range(num_months-1):
    if oil_prod[-1] > 0:
        decline_noise = np.random.uniform(0.78,1)
        curr_prod = oil_base - round((oil_decline*i*decline_noise),0)
    else:
        curr_prod = 0
    oil_prod.append(curr_prod)

gas_base = 8500
gas_decline = 50

# gas production per month
# mcf per month 

gas_prod = [gas_base]
for i in range(num_months-1):
    if gas_prod[-1] > 0:
        decline_noise = np.random.uniform(0.85,1)
        curr_prod = gas_base - round((gas_decline*decline_noise*i),0)
    else:
        curr_prod = 0
    gas_prod.append(curr_prod)

type_curve = {
    "months":months,
    "oil":oil_prod,
    "gas":gas_prod
}

typecurve_df = pd.DataFrame(type_curve)

# Net Revenue Interest and Working Interest Assumptions

# Net revenue interests before and after payout (%)
nri_before_payout = 0.83
nri_after_payout = 0.83

# Working interest before and after payout (%)
wi_before_payout = 1.00
wi_after_payout = 1.00

# Direct Pricing Deductions 

# oil price deduct per barrel ($/barrel)
oil_price_deduct = 3.50

# natural gas deduct ($/mcf)
gas_price_deduct = 0.25

# gas liquids price deduct (%)
ngl_price_deduct = 0.10

# gas transportation assumptions ($/mcf)
primary_pipeline_fee = 0.30
secondary_pipeline_fee = 0.10

# Gas Processing Cost Assumptions

# refinery transportation and fractiation costs
# inlet gas ($/mcf)
inlet_gas_fee = 0.25
# natural gas liquids ($/gal)
ngl_fee =  0.10

# additional revenue sharing/POP (%)
nat_gas_processor_share = 0.10
ngl_processor_share = 0.10
helium_processor_share = 0.10

# Operating Expenses 

# Production well opex ($000/Well/Mo)
pumping_services = 0.5
other_contractors = 1.0
electricity = 5.0
misc = 1.0

# Disposal well opex ($000/Well/Mo)
pumping_services = 0.5
other_contractors = 3.0
electricity = 5.0
misc = 1.0

# Production Taxes

severance_tax = 0.06

# monthly average assumption
ad_valorem_tax = 0.00

#Capital Expenditures

#Production well capex ($000)
#Disposal well capex ($000)

capex_assumptions = {
    "production_well": {
        "land_acquisition": 15,      # $000
        "drilling": 197,
        "completion": 80,
        "facilities": 34,
        "contingency": 71,
        "pipeline": 44,
        "plug_abandon_bond": 20
    },
    "disposal_well": {
        "land_acquisition": 15,      # $000
        "drilling": 313,
        "completion": 122,
        "facilities": 42,
        "contingency": 86,
        "pipeline": 30,
        "plug_abandon_bond": 20
    }
}

# Gas concentration and Refining 

# Pipeline loss and shrinkage
## ADD PIPELINE LOSS AND SHRINKAGE LATER

# Gas concentration assumptions (% molar concentrations)
methane_conc    = 0.5366
ethane_conc     = 0.0493
propane_conc    = 0.0319
ibutane_conc    = 0.0048
nbutane_conc    = 0.0101
ipentane_conc   = 0.0018
npentane_conc   = 0.0025
hexaneplus_conc = 0.0019
helium_conc     = 0.0082

# Compute the remainder fraction as "other"
other = 1 - (
    methane_conc 
  + ethane_conc 
  + propane_conc 
  + ibutane_conc 
  + nbutane_conc 
  + ipentane_conc 
  + npentane_conc 
  + hexaneplus_conc 
  + helium_conc
)

# Consolidate into a single dictionary
gas_concentrations = {
    'methane'     : methane_conc,
    'ethane'      : ethane_conc,
    'propane'     : propane_conc,
    'i-butane'    : ibutane_conc,
    'n-butane'    : nbutane_conc,
    'i-pentane'   : ipentane_conc,
    'n-pentane'   : npentane_conc,
    'hexane+'     : hexaneplus_conc,
    'helium'      : helium_conc,
    'other'       : other
}

# Check that the fractions sum to 1
# !! COME BACK HERE

# Refinery Assumptions (%)
ethane_efficiency = 0.99
propane_efficiency = 0.99
ibutane_efficiency = 0.98
nbutane_efficiency = 0.98
ipentane_efficiency = 0.97
npentane_efficiency = 0.97
hexaneplus_efficiency = 0.96
helium_efficiency = 0.99

# Factor (14.73 PB)  
ethane_factor = 26.745
propane_factor = 27.555
ibutane_factor = 32.714
nbutane_factor = 31.529
ipentane_factor = 36.606
npentane_factor = 36.219
hexaneplus_factor = 43.295

gas_stream_assump = {
    'methane': {
        'concentration': methane_conc,
        'efficiency'   : '',
        'factor'       : ''
    },
    'ethane': {
        'concentration': ethane_conc,
        'efficiency'   : ethane_efficiency,
        'factor'       : ethane_factor
    },
    'propane': {
        'concentration': propane_conc,
        'efficiency'   : propane_efficiency,
        'factor'       : propane_factor
    },
    'i-butane': {
        'concentration': ibutane_conc,
        'efficiency'   : ibutane_efficiency,
        'factor'       : ibutane_factor
    },
    'n-butane': {
        'concentration': nbutane_conc,
        'efficiency'   : nbutane_efficiency,
        'factor'       : nbutane_factor
    },
    'i-pentane': {
        'concentration': ipentane_conc,
        'efficiency'   : ipentane_efficiency,
        'factor'       : ipentane_factor
    },
    'n-pentane': {
        'concentration': npentane_conc,
        'efficiency'   : npentane_efficiency,
        'factor'       : npentane_factor
    },
    'hexane+': {
        'concentration': hexaneplus_conc,
        'efficiency'   : hexaneplus_efficiency,
        'factor'       : hexaneplus_factor
    },
    'helium': {
        'concentration': helium_conc,
        'efficiency'   : helium_efficiency,
        'factor'       : ''
    }
}

# Including pricing
# Assuming simple stable pricing

oil_price = 50.0
methane_price = 2.50
helium_price = 200.00
ethane_price = 0.25
propane_price = 0.81
ibutane_price = 1.40
nbutane_price = 1.40
ipentane_price = 1.45
npentane_price = 1.45
hexaneplus_price = 1.60

# Refinery NGL production Calculations

def gpm_calc(factor, concentration):
    gallons_per_mcf = (factor) * (concentration)  
    return gallons_per_mcf 

# Start date
start_date = '08-01-2025'

num_months = len(months)

cal_dates = pd.date_range(start_date, periods=num_months, freq='MS').strftime('%m-%d-%Y').tolist()

# Single Well Model

# Adding calendar dates and rearranging columns
typecurve_df['date'] = cal_dates
typecurve_df = typecurve_df[['date', 'months', 'oil', 'gas']]

# Production calculations
# Calculating sub components of the production

# oil production (MBbl/mo)
typecurve_df['oil_prod'] = typecurve_df['oil'] /1000  

# methane production (MMcf/mo)
typecurve_df['methane_prod'] = typecurve_df['gas'] /1000 * gas_stream_assump['methane']['concentration'] 

# helium production (MMcf/mo)
typecurve_df['helium_prod'] = typecurve_df['gas'] /1000 * gas_stream_assump['helium']['concentration'] * gas_stream_assump['helium']['efficiency']  

# NGLs production
# ethane production (MGals)
typecurve_df['ethane_prod'] = typecurve_df['gas'] /1000 * (gpm_calc(gas_stream_assump['ethane']['factor'], gas_stream_assump['ethane']['concentration']) ) * gas_stream_assump['ethane']['efficiency']

# propane production (MGals)
typecurve_df['propane_prod'] = typecurve_df['gas'] /1000 * (gpm_calc(gas_stream_assump['propane']['factor'], gas_stream_assump['propane']['concentration']) ) * gas_stream_assump['propane']['efficiency']

# ibutane production (MGals)
typecurve_df['ibutane_prod'] = typecurve_df['gas'] /1000 * (gpm_calc(gas_stream_assump['i-butane']['factor'], gas_stream_assump['i-butane']['concentration']) ) * gas_stream_assump['i-butane']['efficiency']

# nbutane production (MGals)
typecurve_df['nbutane_prod'] = typecurve_df['gas'] /1000 * (gpm_calc(gas_stream_assump['n-butane']['factor'], gas_stream_assump['n-butane']['concentration']) ) * gas_stream_assump['n-butane']['efficiency']

# ipentane production (MGals)
typecurve_df['ipentane_prod'] = typecurve_df['gas'] /1000 * (gpm_calc(gas_stream_assump['i-pentane']['factor'], gas_stream_assump['i-pentane']['concentration']) ) * gas_stream_assump['i-pentane']['efficiency']

# ipentane production (MGals)
typecurve_df['npentane_prod'] = typecurve_df['gas'] /1000 * (gpm_calc(gas_stream_assump['n-pentane']['factor'], gas_stream_assump['n-pentane']['concentration']) ) * gas_stream_assump['n-pentane']['efficiency']

# hexaneplus production (MGals)
typecurve_df['hexaneplus_prod'] = typecurve_df['gas'] /1000 * (gpm_calc(gas_stream_assump['hexane+']['factor'], gas_stream_assump['hexane+']['concentration']) ) * gas_stream_assump['hexane+']['efficiency']

# Integrating Net Revenue Interest and Working Interests into Production

typecurve_df['nri'] = nri_before_payout 
typecurve_df['wi'] = wi_before_payout

# Calculating Net Production Volumes

df = typecurve_df

df['net_oil'] = df['oil_prod'] * df['nri'] * df['wi']

df['net_methane'] = df['methane_prod'] * df['nri'] * df['wi']
df['net_helium'] = df['helium_prod'] * df['nri'] * df['wi']
df['net_ethane'] = df['ethane_prod'] * df['nri'] * df['wi']
df['net_propane'] = df['propane_prod'] * df['nri'] * df['wi']
df['net_ibutane'] = df['ibutane_prod'] * df['nri'] * df['wi']
df['net_nbutane'] = df['nbutane_prod'] * df['nri'] * df['wi']
df['net_ipentane'] = df['ipentane_prod'] * df['nri'] * df['wi']
df['net_npentane'] = df['npentane_prod'] * df['nri'] * df['wi']
df['hexaneplus_prod'] = df['hexaneplus_prod'] * df['nri'] * df['wi']

# Calculating net revenues ($000s)

df['oil_revenue'] = df['net_oil'] * (oil_price - oil_price_deduct) 

df['methane_revenue'] = df['net_methane'] * (methane_price - gas_price_deduct)

df['helium_revenue'] = df['net_helium'] * (helium_price)

df['ethane_revenue'] = df['net_ethane'] * (ethane_price * (1- ngl_price_deduct))

df['propane_revenue'] = df['net_propane'] * (propane_price * (1- ngl_price_deduct))

df['ibutane_revenue'] = df['net_ibutane'] * (ibutane_price * (1- ngl_price_deduct))

df['nbutane_revenue'] = df['net_nbutane'] * (nbutane_price * (1- ngl_price_deduct))

df['ipentane_revenue'] = df['net_ipentane'] * (ipentane_price * (1- ngl_price_deduct))

df['npentane_revenue'] = df['net_npentane'] * (npentane_price * (1- ngl_price_deduct))

df['hexaneplus_revenue'] = df['hexaneplus_prod'] * (hexaneplus_price * (1- ngl_price_deduct))

df['gathering_and_transportation_fees'] =  (df['wi'] * df['gas'] * (primary_pipeline_fee + secondary_pipeline_fee)) /1000
df['gas_processing_fees'] = (df['wi'] * df['gas'] * (inlet_gas_fee)) /1000

df['methane_sharing_cost'] = (df['wi'] * df['methane_revenue'] * (nat_gas_processor_share))
df['helium_sharing_cost'] = (df['wi'] * df['helium_revenue'] * (helium_processor_share))
df['ngl_sharing_cost'] = (
    df['wi']* 
    ngl_processor_share* 
    (
        df['ethane_revenue']+
        df['propane_revenue']+
        df['ibutane_revenue']+
        df['nbutane_revenue']+
        df['ipentane_revenue']+
        df['npentane_revenue']+
        df['hexaneplus_revenue']
    )
)

# Calculating total net revenues
# Minus net revenue expenses

df['total_net_revenues'] = (
    df['oil_revenue']+
    df['methane_revenue']+
    df['helium_revenue']+
    df['ethane_revenue']+
    df['propane_revenue']+
    df['ibutane_revenue']+
    df['nbutane_revenue']+
    df['ipentane_revenue']+
    df['npentane_revenue']+
    df['hexaneplus_revenue'] -
    df['gathering_and_transportation_fees']-
    df['gas_processing_fees']-
    df['methane_sharing_cost']-
    df['helium_sharing_cost']-
    df['ngl_sharing_cost']
)

df['opex_pumping'] = pumping_services
df['opex_electricity'] = electricity
df['opex_other_contractor'] = other_contractors
df['opex_misc'] = misc

df['total_opex'] = (
        df['opex_pumping']+
        df['opex_electricity']+
        df['opex_other_contractor']+
        df['opex_misc']
) 

# Production Taxes Expenses

df['severance_tax'] = (
    (
        df['total_net_revenues']+
        df['gathering_and_transportation_fees']+
        df['gas_processing_fees']
    )*df['wi']*severance_tax
) 


df['ad_valorem_tax'] = (ad_valorem_tax * df['total_net_revenues']  * df['wi']) 

df['total_tax_expenses'] = df['severance_tax'] + df['ad_valorem_tax']

# Calculating EBITDA
# Defined as total_net_revenues minus total_opex and total_tax_expenses (production taxes)

df['EBITDA'] = df['total_net_revenues'] - df['total_opex'] - df['total_tax_expenses']

# Capital Expenditures

prod = capex_assumptions['production_well']

df['land_acquisition_capex'] = [0]*len(df)

df['completion_capex'] = [0]*len(df)

df['facilities_capex'] = [0]*len(df)

df['pipeline_capex'] = [0]*len(df)

df['plug_abandon_bond'] = [0]*len(df)

df.loc[0, 'land_acquisition_capex'] = prod['land_acquisition']*df['wi'].iloc[0]
df.loc[0, 'completion_capex'] = prod['completion']*df['wi'].iloc[0]
df.loc[0, 'facilities_capex'] = prod['facilities']*df['wi'].iloc[0]
df.loc[0, 'pipeline_capex'] = prod['pipeline']*df['wi'].iloc[0]
df.loc[0, 'plug_abandon_bond'] = prod['plug_abandon_bond']*df['wi'].iloc[0]

df['total_capex_spend'] = (
    df['land_acquisition_capex'] +
    df['completion_capex'] +
    df['facilities_capex'] +
    df['pipeline_capex'] +
    df['plug_abandon_bond']                           
)

# free cash flow

df['free_cash_flow'] = df['EBITDA'] - df['total_capex_spend']

df['cum_cash_flow'] = df['free_cash_flow'].cumsum()

df['fcf_margin'] = np.round(df['free_cash_flow'] / df['total_net_revenues'], 2)

# importing numpy financial for calculating metrics
# Note: The following code requires the 'numpy_financial' package.
# Install it using 'pip install numpy-financial' or comment out if not needed.

# import numpy_financial as npf

# irr 
# irr = npf.irr(df['free_cash_flow'])

# npv10
# discount_rate = 0.1
# npv10 = npf.npv(discount_rate, df['free_cash_flow'])

# roi
# Note: 'cum_cash_flows' is not defined; likely meant 'cum_cash_flow'.
# roi = np.round((np.max(df['cum_cash_flows']) / df['total_capex_spend'].sum()),2)

