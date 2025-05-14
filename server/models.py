from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates


from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property


from config import db, brycpt

# Models 

class Well(db.Mode, SerializerMixin):
    __tablename__ = 'wells_table'


    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


    # Foreign Keys
    
    # production_curve_id
    # gas_concentration_id
    # assumptions_id
    # project_id
    # user_id --- for the future

    # Relationships
    # production_curve
    # gas_concentration
    # assumptions
    # project
    # user --- future idea


class Assumptions(db.Model, SerializerMixin):
    __tablename__ = 'assumptions_table'

    # Columns (assumptions)
    
    # nri and wi
    nri_before_payout = db.Column(db.Float, nullable=False)
    nri_after_payout = db.Column(db.Float, nullable=False)
    wi_before_payout = db.Column(db.Float, nullable=False)
    wi_after_payout = db.Column(db.Float, nullable=False)
    
    # deducts (oil $/barrel, gas $/mcf, ngl (%))
    oil_price_deduct = db.Column(db.Float)
    gas_price_deduct = db.Column(db.Float)
    ngl_price_deduct = db.Column(db.Float)

    # gas transportation assumptions ($/mcf)
    primary_pipeline_fee = db.Column(db.Float)
    secondary_pipeline_fee = db.Column(db.Float)

    # gas processing cost assumptions
    # inlet_gas_fee ($/mcf)
    inlet_gas_fee = db.Column(db.Float)
    # nat gas liquids ($/gal)
















