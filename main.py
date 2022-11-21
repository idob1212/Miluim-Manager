import os
from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date, datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import LoginForm, RegisterForm, CreateReviewForm, CommentForm, EditUserForm, Search_review, EditReviewForm, UpdateDateForm
from flask_gravatar import Gravatar
from werkzeug.datastructures import MultiDict
import sys
import logging



app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)




##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

import logging

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CONFIGURE TABLE


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(1000), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.String(1000), nullable=False)
    qualified = db.Column(db.String(1000), nullable=False)
    qualified_assist = db.Column(db.String(1000), nullable=False)
    madrat = db.Column(db.String(1000), nullable=False)
    qualified_status = db.Column(db.String(1000), nullable=False)
    op_flight_time = db.Column(db.Integer, nullable=False)
    op_flight_time_goal = db.Column(db.Integer, nullable=False)
    tr_flight_time = db.Column(db.Integer, nullable=False)
    tr_flight_time_goal = db.Column(db.Integer, nullable=False)
    guide_flight_time = db.Column(db.Integer, nullable=False)
    coach = db.Column(db.Boolean, nullable=False)
    last_15_date = db.Column(db.Date, nullable=False)
    last_flight_date = db.Column(db.Date, nullable=False)
    reviews = relationship("Review", back_populates="author")


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date = db.Column(db.Date, nullable=False)
    author = relationship("User", back_populates="reviews")
    author_name = db.Column(db.String(250), nullable=False)
    subject = db.Column(db.String(250), nullable=False)
    keep_pts = db.Column(db.Text, nullable=False)
    improve_pts = db.Column(db.Text, nullable=False)
    op_level = db.Column(db.Integer, nullable=False)
    co_op_level = db.Column(db.Integer, nullable=False)


