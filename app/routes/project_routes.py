from flask import Blueprint, render_template
from app.models.project_model import Project

project_bp = Blueprint('project_bp', __name__)

@project_bp.route('/projects')
def projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('pages/projects.html', projects=projects)
