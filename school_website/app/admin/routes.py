import os
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.admin import admin_bp
from app.models import Admin, Message, News, Topper, Event, Teacher, Gallery
from app.forms import LoginForm, NewsForm, TopperForm, EventForm, TeacherForm, GalleryForm, MessageForm

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('admin.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/login.html', title='Sign In', form=form)

@admin_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

# Manage Principal's Message
@admin_bp.route('/manage/principal_message', methods=['GET', 'POST'])
@login_required
def manage_principal_message():
    message = Message.query.filter_by(type='principal').first()
    form = MessageForm(obj=message)
    if form.validate_on_submit():
        if message:
            message.message = form.message.data
        else:
            message = Message(type='principal', message=form.message.data)
            db.session.add(message)
        db.session.commit()
        flash('Principal\'s message has been updated.')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/manage_message.html', form=form, title="Principal's Message")

# Manage Vice Principal's Message
@admin_bp.route('/manage/vp_message', methods=['GET', 'POST'])
@login_required
def manage_vp_message():
    message = Message.query.filter_by(type='vice_principal').first()
    form = MessageForm(obj=message)
    if form.validate_on_submit():
        if message:
            message.message = form.message.data
        else:
            message = Message(type='vice_principal', message=form.message.data)
            db.session.add(message)
        db.session.commit()
        flash('Vice Principal\'s message has been updated.')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/manage_message.html', form=form, title="Vice Principal's Message")

# Manage News
@admin_bp.route('/manage/news', methods=['GET', 'POST'])
@login_required
def manage_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News(title=form.title.data, content=form.content.data)
        db.session.add(news)
        db.session.commit()
        flash('News has been added.')
        return redirect(url_for('admin.manage_news'))
    all_news = News.query.all()
    return render_template('admin/manage_news.html', form=form, all_news=all_news)

# Manage Toppers
@admin_bp.route('/manage/toppers', methods=['GET', 'POST'])
@login_required
def manage_toppers():
    form = TopperForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        topper = Topper(name=form.name.data, year=form.year.data, percentage=form.percentage.data, photo=filename)
        db.session.add(topper)
        db.session.commit()
        flash('Topper has been added.')
        return redirect(url_for('admin.manage_toppers'))
    toppers = Topper.query.all()
    return render_template('admin/manage_toppers.html', form=form, toppers=toppers)

# Manage Events
@admin_bp.route('/manage/events', methods=['GET', 'POST'])
@login_required
def manage_events():
    form = EventForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        event = Event(title=form.title.data, description=form.description.data, date=form.date.data, photo=filename)
        db.session.add(event)
        db.session.commit()
        flash('Event has been added.')
        return redirect(url_for('admin.manage_events'))
    events = Event.query.all()
    return render_template('admin/manage_events.html', form=form, events=events)

# Manage Teachers
@admin_bp.route('/manage/teachers', methods=['GET', 'POST'])
@login_required
def manage_teachers():
    form = TeacherForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        teacher = Teacher(name=form.name.data, subject=form.subject.data, qualifications=form.qualifications.data, photo=filename)
        db.session.add(teacher)
        db.session.commit()
        flash('Teacher has been added.')
        return redirect(url_for('admin.manage_teachers'))
    teachers = Teacher.query.all()
    return render_template('admin/manage_teachers.html', form=form, teachers=teachers)

# Manage Gallery
@admin_bp.route('/manage/gallery', methods=['GET', 'POST'])
@login_required
def manage_gallery():
    form = GalleryForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        gallery = Gallery(caption=form.caption.data, photo=filename)
        db.session.add(gallery)
        db.session.commit()
        flash('Image has been added to the gallery.')
        return redirect(url_for('admin.manage_gallery'))
    images = Gallery.query.all()
    return render_template('admin/manage_gallery.html', form=form, images=images)
