from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from app.models.contact_model import Contact
from app.models.reference_model import Reference
from app.services.database_service import DatabaseService
from app.services.email_service import EmailService

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('All fields are required!', 'danger')
        else:
            new_contact = Contact(name=name, email=email, message=message)
            if DatabaseService.add_item(new_contact):
                # Send email notification
                EmailService.send_contact_email(name, email, message)
                flash('Your message has been sent successfully!', 'success')
                return redirect(url_for('contact_bp.contact'))
            else:
                flash('An error occurred while saving your message. Please try again.', 'danger')
            
    return render_template('pages/contact.html')

@contact_bp.route('/api/references')
def get_references():
    references = Reference.query.all()
    return jsonify([{
        'name': r.name,
        'email': r.email,
        'phone': r.phone
    } for r in references])
