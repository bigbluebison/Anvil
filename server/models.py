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
    production_curve_id = db.Column(db.Integer, db.ForeignKey('production_curve_table.id'))
    assumptions_id = db.Column(db.Integer, db.ForeignKey('assumptions_table.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects_table.id'))
    # user_id --- for the future

    # Relationships
    production_curve db.relationship('ProductionCurve', back_populates='well')
    assumptions = db.relationship('Assumptions', back_populates='well')
    project = db.relationship('Project', back_populates='wells')
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
    ngl_processing_feee = db.Column(db.Float)

    # additional revenue sharing arrangement/POP (% of revenue)
    nat_gas_processor_share = db.Column(db.Float)
    ngl_processor_share = db.Column(db.Float)
    helium_processor_share = db.Column(db.Float)

    # production taxes
    severance_tax = db.Column(db.Float)
    ad_valorem_tax = db.Column(db.Float)

    # capex assumptions
    capex_assumptions = db.Column(db.String, nullable=False)

    # gas concentration assumptions
    gas_concentrations = db.Column(db.String)

    # refinary assumptions
    # percentage eefficiency
    refinery_assumptions = db.Column(db.String)

    # drilling_start_date
    drilling_start_date = db.Column(db.String)

    # production_start_date
    prod_start_date = db.Column(db.String)


    # RELATIONSHIPS
    well = db.relationship('Well', back_populates='assumptions')


    # serialize rules
    serialize_rules = ('-wells_table',)

    # validations
    # for any future modification


class ProductionCurve(db.Model, SerializerMixin):
    __tablename__ = 'production_curve_table'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    type_curve = db.Column(db.String, nullable=False)

    # RELATIONSHIPS
    well = db.relationship('Well', back_populates='production_curve')

    # serialize rules
    serialize_rules = ('-wells_table',)

    # valiations
    # (need to think about this)

class Project(db.Model, SerializerMixin):
    __tablename__ = 'projects_table'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # RELATIONSHIPS
    wells = db.relationship('Well', back_populates='project')

    # serialize rules
    serialize_rules = ('-wells_table',)


class Pricing(db.Model, SerializerMixin):
    __tablename__ = "Pricing_table"

    id = db.Column(db.Integer, primary_key=True)

    oil_price = db.Column(db.Float)
    methane_price = db.Column(db.Float)
    helium_price = db.Column(db.Float)
    ethane_price =  db.Column(db.Float)
    propane_price =  db.Column(db.Float)
    i_butane_price  = db.Column(db.Float)
    n_butane_price = db.Column(db.Float)
    i_pentane_price = db.Column(db.Float)
    n_pentane_price = db.Column(db.Float)
    hexane_plus_price = db.Column(db.Float)


