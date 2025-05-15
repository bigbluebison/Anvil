#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, render_template
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports

from models import Well, Assumptions, ProductionCurve, Project, Pricing
import singlewellmodel


# well routes

class WellNorm(Resource):

    # get all wells
    def get(self):
        wells_to_get = Well.query.all()

        data = [well.to_dict() for well in wells to get]

        return data, 200

    # post a new well
    def post(self):
        well_to_create = request.get_json()

        try:
            new_well = Well(
                name=well_to_create['name']
            )

            db.session.add(new_well)
            db.session.commit()

            return new_well.to_dict(), 201

        except:
            raise Exception('There was an error creating this well')

    api.add_resource(WellNorm, '/wells_table')


class WellId(Resource):

    # get a sepecific well by id
    def get(self, id):
        well_to_choose = Well.query.filter_by(id=id).first()

        if well_to_choose:
            return well_to_choose.to_dict(), 200
        else:
            return {'error': 'Well does not exist'}, 404

    # patch a specific well by id
    def patch(self, id):

        data_to_patch_with = request.get_json()

        try:
            well_to_choose = Well.query.filter_by(id=id).first()

            for field in data_to_patch_with:
                setattr(well_to_choose, field, data_to_patch_with[field])

            db.session.commit()
            return well_to_choose.to_dict(), 200

        except Exception as e:
            Print(e) 
            return {'error': 'There was an error updating this well'}, 400


    # delete a specific well by id
    def delete(self, id):
        well_to_delete = Well.query.filter_by(id=id).first()

        if well_to_delete:
            db.session.delete(well_to_delete)
            db.session.commit()
            return {'message': 'Well deleted successfully'}, 200
        else:
            return {'error': 'Well does not exist'}, 404
    
    api.add_resource(WellById, '/wells_table/<int:id>')



class AssumptionById(Resource):

    # get assumptions of a specific well by id
    def get(self, id):
        assumptions_to_get = Assumptions.query.filter_by(id=id).first()

        if assumptions_to_get:
            return assumptions_to_get.to_dict(), 200
        else:
            return {'error': 'Assumptions do not exist'}, 404

    # patch specific assumptions for a well by id
    def path(self, id):
        data_to_patch_with = request.get_json()

        try:
            assumption_to_choose = Assumptions.query.filter_by(id=id).first()
            for field in data_to_patch_with:
                setattr(assumption_to_choose, field, data_to_patch_with[field])
            db.session.commit()
            return assumption_to_choose.to_dict(), 200
        except Exception as e:
            print(e)
            return {'error': 'There was an error updating this assumption, it might not exits'}, 400

    def delete(self, id):
        assumption_to_delete = Assumptions.query.filter_by(id=id).first()

        if assumption_to_delete:
            db.session.delete(assumption_to_delete)
            db.session.commit()
            return {'message': 'Assumption deleted successfully'}, 200
        else:
            return {'error': 'Assumption does not exist'}, 404


    api.add_resource(AssumptionById, '/assumptions_table/<int:id>')


# all production curves
class ProductionCurveNorm(Resource):

    # get all production curves
    def get(self):
        production_curves_to_get = ProductionCurve.query.all()

        data = [production_curve.to_dict() for production_curve in production_curves_to_get]

        return data, 200

    # post a new production curve
    def post(self):
        production_curve_to_create = request.get_json()

        try:
            new_production_curve = ProductionCurve(
                type_curve=production_curve_to_create['type_curve']
            )

            db.session.add(new_production_curve)
            db.session.commit()

            return new_production_curve.to_dict(), 201

        except:
            raise Exception('There was an error creating this production curve')

    api.add_resource(ProductionCurveNorm, '/production_curve_table')

class ProductionCurveById(Resource):
    # get a specific production curve by id
    def get(self, id):
        production_curve_to_choose = ProductionCurve.query.filter_by(id=id).first()

        if production_curve_to_choose:
            return production_curve_to_choose.to_dict(), 200
        else:
            return {'error': 'Production curve does not exist'}, 404

    # patch a specific production curve by id
    def patch(self, id):

        data_to_patch_with = request.get_json()

        try:
            production_curve_to_choose = ProductionCurve.query.filter_by(id=id).first()

            for field in data_to_patch_with:
                setattr(production_curve_to_choose, field, data_to_patch_with[field])

            db.session.commit()
            return production_curve_to_choose.to_dict(), 200

        except Exception as e:
            print(e) 
            return {'error': 'There was an error updating this production curve'}, 400


    # delete a specific production curve by id
    def delete(self, id):
        production_curve_to_delete = ProductionCurve.query.filter_by(id=id).first()

        if production_curve_to_delete:
            db.session.delete(production_curve_to_delete)
            db.session.commit()
            return {'message': 'Production curve deleted successfully'}, 200
        else:
            return {'error': 'Production curve does not exist'}, 404
    
    api.add_resource(ProductionCurveById, '/production_curve_table/<int:id>')


class ProjectNorm(Resource):

    # get all projects
    def get(self):
        projects_to_get = Project.query.all()

        data = [project.to_dict() for project in projects_to_get]

        return data, 200

    # post a new project
    def post(self):
        project_to_create = request.get_json()

        try:
            new_project = Project(
                name=project_to_create['name']
            )

            db.session.add(new_project)
            db.session.commit()

            return new_project.to_dict(), 201

        except:
            raise Exception('There was an error creating this project')

    api.add_resource(ProjectNorm, '/projects_table')


class ProjectById(Resource):
    # get a specific project by id
    def get(self, id):
        project_to_choose = Project.query.filter_by(id=id).first()

        if project_to_choose:
            return project_to_choose.to_dict(), 200
        else:
            return {'error': 'Project does not exist'}, 404

    # patch a specific project by id
    def patch(self, id):

        data_to_patch_with = request.get_json()

        try:
            project_to_choose = Project.query.filter_by(id=id).first()

            for field in data_to_patch_with:
                setattr(project_to_choose, field, data_to_patch_with[field])

            db.session.commit()
            return project_to_choose.to_dict(), 200

        except Exception as e:
            print(e) 
            return {'error': 'There was an error updating this project'}, 400


    # delete a specific project by id
    def delete(self, id):
        project_to_delete = Project.query.filter_by(id=id).first()

        if project_to_delete:
            db.session.delete(project_to_delete)
            db.session.commit()
            return {'message': 'Project deleted successfully'}, 200
        else:
            return {'error': 'Project does not exist'}, 404
    
    api.add_resource(ProjectById, '/projects_table/<int:id>')







# @app.route('/')
# def index():
#     return '<h1>Phase 4 Project Server</h1>'

# Views go here! use either route!
# @app.errorhandler(404)
# def not_found(e):
#     return render_template("index.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)

