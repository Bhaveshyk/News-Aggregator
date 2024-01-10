from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from .models import User, Prefrences, News
from . import db
from .constants import CATEGORIES, SITE_MAP
from .helper import utils

views = Blueprint('views', __name__)

@views.route('/dumpusers')
def dumpusers():
    gmail_addresses = [
        'bytegeek@gmail.com',
        'codemaster@gmail.com',
        'techwhiz@gmail.com',
        'cybergeek@gmail.com',
        'digitech@gmail.com',
        'gadgetguru@gmail.com',
        'innovatorx@gmail.com',
        'computernerd@gmail.com',
        'robotlover@gmail.com',
        'cybersleuth@gmail.com',
        'techsavvy@gmail.com',
        'datapioneer@gmail.com',
        'codehacker@gmail.com',
        'techjunkie@gmail.com',
        'techiegenius@gmail.com',
        'geekgirl@gmail.com',
        'cyberspacepro@gmail.com',
        'digitalwizard@gmail.com',
        'hackermind@gmail.com',
        'technomaster@gmail.com'
    ]
    password = 'Geeks12@'
    for email in gmail_addresses:
        new_user = User(email=email, password=generate_password_hash(password), isadmin=False)
        db.session.add(new_user)
        db.session.commit()
    print(User.query.all())
    return redirect(url_for('auth.logout'))

@views.route('/')
@login_required
def home():
    cats = Prefrences.query.filter_by(user_id=current_user.id).all()
    return redirect('/national')

@views.route('/account', methods=['GET', 'POST'])
@login_required
def pref():
    if request.method == 'POST':
        add_pref = request.form.get('add')
        rem_pref = request.form.get('rem')

        if add_pref != 'Choose a preference':
            prefs = Prefrences(cat=add_pref, user_id=current_user.id)
            db.session.add(prefs)
            db.session.commit()

        if not rem_pref == 'Choose a preference':
            prefs = Prefrences.query.filter_by(user_id=current_user.id)
            for item in prefs:
                if item.cat == rem_pref:
                    db.session.delete(item)
                    db.session.commit()
        
    cats = Prefrences.query.filter_by(user_id=current_user.id).all()
    rem_cats = [item.cat for item in cats]
    add_cats = list(set(CATEGORIES).symmetric_difference(set(rem_cats)))

    return render_template('pref.html', user=current_user, add_cats=add_cats, rem_cats=rem_cats, preferences=cats)

@views.route('/<string:category>')
@login_required
def news_cat(category):
    cats = Prefrences.query.filter_by(user_id=current_user.id).all()
    category = category.title()
    news = News.query.filter_by(category=category).all()
    math = (len(news) // 2) - ((len(news) // 2) % 3)
    news = news[:math]
    # for i in range(len(news) // 2):
    #     print(news[i].news)
    # print(len(news))
    return render_template('index.html', user=current_user, preferences=cats, data=news, papers=SITE_MAP[category])

@views.route('/admin')
@login_required
def admin_panel():
    if not current_user.isadmin:
        return 'You cannot access this page', 404
    cats = Prefrences.query.filter_by(user_id=current_user.id).all()
    users = User.query.all()
    return render_template('panel.html', user=current_user, users=users, preferences=cats)

@views.route('/make_admin/<int:id>')
@login_required
def make_admin(id):
    id = int(id)
    user = User.query.filter_by(id=id).first()
    user.isadmin = True
    db.session.commit()
    return redirect(url_for('views.admin_panel'))

@views.route('/remove_admin/<int:id>')
@login_required
def remove_admin(id):
    id = int(id)
    user = User.query.filter_by(id=id).first()
    user.isadmin = False
    db.session.commit()
    return redirect(url_for('views.admin_panel'))

@views.route('/delete_user/<int:id>')
@login_required
def delete_user(id):
    id = int(id)
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('views.admin_panel'))

@views.route('/api/<string:category>')
def api(category):
    result = []
    records = News.query.filter_by(category=category.title()).all()
    print(len(records))
    for record in records:
        temp = {
            'headline': record.news,
            'source': record.link,
            'site': record.site
        }
        result.append(temp)
    data = {
        'category': category,
        'data': result
    }
    return jsonify(data)

# @views.route('/xyz')
# def xyz():
#     news = News.query.all()
#     print(len(news))
#     return '<p></p>'