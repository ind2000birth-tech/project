from flask import Blueprint, render_template
from app.models.experience_model import Experience

experience_bp = Blueprint('experience_bp', __name__)

@experience_bp.route('/experience')
def experience():
    experiences = Experience.query.order_by(Experience.created_at.desc()).all()
    return render_template('pages/experience.html', experiences=experiences)
