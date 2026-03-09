from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user_model import User
from app.models.experience_model import Experience
from app.models.project_model import Project
from app.models.reference_model import Reference
from app.models.contact_model import Contact
from app.services.auth_service import AuthService
from app.services.database_service import DatabaseService
from app.extensions import db

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_bp.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = AuthService.authenticate_admin(username, password)
        if user:
            login_user(user)
            return redirect(url_for('admin_bp.dashboard'))
        flash('Invalid username or password', 'danger')
        
    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_bp.index'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    experience_count = Experience.query.count()
    project_count = Project.query.count()
    reference_count = Reference.query.count()
    message_count = Contact.query.count()
    return render_template('admin/dashboard.html', 
                           experience_count=experience_count,
                           project_count=project_count,
                           reference_count=reference_count,
                           message_count=message_count)

# Experience CRUD
@admin_bp.route('/experience')
@login_required
def experience_list():
    experiences = Experience.query.order_by(Experience.created_at.desc()).all()
    return render_template('admin/experience.html', experiences=experiences)

@admin_bp.route('/experience/add', methods=['POST'])
@login_required
def add_experience():
    job_title = request.form.get('job_title')
    company = request.form.get('company')
    duration = request.form.get('duration')
    description = request.form.get('description')
    
    new_exp = Experience(job_title=job_title, company=company, duration=duration, description=description)
    DatabaseService.add_item(new_exp)
    flash('Experience added successfully', 'success')
    return redirect(url_for('admin_bp.experience_list'))

@admin_bp.route('/experience/edit/<int:id>', methods=['POST'])
@login_required
def edit_experience(id):
    exp = Experience.query.get_or_404(id)
    exp.job_title = request.form.get('job_title')
    exp.company = request.form.get('company')
    exp.duration = request.form.get('duration')
    exp.description = request.form.get('description')
    DatabaseService.update_item()
    flash('Experience updated successfully', 'success')
    return redirect(url_for('admin_bp.experience_list'))

@admin_bp.route('/experience/delete/<int:id>')
@login_required
def delete_experience(id):
    exp = Experience.query.get_or_404(id)
    DatabaseService.delete_item(exp)
    flash('Experience deleted successfully', 'success')
    return redirect(url_for('admin_bp.experience_list'))

# Project CRUD
@admin_bp.route('/projects')
@login_required
def project_list():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('admin/projects.html', projects=projects)

@admin_bp.route('/projects/add', methods=['POST'])
@login_required
def add_project():
    title = request.form.get('title')
    description = request.form.get('description')
    github_link = request.form.get('github_link')
    live_demo_link = request.form.get('live_demo_link')
    image_url = request.form.get('image_url')
    
    new_project = Project(title=title, description=description, github_link=github_link, 
                         live_demo_link=live_demo_link, image_url=image_url)
    DatabaseService.add_item(new_project)
    flash('Project added successfully', 'success')
    return redirect(url_for('admin_bp.project_list'))

@admin_bp.route('/projects/edit/<int:id>', methods=['POST'])
@login_required
def edit_project(id):
    proj = Project.query.get_or_404(id)
    proj.title = request.form.get('title')
    proj.description = request.form.get('description')
    proj.github_link = request.form.get('github_link')
    proj.live_demo_link = request.form.get('live_demo_link')
    proj.image_url = request.form.get('image_url')
    DatabaseService.update_item()
    flash('Project updated successfully', 'success')
    return redirect(url_for('admin_bp.project_list'))

@admin_bp.route('/projects/delete/<int:id>')
@login_required
def delete_project(id):
    proj = Project.query.get_or_404(id)
    DatabaseService.delete_item(proj)
    flash('Project deleted successfully', 'success')
    return redirect(url_for('admin_bp.project_list'))

# Reference CRUD
@admin_bp.route('/references')
@login_required
def reference_list():
    references = Reference.query.order_by(Reference.created_at.desc()).all()
    return render_template('admin/references.html', references=references)

@admin_bp.route('/references/add', methods=['POST'])
@login_required
def add_reference():
    name = request.form.get('name')
    job_role = request.form.get('job_role')
    email = request.form.get('email')
    phone = request.form.get('phone')
    
    new_ref = Reference(name=name, job_role=job_role, email=email, phone=phone)
    DatabaseService.add_item(new_ref)
    flash('Reference added successfully', 'success')
    return redirect(url_for('admin_bp.reference_list'))

@admin_bp.route('/references/edit/<int:id>', methods=['POST'])
@login_required
def edit_reference(id):
    ref = Reference.query.get_or_404(id)
    ref.name = request.form.get('name')
    ref.job_role = request.form.get('job_role')
    ref.email = request.form.get('email')
    ref.phone = request.form.get('phone')
    DatabaseService.update_item()
    flash('Reference updated successfully', 'success')
    return redirect(url_for('admin_bp.reference_list'))

@admin_bp.route('/references/delete/<int:id>')
@login_required
def delete_reference(id):
    ref = Reference.query.get_or_404(id)
    DatabaseService.delete_item(ref)
    flash('Reference deleted successfully', 'success')
    return redirect(url_for('admin_bp.reference_list'))

# Messages
@admin_bp.route('/messages')
@login_required
def message_list():
    messages = Contact.query.order_by(Contact.created_at.desc()).all()
    return render_template('admin/messages.html', messages=messages)

@admin_bp.route('/messages/delete/<int:id>')
@login_required
def delete_message(id):
    msg = Contact.query.get_or_404(id)
    DatabaseService.delete_item(msg)
    flash('Message deleted successfully', 'success')
    return redirect(url_for('admin_bp.message_list'))
