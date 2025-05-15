#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
import json

# Local imports
from app import app
from models import db, Well, Assumptions, ProductionCurve, Project, Pricing


def seed_well():

    well1 = Well(name='flowerwell', production_curve_id=1, assumptions_id=1, project_id=1)
    well2 = Well(name='rosewell', production_curve_id=2, assumptions_id=2, project_id=2)

    db.session.add(well1)
    db.session.add(well2)

def seed_assumptions():
    assumptions1 = Assumptions(
        nri_before_payout = 0.825,
        nri_after_payout = 0.825,
        wi_before_payout = 1.00,
        wi_after_payout = 1.00,
        oil_price_deduct = 3.25,
        gas_price_deduct = 0.18,
        ngl_price_deduct = 0.05,
        primary_pipeline_fee = 0.10,
        secondary_pipeline_fee = 0.05,
        inlet_gas_fee = 0.20,
        ngl_processing_feee = 0.10,
        nat_gas_processor_share = 0.03,
        ngl_processor_share = 0.05,
        helium_processor_share = 0.05,
        severance_tax = 0.05,
        ad_valorem_tax = 0.02,
        capex_assumptions = json.dumps({
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
        }),
        gas_concentrations = json.dumps({
            'methane'     : 0.5366,
            'ethane'      : 0.0493,
            'propane'     : 0.0319,
            'i-butane'    : 0.0048,
            'n-butane'    : 0.0101,
            'i-pentane'   : 0.0018,
            'n-pentane'   : 0.0025,
            'hexane+'     : 0.0019,
            'helium'      : 0.0082,
            'other'       : 0.0000
        }),
        refinery_assumptions = json.dumps({
            ethane_efficiency = 0.99,
            propane_efficiency = 0.99,
            ibutane_efficiency = 0.98,
            nbutane_efficiency = 0.98,
            ipentane_efficiency = 0.97,
            npentane_efficiency = 0.97,
            hexaneplus_efficiency = 0.96,
            helium_efficiency = 0.99
        }),
        drilling_start_date = '2023-01-01',
        prod_start_date = '2023-06-01'
    )

    assumptions2 = Assumptions(
        nri_before_payout = 0.825,
        nri_after_payout = 0.825,
        wi_before_payout = 1.00,
        wi_after_payout = 1.00,
        oil_price_deduct = 3.25,
        gas_price_deduct = 0.18,
        ngl_price_deduct = 0.05,
        primary_pipeline_fee = 0.10,
        secondary_pipeline_fee = 0.05,
        inlet_gas_fee = 0.20,
        ngl_processing_feee = 0.10,
        nat_gas_processor_share = 0.03,
        ngl_processor_share = 0.05,
        helium_processor_share = 0.05,
        severance_tax = 0.05,
        ad_valorem_tax = 0.02,
        capex_assumptions = json.dumps({
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
        }),
        gas_concentrations = json.dumps({
            'methane'     : 0.5241,
            'ethane'      : 0.0543,
            'propane'     : 0.0219,
            'i-butane'    : 0.0148,
            'n-butane'    : 0.0101,
            'i-pentane'   : 0.0028,
            'n-pentane'   : 0.0019,
            'hexane+'     : 0.0017,
            'helium'      : 0.0079,
            'other'       : 0.0000
        }),
        refinery_assumptions = json.dumps({
            ethane_efficiency = 0.99,
            propane_efficiency = 0.99,
            ibutane_efficiency = 0.98,
            nbutane_efficiency = 0.98,
            ipentane_efficiency = 0.97,
            npentane_efficiency = 0.97,
            hexaneplus_efficiency = 0.96,
            helium_efficiency = 0.99
        }),
        drilling_start_date = '2023-03-01',
        prod_start_date = '2023-09-01'
    )







if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

