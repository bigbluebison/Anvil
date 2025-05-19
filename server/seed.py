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
        opex_assumptions = json.dumps({
            "production_well": {
                "pumper": 7,              # $000
                "electricity": 5,         
                "water_disposal": 3,      
                "maintenance_repairs": 4, 
                "chemical_treatments": 2, 
                "other": 1           
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
            'ethane_efficiency' : 0.99,
            'propane_efficiency' : 0.99,
            'ibutane_efficiency' : 0.98,
            'nbutane_efficiency' : 0.98,
            'ipentane_efficiency' : 0.97,
            'npentane_efficiency' : 0.97,
            'hexaneplus_efficiency' : 0.96,
            'helium_efficiency' : 0.99
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
        opex_assumptions = json.dumps({
            "production_well": {
                "pumper": 7,              # $000
                "electricity": 5,         
                "water_disposal": 3,      
                "maintenance_repairs": 4, 
                "chemical_treatments": 2, 
                "other": 1           
            }
        }),
        gas_concentrations = json.dumps({
            'methane'     : 0.5143,
            'ethane'      : 0.0453,
            'propane'     : 0.0219,
            'i-butane'    : 0.0188,
            'n-butane'    : 0.0101,
            'i-pentane'   : 0.0028,
            'n-pentane'   : 0.0019,
            'hexane+'     : 0.0017,
            'helium'      : 0.0079,
            'other'       : 0.0000
        }),
        refinery_assumptions = json.dumps({
            'ethane_efficiency' : 0.99,
            'propane_efficiency' : 0.99,
            'ibutane_efficiency' : 0.98,
            'nbutane_efficiency' : 0.98,
            'ipentane_efficiency' : 0.97,
            'npentane_efficiency' : 0.97,
            'hexaneplus_efficiency' : 0.96,
            'helium_efficiency' : 0.99
        }),
        drilling_start_date = '2023-03-01',
        prod_start_date = '2023-09-01'
    )

    db.session.add(assumptions1)
    db.session.add(assumptions2)



def seed_curves():

    curve1 = ProductionCurve(type_curve=json.dumps([
    {"Month": 0, "Oil_Production (Bbl)": "22,800", "Total_Gas_Production (Mcf)": "44,460"},
    {"Month": 1, "Oil_Production (Bbl)": "20,668", "Total_Gas_Production (Mcf)": "40,484"},
    {"Month": 2, "Oil_Production (Bbl)": "17,244", "Total_Gas_Production (Mcf)": "34,082"},
    {"Month": 3, "Oil_Production (Bbl)": "14,723", "Total_Gas_Production (Mcf)": "29,360"},
    {"Month": 4, "Oil_Production (Bbl)": "12,796", "Total_Gas_Production (Mcf)": "25,748"},
    {"Month": 5, "Oil_Production (Bbl)": "11,280", "Total_Gas_Production (Mcf)": "22,902"},
    {"Month": 6, "Oil_Production (Bbl)": "10,059", "Total_Gas_Production (Mcf)": "20,608"},
    {"Month": 7, "Oil_Production (Bbl)": "9,058", "Total_Gas_Production (Mcf)": "18,724"},
    {"Month": 8, "Oil_Production (Bbl)": "8,223", "Total_Gas_Production (Mcf)": "17,150"},
    {"Month": 9, "Oil_Production (Bbl)": "7,516", "Total_Gas_Production (Mcf)": "15,819"},
    {"Month": 10, "Oil_Production (Bbl)": "6,912", "Total_Gas_Production (Mcf)": "14,679"},
    {"Month": 11, "Oil_Production (Bbl)": "6,391", "Total_Gas_Production (Mcf)": "13,693"},
    {"Month": 12, "Oil_Production (Bbl)": "5,936", "Total_Gas_Production (Mcf)": "12,833"},
    {"Month": 13, "Oil_Production (Bbl)": "5,536", "Total_Gas_Production (Mcf)": "12,076"},
    {"Month": 14, "Oil_Production (Bbl)": "5,182", "Total_Gas_Production (Mcf)": "11,406"},
    {"Month": 15, "Oil_Production (Bbl)": "4,867", "Total_Gas_Production (Mcf)": "10,810"},
    {"Month": 16, "Oil_Production (Bbl)": "4,585", "Total_Gas_Production (Mcf)": "10,275"},
    {"Month": 17, "Oil_Production (Bbl)": "4,331", "Total_Gas_Production (Mcf)": "9,793"},
    {"Month": 18, "Oil_Production (Bbl)": "4,101", "Total_Gas_Production (Mcf)": "9,357"},
    {"Month": 19, "Oil_Production (Bbl)": "3,892", "Total_Gas_Production (Mcf)": "8,961"},
    {"Month": 20, "Oil_Production (Bbl)": "3,702", "Total_Gas_Production (Mcf)": "8,599"},
    {"Month": 21, "Oil_Production (Bbl)": "3,528", "Total_Gas_Production (Mcf)": "8,268"},
    {"Month": 22, "Oil_Production (Bbl)": "3,368", "Total_Gas_Production (Mcf)": "7,965"},
    {"Month": 23, "Oil_Production (Bbl)": "3,220", "Total_Gas_Production (Mcf)": "7,685"},
    {"Month": 24, "Oil_Production (Bbl)": "3,084", "Total_Gas_Production (Mcf)": "7,426"},
    {"Month": 25, "Oil_Production (Bbl)": "2,958", "Total_Gas_Production (Mcf)": "7,187"},
    {"Month": 26, "Oil_Production (Bbl)": "2,841", "Total_Gas_Production (Mcf)": "6,964"},
    {"Month": 27, "Oil_Production (Bbl)": "2,732", "Total_Gas_Production (Mcf)": "6,757"},
    {"Month": 28, "Oil_Production (Bbl)": "2,630", "Total_Gas_Production (Mcf)": "6,564"},
    {"Month": 29, "Oil_Production (Bbl)": "2,535", "Total_Gas_Production (Mcf)": "6,384"},
    {"Month": 30, "Oil_Production (Bbl)": "2,446", "Total_Gas_Production (Mcf)": "6,215"},
    {"Month": 31, "Oil_Production (Bbl)": "2,362", "Total_Gas_Production (Mcf)": "6,057"},
    {"Month": 32, "Oil_Production (Bbl)": "2,284", "Total_Gas_Production (Mcf)": "5,908"},
    {"Month": 33, "Oil_Production (Bbl)": "2,210", "Total_Gas_Production (Mcf)": "5,768"},
    {"Month": 34, "Oil_Production (Bbl)": "2,140", "Total_Gas_Production (Mcf)": "5,636"},
    {"Month": 35, "Oil_Production (Bbl)": "2,074", "Total_Gas_Production (Mcf)": "5,512"},
    {"Month": 36, "Oil_Production (Bbl)": "2,011", "Total_Gas_Production (Mcf)": "5,394"},
    {"Month": 37, "Oil_Production (Bbl)": "1,952", "Total_Gas_Production (Mcf)": "5,283"},
    {"Month": 38, "Oil_Production (Bbl)": "1,896", "Total_Gas_Production (Mcf)": "5,177"},
    {"Month": 39, "Oil_Production (Bbl)": "1,843", "Total_Gas_Production (Mcf)": "5,078"},
    {"Month": 40, "Oil_Production (Bbl)": "1,793", "Total_Gas_Production (Mcf)": "4,983"},
    {"Month": 41, "Oil_Production (Bbl)": "1,744", "Total_Gas_Production (Mcf)": "4,893"},
    {"Month": 42, "Oil_Production (Bbl)": "1,699", "Total_Gas_Production (Mcf)": "4,807"},
    {"Month": 43, "Oil_Production (Bbl)": "1,655", "Total_Gas_Production (Mcf)": "4,726"},
    {"Month": 44, "Oil_Production (Bbl)": "1,613", "Total_Gas_Production (Mcf)": "4,648"},
    {"Month": 45, "Oil_Production (Bbl)": "1,573", "Total_Gas_Production (Mcf)": "4,574"},
    {"Month": 46, "Oil_Production (Bbl)": "1,535", "Total_Gas_Production (Mcf)": "4,503"},
    {"Month": 47, "Oil_Production (Bbl)": "1,499", "Total_Gas_Production (Mcf)": "4,436"},
    {"Month": 48, "Oil_Production (Bbl)": "1,464", "Total_Gas_Production (Mcf)": "4,371"},
    {"Month": 49, "Oil_Production (Bbl)": "1,430", "Total_Gas_Production (Mcf)": "4,295"},
    {"Month": 50, "Oil_Production (Bbl)": "1,398", "Total_Gas_Production (Mcf)": "4,206"},
    {"Month": 51, "Oil_Production (Bbl)": "1,367", "Total_Gas_Production (Mcf)": "4,122"},
    {"Month": 52, "Oil_Production (Bbl)": "1,337", "Total_Gas_Production (Mcf)": "4,040"},
    {"Month": 53, "Oil_Production (Bbl)": "1,309", "Total_Gas_Production (Mcf)": "3,962"},
    {"Month": 54, "Oil_Production (Bbl)": "1,281", "Total_Gas_Production (Mcf)": "3,887"},
    {"Month": 55, "Oil_Production (Bbl)": "1,255", "Total_Gas_Production (Mcf)": "3,814"},
    {"Month": 56, "Oil_Production (Bbl)": "1,229", "Total_Gas_Production (Mcf)": "3,744"},
    {"Month": 57, "Oil_Production (Bbl)": "1,205", "Total_Gas_Production (Mcf)": "3,677"},
    {"Month": 58, "Oil_Production (Bbl)": "1,181", "Total_Gas_Production (Mcf)": "3,612"},
    {"Month": 59, "Oil_Production (Bbl)": "1,158", "Total_Gas_Production (Mcf)": "3,549"},
    {"Month": 60, "Oil_Production (Bbl)": "1,136", "Total_Gas_Production (Mcf)": "3,488"},
    {"Month": 61, "Oil_Production (Bbl)": "1,117", "Total_Gas_Production (Mcf)": "3,436"},
    {"Month": 62, "Oil_Production (Bbl)": "1,099", "Total_Gas_Production (Mcf)": "3,386"},
    {"Month": 63, "Oil_Production (Bbl)": "1,081", "Total_Gas_Production (Mcf)": "3,336"},
    {"Month": 64, "Oil_Production (Bbl)": "1,063", "Total_Gas_Production (Mcf)": "3,287"},
    {"Month": 65, "Oil_Production (Bbl)": "1,046", "Total_Gas_Production (Mcf)": "3,239"},
    {"Month": 66, "Oil_Production (Bbl)": "1,028", "Total_Gas_Production (Mcf)": "3,191"},
    {"Month": 67, "Oil_Production (Bbl)": "1,011", "Total_Gas_Production (Mcf)": "3,144"},
    {"Month": 68, "Oil_Production (Bbl)": "995", "Total_Gas_Production (Mcf)": "3,097"},
    {"Month": 69, "Oil_Production (Bbl)": "978", "Total_Gas_Production (Mcf)": "3,052"},
    {"Month": 70, "Oil_Production (Bbl)": "962", "Total_Gas_Production (Mcf)": "3,007"},
    {"Month": 71, "Oil_Production (Bbl)": "946", "Total_Gas_Production (Mcf)": "2,962"},
    {"Month": 72, "Oil_Production (Bbl)": "931", "Total_Gas_Production (Mcf)": "2,919"},
    {"Month": 73, "Oil_Production (Bbl)": "915", "Total_Gas_Production (Mcf)": "2,875"},
    {"Month": 74, "Oil_Production (Bbl)": "900", "Total_Gas_Production (Mcf)": "2,833"},
    {"Month": 75, "Oil_Production (Bbl)": "886", "Total_Gas_Production (Mcf)": "2,791"},
    {"Month": 76, "Oil_Production (Bbl)": "871", "Total_Gas_Production (Mcf)": "2,750"},
    {"Month": 77, "Oil_Production (Bbl)": "857", "Total_Gas_Production (Mcf)": "2,709"},
    {"Month": 78, "Oil_Production (Bbl)": "843", "Total_Gas_Production (Mcf)": "2,669"},
    {"Month": 79, "Oil_Production (Bbl)": "829", "Total_Gas_Production (Mcf)": "2,630"},
    {"Month": 80, "Oil_Production (Bbl)": "815", "Total_Gas_Production (Mcf)": "2,591"},
    {"Month": 81, "Oil_Production (Bbl)": "802", "Total_Gas_Production (Mcf)": "2,553"},
    {"Month": 82, "Oil_Production (Bbl)": "789", "Total_Gas_Production (Mcf)": "2,515"},
    {"Month": 83, "Oil_Production (Bbl)": "776", "Total_Gas_Production (Mcf)": "2,478"},
    {"Month": 84, "Oil_Production (Bbl)": "763", "Total_Gas_Production (Mcf)": "2,442"},
    {"Month": 85, "Oil_Production (Bbl)": "751", "Total_Gas_Production (Mcf)": "2,406"},
    {"Month": 86, "Oil_Production (Bbl)": "738", "Total_Gas_Production (Mcf)": "2,370"},
    {"Month": 87, "Oil_Production (Bbl)": "726", "Total_Gas_Production (Mcf)": "2,336"},
    {"Month": 88, "Oil_Production (Bbl)": "714", "Total_Gas_Production (Mcf)": "2,301"},
    {"Month": 89, "Oil_Production (Bbl)": "703", "Total_Gas_Production (Mcf)": "2,267"},
    {"Month": 90, "Oil_Production (Bbl)": "691", "Total_Gas_Production (Mcf)": "2,234"},
    {"Month": 91, "Oil_Production (Bbl)": "680", "Total_Gas_Production (Mcf)": "2,201"},
    {"Month": 92, "Oil_Production (Bbl)": "669", "Total_Gas_Production (Mcf)": "2,169"},
    {"Month": 93, "Oil_Production (Bbl)": "658", "Total_Gas_Production (Mcf)": "2,137"},
    {"Month": 94, "Oil_Production (Bbl)": "647", "Total_Gas_Production (Mcf)": "2,105"},
    {"Month": 95, "Oil_Production (Bbl)": "636", "Total_Gas_Production (Mcf)": "2,074"},
    {"Month": 96, "Oil_Production (Bbl)": "626", "Total_Gas_Production (Mcf)": "2,044"},
    {"Month": 97, "Oil_Production (Bbl)": "616", "Total_Gas_Production (Mcf)": "2,014"},
    {"Month": 98, "Oil_Production (Bbl)": "606", "Total_Gas_Production (Mcf)": "1,984"},
    {"Month": 99, "Oil_Production (Bbl)": "596", "Total_Gas_Production (Mcf)": "1,955"},
    {"Month": 100, "Oil_Production (Bbl)": "586", "Total_Gas_Production (Mcf)": "1,926"},
    {"Month": 101, "Oil_Production (Bbl)": "576", "Total_Gas_Production (Mcf)": "1,898"},
    {"Month": 102, "Oil_Production (Bbl)": "567", "Total_Gas_Production (Mcf)": "1,870"},
    {"Month": 103, "Oil_Production (Bbl)": "558", "Total_Gas_Production (Mcf)": "1,843"},
    {"Month": 104, "Oil_Production (Bbl)": "548", "Total_Gas_Production (Mcf)": "1,816"},
    {"Month": 105, "Oil_Production (Bbl)": "539", "Total_Gas_Production (Mcf)": "1,789"},
    {"Month": 106, "Oil_Production (Bbl)": "531", "Total_Gas_Production (Mcf)": "1,763"},
    {"Month": 107, "Oil_Production (Bbl)": "522", "Total_Gas_Production (Mcf)": "1,737"},
    {"Month": 108, "Oil_Production (Bbl)": "513", "Total_Gas_Production (Mcf)": "1,712"},
    {"Month": 109, "Oil_Production (Bbl)": "505", "Total_Gas_Production (Mcf)": "1,687"},
    {"Month": 110, "Oil_Production (Bbl)": "496", "Total_Gas_Production (Mcf)": "1,662"},
    {"Month": 111, "Oil_Production (Bbl)": "488", "Total_Gas_Production (Mcf)": "1,637"},
    {"Month": 112, "Oil_Production (Bbl)": "480", "Total_Gas_Production (Mcf)": "1,613"},
    {"Month": 113, "Oil_Production (Bbl)": "472", "Total_Gas_Production (Mcf)": "1,589"},
    {"Month": 114, "Oil_Production (Bbl)": "464", "Total_Gas_Production (Mcf)": "1,566"},
    {"Month": 115, "Oil_Production (Bbl)": "457", "Total_Gas_Production (Mcf)": "1,543"},
    {"Month": 116, "Oil_Production (Bbl)": "449", "Total_Gas_Production (Mcf)": "1,520"},
    {"Month": 117, "Oil_Production (Bbl)": "442", "Total_Gas_Production (Mcf)": "1,498"},
    {"Month": 118, "Oil_Production (Bbl)": "435", "Total_Gas_Production (Mcf)": "1,476"},
    {"Month": 119, "Oil_Production (Bbl)": "427", "Total_Gas_Production (Mcf)": "1,454"},
    {"Month": 120, "Oil_Production (Bbl)": "420", "Total_Gas_Production (Mcf)": "1,433"}
    ]))

    curve2 = ProductionCurve(type_curve=json.dumps([
    {"Month": 0, "Oil_Production (Bbl)": "22,800", "Total_Gas_Production (Mcf)": "44,460"},
    {"Month": 1, "Oil_Production (Bbl)": "20,668", "Total_Gas_Production (Mcf)": "40,484"},
    {"Month": 2, "Oil_Production (Bbl)": "17,244", "Total_Gas_Production (Mcf)": "34,082"},
    {"Month": 3, "Oil_Production (Bbl)": "14,723", "Total_Gas_Production (Mcf)": "29,360"},
    {"Month": 4, "Oil_Production (Bbl)": "12,796", "Total_Gas_Production (Mcf)": "25,748"},
    {"Month": 5, "Oil_Production (Bbl)": "11,280", "Total_Gas_Production (Mcf)": "22,902"},
    {"Month": 6, "Oil_Production (Bbl)": "10,059", "Total_Gas_Production (Mcf)": "20,608"},
    {"Month": 7, "Oil_Production (Bbl)": "9,058", "Total_Gas_Production (Mcf)": "18,724"},
    {"Month": 8, "Oil_Production (Bbl)": "8,223", "Total_Gas_Production (Mcf)": "17,150"},
    {"Month": 9, "Oil_Production (Bbl)": "7,516", "Total_Gas_Production (Mcf)": "15,819"},
    {"Month": 10, "Oil_Production (Bbl)": "6,912", "Total_Gas_Production (Mcf)": "14,679"},
    {"Month": 11, "Oil_Production (Bbl)": "6,391", "Total_Gas_Production (Mcf)": "13,693"},
    {"Month": 12, "Oil_Production (Bbl)": "5,936", "Total_Gas_Production (Mcf)": "12,833"},
    {"Month": 13, "Oil_Production (Bbl)": "5,536", "Total_Gas_Production (Mcf)": "12,076"},
    {"Month": 14, "Oil_Production (Bbl)": "5,182", "Total_Gas_Production (Mcf)": "11,406"},
    {"Month": 15, "Oil_Production (Bbl)": "4,867", "Total_Gas_Production (Mcf)": "10,810"},
    {"Month": 16, "Oil_Production (Bbl)": "4,585", "Total_Gas_Production (Mcf)": "10,275"},
    {"Month": 17, "Oil_Production (Bbl)": "4,331", "Total_Gas_Production (Mcf)": "9,793"},
    {"Month": 18, "Oil_Production (Bbl)": "4,101", "Total_Gas_Production (Mcf)": "9,357"},
    {"Month": 19, "Oil_Production (Bbl)": "3,892", "Total_Gas_Production (Mcf)": "8,961"},
    {"Month": 20, "Oil_Production (Bbl)": "3,702", "Total_Gas_Production (Mcf)": "8,599"},
    {"Month": 21, "Oil_Production (Bbl)": "3,528", "Total_Gas_Production (Mcf)": "8,268"},
    {"Month": 22, "Oil_Production (Bbl)": "3,368", "Total_Gas_Production (Mcf)": "7,965"},
    {"Month": 23, "Oil_Production (Bbl)": "3,220", "Total_Gas_Production (Mcf)": "7,685"},
    {"Month": 24, "Oil_Production (Bbl)": "3,084", "Total_Gas_Production (Mcf)": "7,426"},
    {"Month": 25, "Oil_Production (Bbl)": "2,958", "Total_Gas_Production (Mcf)": "7,187"},
    {"Month": 26, "Oil_Production (Bbl)": "2,841", "Total_Gas_Production (Mcf)": "6,964"},
    {"Month": 27, "Oil_Production (Bbl)": "2,732", "Total_Gas_Production (Mcf)": "6,757"},
    {"Month": 28, "Oil_Production (Bbl)": "2,630", "Total_Gas_Production (Mcf)": "6,564"},
    {"Month": 29, "Oil_Production (Bbl)": "2,535", "Total_Gas_Production (Mcf)": "6,384"},
    {"Month": 30, "Oil_Production (Bbl)": "2,446", "Total_Gas_Production (Mcf)": "6,215"},
    {"Month": 31, "Oil_Production (Bbl)": "2,362", "Total_Gas_Production (Mcf)": "6,057"},
    {"Month": 32, "Oil_Production (Bbl)": "2,284", "Total_Gas_Production (Mcf)": "5,908"},
    {"Month": 33, "Oil_Production (Bbl)": "2,210", "Total_Gas_Production (Mcf)": "5,768"},
    {"Month": 34, "Oil_Production (Bbl)": "2,140", "Total_Gas_Production (Mcf)": "5,636"},
    {"Month": 35, "Oil_Production (Bbl)": "2,074", "Total_Gas_Production (Mcf)": "5,512"},
    {"Month": 36, "Oil_Production (Bbl)": "2,011", "Total_Gas_Production (Mcf)": "5,394"},
    {"Month": 37, "Oil_Production (Bbl)": "1,952", "Total_Gas_Production (Mcf)": "5,283"},
    {"Month": 38, "Oil_Production (Bbl)": "1,896", "Total_Gas_Production (Mcf)": "5,177"},
    {"Month": 39, "Oil_Production (Bbl)": "1,843", "Total_Gas_Production (Mcf)": "5,078"},
    {"Month": 40, "Oil_Production (Bbl)": "1,793", "Total_Gas_Production (Mcf)": "4,983"},
    {"Month": 41, "Oil_Production (Bbl)": "1,744", "Total_Gas_Production (Mcf)": "4,893"},
    {"Month": 42, "Oil_Production (Bbl)": "1,699", "Total_Gas_Production (Mcf)": "4,807"},
    {"Month": 43, "Oil_Production (Bbl)": "1,655", "Total_Gas_Production (Mcf)": "4,726"},
    {"Month": 44, "Oil_Production (Bbl)": "1,613", "Total_Gas_Production (Mcf)": "4,648"},
    {"Month": 45, "Oil_Production (Bbl)": "1,573", "Total_Gas_Production (Mcf)": "4,574"},
    {"Month": 46, "Oil_Production (Bbl)": "1,535", "Total_Gas_Production (Mcf)": "4,503"},
    {"Month": 47, "Oil_Production (Bbl)": "1,499", "Total_Gas_Production (Mcf)": "4,436"},
    {"Month": 48, "Oil_Production (Bbl)": "1,464", "Total_Gas_Production (Mcf)": "4,371"},
    {"Month": 49, "Oil_Production (Bbl)": "1,430", "Total_Gas_Production (Mcf)": "4,295"},
    {"Month": 50, "Oil_Production (Bbl)": "1,398", "Total_Gas_Production (Mcf)": "4,206"},
    {"Month": 51, "Oil_Production (Bbl)": "1,367", "Total_Gas_Production (Mcf)": "4,122"},
    {"Month": 52, "Oil_Production (Bbl)": "1,337", "Total_Gas_Production (Mcf)": "4,040"},
    {"Month": 53, "Oil_Production (Bbl)": "1,309", "Total_Gas_Production (Mcf)": "3,962"},
    {"Month": 54, "Oil_Production (Bbl)": "1,281", "Total_Gas_Production (Mcf)": "3,887"},
    {"Month": 55, "Oil_Production (Bbl)": "1,255", "Total_Gas_Production (Mcf)": "3,814"},
    {"Month": 56, "Oil_Production (Bbl)": "1,229", "Total_Gas_Production (Mcf)": "3,744"},
    {"Month": 57, "Oil_Production (Bbl)": "1,205", "Total_Gas_Production (Mcf)": "3,677"},
    {"Month": 58, "Oil_Production (Bbl)": "1,181", "Total_Gas_Production (Mcf)": "3,612"},
    {"Month": 59, "Oil_Production (Bbl)": "1,158", "Total_Gas_Production (Mcf)": "3,549"},
    {"Month": 60, "Oil_Production (Bbl)": "1,136", "Total_Gas_Production (Mcf)": "3,488"},
    {"Month": 61, "Oil_Production (Bbl)": "1,117", "Total_Gas_Production (Mcf)": "3,436"},
    {"Month": 62, "Oil_Production (Bbl)": "1,099", "Total_Gas_Production (Mcf)": "3,386"},
    {"Month": 63, "Oil_Production (Bbl)": "1,081", "Total_Gas_Production (Mcf)": "3,336"},
    {"Month": 64, "Oil_Production (Bbl)": "1,063", "Total_Gas_Production (Mcf)": "3,287"},
    {"Month": 65, "Oil_Production (Bbl)": "1,046", "Total_Gas_Production (Mcf)": "3,239"},
    {"Month": 66, "Oil_Production (Bbl)": "1,028", "Total_Gas_Production (Mcf)": "3,191"},
    {"Month": 67, "Oil_Production (Bbl)": "1,011", "Total_Gas_Production (Mcf)": "3,144"},
    {"Month": 68, "Oil_Production (Bbl)": "995", "Total_Gas_Production (Mcf)": "3,097"},
    {"Month": 69, "Oil_Production (Bbl)": "978", "Total_Gas_Production (Mcf)": "3,052"},
    {"Month": 70, "Oil_Production (Bbl)": "962", "Total_Gas_Production (Mcf)": "3,007"},
    {"Month": 71, "Oil_Production (Bbl)": "946", "Total_Gas_Production (Mcf)": "2,962"},
    {"Month": 72, "Oil_Production (Bbl)": "931", "Total_Gas_Production (Mcf)": "2,919"},
    {"Month": 73, "Oil_Production (Bbl)": "915", "Total_Gas_Production (Mcf)": "2,875"},
    {"Month": 74, "Oil_Production (Bbl)": "900", "Total_Gas_Production (Mcf)": "2,833"},
    {"Month": 75, "Oil_Production (Bbl)": "886", "Total_Gas_Production (Mcf)": "2,791"},
    {"Month": 76, "Oil_Production (Bbl)": "871", "Total_Gas_Production (Mcf)": "2,750"},
    {"Month": 77, "Oil_Production (Bbl)": "857", "Total_Gas_Production (Mcf)": "2,709"},
    {"Month": 78, "Oil_Production (Bbl)": "843", "Total_Gas_Production (Mcf)": "2,669"},
    {"Month": 79, "Oil_Production (Bbl)": "829", "Total_Gas_Production (Mcf)": "2,630"},
    {"Month": 80, "Oil_Production (Bbl)": "815", "Total_Gas_Production (Mcf)": "2,591"},
    {"Month": 81, "Oil_Production (Bbl)": "802", "Total_Gas_Production (Mcf)": "2,553"},
    {"Month": 82, "Oil_Production (Bbl)": "789", "Total_Gas_Production (Mcf)": "2,515"},
    {"Month": 83, "Oil_Production (Bbl)": "776", "Total_Gas_Production (Mcf)": "2,478"},
    {"Month": 84, "Oil_Production (Bbl)": "763", "Total_Gas_Production (Mcf)": "2,442"},
    {"Month": 85, "Oil_Production (Bbl)": "751", "Total_Gas_Production (Mcf)": "2,406"},
    {"Month": 86, "Oil_Production (Bbl)": "738", "Total_Gas_Production (Mcf)": "2,370"},
    {"Month": 87, "Oil_Production (Bbl)": "726", "Total_Gas_Production (Mcf)": "2,336"},
    {"Month": 88, "Oil_Production (Bbl)": "714", "Total_Gas_Production (Mcf)": "2,301"},
    {"Month": 89, "Oil_Production (Bbl)": "703", "Total_Gas_Production (Mcf)": "2,267"},
    {"Month": 90, "Oil_Production (Bbl)": "691", "Total_Gas_Production (Mcf)": "2,234"},
    {"Month": 91, "Oil_Production (Bbl)": "680", "Total_Gas_Production (Mcf)": "2,201"},
    {"Month": 92, "Oil_Production (Bbl)": "669", "Total_Gas_Production (Mcf)": "2,169"},
    {"Month": 93, "Oil_Production (Bbl)": "658", "Total_Gas_Production (Mcf)": "2,137"},
    {"Month": 94, "Oil_Production (Bbl)": "647", "Total_Gas_Production (Mcf)": "2,105"},
    {"Month": 95, "Oil_Production (Bbl)": "636", "Total_Gas_Production (Mcf)": "2,074"},
    {"Month": 96, "Oil_Production (Bbl)": "626", "Total_Gas_Production (Mcf)": "2,044"},
    {"Month": 97, "Oil_Production (Bbl)": "616", "Total_Gas_Production (Mcf)": "2,014"},
    {"Month": 98, "Oil_Production (Bbl)": "606", "Total_Gas_Production (Mcf)": "1,984"},
    {"Month": 99, "Oil_Production (Bbl)": "596", "Total_Gas_Production (Mcf)": "1,955"},
    {"Month": 100, "Oil_Production (Bbl)": "586", "Total_Gas_Production (Mcf)": "1,926"},
    {"Month": 101, "Oil_Production (Bbl)": "576", "Total_Gas_Production (Mcf)": "1,898"},
    {"Month": 102, "Oil_Production (Bbl)": "567", "Total_Gas_Production (Mcf)": "1,870"},
    {"Month": 103, "Oil_Production (Bbl)": "558", "Total_Gas_Production (Mcf)": "1,843"},
    {"Month": 104, "Oil_Production (Bbl)": "548", "Total_Gas_Production (Mcf)": "1,816"},
    {"Month": 105, "Oil_Production (Bbl)": "539", "Total_Gas_Production (Mcf)": "1,789"},
    {"Month": 106, "Oil_Production (Bbl)": "531", "Total_Gas_Production (Mcf)": "1,763"},
    {"Month": 107, "Oil_Production (Bbl)": "522", "Total_Gas_Production (Mcf)": "1,737"},
    {"Month": 108, "Oil_Production (Bbl)": "513", "Total_Gas_Production (Mcf)": "1,712"},
    {"Month": 109, "Oil_Production (Bbl)": "505", "Total_Gas_Production (Mcf)": "1,687"},
    {"Month": 110, "Oil_Production (Bbl)": "496", "Total_Gas_Production (Mcf)": "1,662"},
    {"Month": 111, "Oil_Production (Bbl)": "488", "Total_Gas_Production (Mcf)": "1,637"},
    {"Month": 112, "Oil_Production (Bbl)": "480", "Total_Gas_Production (Mcf)": "1,613"},
    {"Month": 113, "Oil_Production (Bbl)": "472", "Total_Gas_Production (Mcf)": "1,589"},
    {"Month": 114, "Oil_Production (Bbl)": "464", "Total_Gas_Production (Mcf)": "1,566"},
    {"Month": 115, "Oil_Production (Bbl)": "457", "Total_Gas_Production (Mcf)": "1,543"},
    {"Month": 116, "Oil_Production (Bbl)": "449", "Total_Gas_Production (Mcf)": "1,520"},
    {"Month": 117, "Oil_Production (Bbl)": "442", "Total_Gas_Production (Mcf)": "1,498"},
    {"Month": 118, "Oil_Production (Bbl)": "435", "Total_Gas_Production (Mcf)": "1,476"},
    {"Month": 119, "Oil_Production (Bbl)": "427", "Total_Gas_Production (Mcf)": "1,454"},
    {"Month": 120, "Oil_Production (Bbl)": "420", "Total_Gas_Production (Mcf)": "1,433"}
    ]))

    db.session.add(curve1)
    db.session.add(curve2)


def seed_project():
    # Creating some sample projects
    project1 = Project(name="ProjectAAA")
    project2 = Project(name="ProjectBBB")

    db.session.add(project1)
    db.session.add(project2)

def seed_pricing():
    # Creating a pricing instance
    pricing1 = Pricing ( oil_price = 30.0,
                       methane_price = 4.0,
                       helium_price = 50.0,
                       ethane_price = 0.46,
                       propane_price = 0.25,
                       i_butane_price = 0.15,
                       n_butane_price = 1.0,
                       i_pentane_price = 1.0,
                       n_pentane_price = 1.0,
                       hexane_plus_price = 1.0 )
    
    db.session.add(pricing1)



if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        seed_well()
        seed_assumptions()
        seed_curves()
        seed_project()
        seed_pricing()

        db.session.commit()