# class Comment(db.Model):
#     __tablename__ = "comments"
#     id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
#     author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     parent_post = relationship("BlogPost", back_populates="comments")
#     comment_author = relationship("User", back_populates="comments")
#     text = db.Column(db.Text, nullable=False)
db.create_all()
#

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def get_all_posts():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    # posts = BlogPost.query.all()
    return render_template("index.html", current_user=current_user)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(id=form.id.data).first():
            print(User.query.filter_by(id=form.id.data).first())
            #User already exists
            flash("משתמש כבר קיים!")
            return redirect(url_for('manage'))

        # hash_and_salted_password = generate_password_hash(
        #     form.password.data,
        #     method='pbkdf2:sha256',
        #     salt_length=8
        # )
        new_user = User(
            id=form.id.data,
            name=form.name.data,
            password=form.password.data,
            status=form.status.data,
            qualified_assist = form.qualified_assist.data,
            guide_flight_time = form.guide_flight_time.data,
            last_15_date = form.last_15_date.data,
            op_flight_time=form.op_flight_time.data,
            tr_flight_time=form.tr_flight_time.data,
            op_flight_time_goal=form.tr_flight_time_goal.data,
            tr_flight_time_goal=form.tr_flight_time_goal.data,
            last_flight_date=form.last_flight_date.data,
            qualified=form.qualified.data,
            madrat=form.madrat.data,
            coach=form.coach.data,
            qualified_status = form.qualified_status.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('manage'))
    return render_template("register.html", form=form, current_user=current_user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        id = form.id.data
        password = form.password.data
        user = User.query.filter_by(id=id).first()
        # Email doesn't exist or password incorrect.
        if not user:
            flash("מספר אישי שגוי")
            return redirect(url_for('login'))
        elif not user.password == password:
            flash('סיסמה לא נכונה')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/new-review", methods=["GET", "POST"])
def add_new_review():
    names = []
    for user in User.query.all():
        if user.name != "מנהל" and user.name!= current_user.name:
            names.append(user.name)
    names.sort()
    form = CreateReviewForm()
    form.subject.choices=names
    if form.validate_on_submit():
        new_review = Review(
            subject=form.subject.data,
            keep_pts=form.keep_pts.data,
            improve_pts=form.improve_pts.data,
            op_level=form.op_level.data,
            co_op_level=form.co_op_level.data,
            author=current_user,
            author_name=current_user.name,
            date=form.last_flight_date.data
        )
        if(current_user.last_flight_date < form.last_flight_date.data and form.last_flight_date.data < date.today()):
            current_user.last_flight_date = form.last_flight_date.data
        flight_type = form.flight_type.data
        if flight_type =="op":
            current_user.op_flight_time += int(form.flight_time.data)
        elif flight_type == "tr":
            current_user.tr_flight_time += int(form.flight_time.data)
        elif flight_type == "gu":
            current_user.guide_flight_time += int(form.flight_time.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form, current_user=current_user)


@app.route('/panel')
@admin_only
def manage():
    users = User.query.all()
    return render_template('panel.html', users=users)

@app.route("/edit-user/<int:user_id>", methods=["GET", "POST"])
@admin_only
def edit_user(user_id):
    user = User.query.get(user_id)
    edit_form = EditUserForm(
        name=user.name,
        op_flight_time=user.op_flight_time,
        tr_flight_time=user.tr_flight_time,
        last_flight_date=user.last_flight_date,
        qualified=user.qualified,
        madrat=user.madrat,
        coach=user.coach,
        qualified_assist = user.qualified_assist,
        op_flight_time_goal = user.op_flight_time_goal,
        tr_flight_time_goal=user.tr_flight_time_goal,
        guide_flight_time = user.guide_flight_time,
        last_15_date = user.last_15_date,
        status = user.status,
        qualified_status = user.qualified_status
    )
    if edit_form.validate_on_submit():
        user.name = edit_form.name.data
        user.op_flight_time = edit_form.op_flight_time.data
        user.tr_flight_time = edit_form.tr_flight_time.data
        user.last_flight_date = edit_form.last_flight_date.data
        user.qualified = edit_form.qualified.data
        user.madrat = edit_form.madrat.data
        user.coach = edit_form.coach.data
        user.qualified_assist = edit_form.qualified_assist.data
        user.op_flight_time_goal = edit_form.op_flight_time_goal.data
        user.tr_flight_time_goal = edit_form.tr_flight_time_goal.data
        user.guide_flight_time = edit_form.guide_flight_time.data
        user.last_15_date = edit_form.last_15_date.data
        db.session.commit()
        return redirect(url_for("manage"))
    return render_template("register.html", form=edit_form,is_edit=True, current_user=current_user)


@app.route("/delete/<int:user_id>")
@admin_only
def delete_post(user_id):
    user_to_delete = User.query.get(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route('/reviews-finder', methods=["GET", "POST"])
@admin_only
def search_reviews():
    form = Search_review()
    if form.validate_on_submit():
        name = form.name.data
        if name == "":
            return redirect(url_for('show_reviews', user_id=0))
        else:
            user = User.query.filter_by(name=form.name.data).first()
            if user:
                return redirect(url_for('show_reviews', user_id=user.id))
            else:
                flash("לא נמצא משתמש")
                return render_template("search.html", form=form)
    return render_template("search.html", form=form)


@app.route("/reviews/<int:user_id>", methods=["GET", "POST"])
@admin_only
def show_reviews(user_id):
    if user_id == 0:
        reviews = Review.query.all()
        return render_template('reviews.html', reviews=reviews, user_id=user_id)
    user = User.query.filter_by(id=user_id).first()
    reviews = Review.query.filter_by(subject=user.name).all()
    return render_template('reviews.html', reviews=reviews, user_id=user_id)


@app.route("/edit-review/<int:review_id>", methods=["GET", "POST"])
@admin_only
def edit_review(review_id):
    review = Review.query.get(review_id)
    id = User.query.filter_by(name=review.subject).first().id
    edit_form = EditReviewForm(
        keep_pts=review.keep_pts,
        improve_pts=review.improve_pts,
        op_level=review.op_level,
        knowledge_level=review.knowledge_level
    )
    if edit_form.validate_on_submit():
        review.keep_pts = edit_form.keep_pts.data
        review.improve_pts = edit_form.improve_pts.data
        review.op_level = edit_form.op_level.data
        review.knowledge_level = edit_form.knowledge_level.data
        db.session.commit()
        return redirect(url_for("search_reviews"))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


@app.route("/delete-review/<int:review_id>")
@admin_only
def delete_review(review_id):
    review_to_delete = Review.query.get(review_id)
    id = User.query.filter_by(name=review_to_delete.subject).first().id
    db.session.delete(review_to_delete)
    db.session.commit()
    return redirect(url_for("search_reviews"))


@app.route("/update-date", methods=["GET", "POST"])
def update_date():
    form = UpdateDateForm(last_15_date=current_user.last_15_date)
    if form.validate_on_submit():
        last_15 = form.last_15_date.data
        current_user.last_15_date = last_15
        db.session.commit()
        return render_template("index.html", current_user=current_user)
    return render_template("update-date.html", form=form, current_user=current_user)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
