from flask import Blueprint, render_template

about_bp = Blueprint('about_bp', __name__)

@about_bp.route('/about')
def about():
    # Skills list as requested
    skills = [
        "Python", "Django", "Flask Framework", "Tailwind CSS", 
        "NodeJS", "Angular Framework", "HTML", "JavaScript", "AutoCAD"
    ]
    return render_template('pages/about.html', skills=skills)
