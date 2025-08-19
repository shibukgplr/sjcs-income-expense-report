from flask import render_template
from app.public import public_bp
from app.models import Message, News, Topper, Event, Teacher, Gallery

@public_bp.route('/')
def index():
    news = News.query.order_by(News.created_at.desc()).limit(5).all()
    return render_template('public/index.html', news=news)

@public_bp.route('/about')
def about():
    principal_message = Message.query.filter_by(type='principal').first()
    vp_message = Message.query.filter_by(type='vice_principal').first()
    return render_template('public/about.html', principal_message=principal_message, vp_message=vp_message)

@public_bp.route('/toppers')
def toppers():
    toppers = Topper.query.order_by(Topper.year.desc()).all()
    return render_template('public/toppers.html', toppers=toppers)

@public_bp.route('/activities')
def activities():
    events = Event.query.order_by(Event.date.desc()).all()
    return render_template('public/activities.html', events=events)

@public_bp.route('/teachers')
def teachers():
    teachers = Teacher.query.all()
    return render_template('public/teachers.html', teachers=teachers)

@public_bp.route('/contact')
def contact():
    return render_template('public/contact.html')
