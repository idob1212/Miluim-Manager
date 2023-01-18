from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, BooleanField, FloatField
from wtforms.validators import DataRequired, URL, NumberRange, InputRequired
from wtforms.fields.html5 import DateField
from flask_ckeditor import CKEditorField


##WTForm
class CreateReviewForm(FlaskForm):
    subject = SelectField("שם המוערך", validators=[DataRequired()])
    keep_pts = StringField("נקודות לשימור")
    improve_pts = StringField("נקודות לשיפור")
    op_level = SelectField("רמת הפעלה", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    co_op_level = SelectField("עבודת צוות", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    last_flight_date = DateField("תאריך טיסה",render_kw={'max':datetime.today() + timedelta(1)},validators=[DataRequired("זהו סעיף חובה")])
    flight_type = SelectField("סוג טיסה", choices=[("op", 'מבצעית'), ("tr", 'אימון'),("gu", 'הדרכה')], validators=[DataRequired()])
    flight_time = SelectField("שעות טיסה", choices=[(0, '0'),(0.5, '0.5'), (1, '1'), (1.5, '1.5'),(2, '2'),(2.5, '2.5'),(3, '3'),(3.5, '3.5'),(4, '4'),(4.5, '4.5'),(5, '5'),(5.5, '5.5'),(6, '6'),(6.5, '6.5'), (7,'7'), (7.5,'7.5'),(8,'8'), (8.5,'8.5'),(9,'9'),(9.5,'9.5'),(10,'10'),(10.5,'10.5'), (11,'11'), (11.5,'11.5'), (12, '12')], validators=[DataRequired()])
    submit = SubmitField("סיים טיסה")

class EditReviewForm(FlaskForm):
    keep_pts = StringField("נקודות לשימור")
    improve_pts = StringField("נקודות לשיפור")
    op_level = SelectField("רמת הפעלה", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    co_op_level = SelectField("עבודת צוות", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    last_flight_date = DateField("תאריך טיסה ",render_kw={'max':datetime.today() + timedelta(1)}, validators=[DataRequired("זהו סעיף חובה")])
    flight_type = SelectField("סוג טיסה", choices=[("op", 'מבצעית'), ("tr", 'אימון'),("gu", 'הדרכה')], validators=[DataRequired()])
    flight_time = SelectField("שעות טיסה", choices=[(0, '0'),(0.5, '0.5'), (1, '1'), (1.5, '1.5'),(2, '2'),(2.5, '2.5'),(3, '3'),(3.5, '3.5'),(4, '4'),(4.5, '4.5'),(5, '5'),(5.5, '5.5'),(6, '6'),(6.5, '6.5'), (7,'7'), (7.5,'7.5'),(8,'8'), (8.5,'8.5'),(9,'9'),(9.5,'9.5'),(10,'10'),(10.5,'10.5'), (11,'11'), (11.5,'11.5'), (12, '12')], validators=[DataRequired()])
    submit = SubmitField("סיים טיסה")

class RegisterForm(FlaskForm):
    id = IntegerField("מספר אישי", validators=[DataRequired("זהו סעיף חובה")])
    password = PasswordField("סיסמה", validators=[DataRequired("זהו סעיף חובה")])
    name = StringField("שם מלא", validators=[DataRequired("זהו סעיף חובה")])
    status = StringField("סטטוס", validators=[DataRequired("זהו סעיף חובה")])
    qualified = StringField("כשירות", validators=[DataRequired("זהו סעיף חובה")])
    qualified_status = StringField("סטטוס הסמכה", validators=[DataRequired("זהו סעיף חובה")])
    op_flight_time = FloatField("שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    op_flight_time_goal = FloatField("יעד שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time = FloatField("שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time_goal = FloatField("יעד שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    guide_flight_time = FloatField("שעות טיסת הדרכה", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    last_15_date = DateField("כוננות 15' אחרונה", render_kw={'max':datetime.today() + timedelta(1)}, validators=[DataRequired("זהו סעיף חובה")])
    last_flight_date = DateField("תאריך טיסה אחרונה ", render_kw={'max':datetime.today() + timedelta(1)}, validators=[DataRequired("זהו סעיף חובה")])
    coach = BooleanField( "ביצע מאמן" ,render_kw={'style':'margin:10px'})
    qualified_assist = BooleanField("כשירות סיוע",render_kw={'style':'margin:10px'})
    madrat = BooleanField('מדר"ט',render_kw={'style':'margin:10px'})
    submit = SubmitField("הוסף משתמש")

class EditUserForm(FlaskForm):
    name = StringField("שם מלא", validators=[DataRequired("זהו סעיף חובה")])
    status = StringField("סטטוס", validators=[DataRequired("זהו סעיף חובה")])
    qualified = StringField("כשירות", validators=[DataRequired("זהו סעיף חובה")])
    qualified_status = StringField("סטטוס הסמכה", validators=[DataRequired("זהו סעיף חובה")])
    op_flight_time = FloatField("שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    op_flight_time_goal = FloatField("יעד שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time = FloatField("שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time_goal = FloatField("יעד שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    guide_flight_time = FloatField("שעות טיסת הדרכה", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    last_15_date = DateField("כוננות 15' אחרונה ",render_kw={'max':datetime.today() + timedelta(1)}, validators=[DataRequired("זהו סעיף חובה")])
    last_flight_date = DateField("תאריך טיסה אחרונה ",render_kw={'max':datetime.today() + timedelta(1)}, validators=[DataRequired("זהו סעיף חובה")])
    coach = BooleanField( "ביצע מאמן" ,render_kw={'style':'margin:10px'})
    qualified_assist = BooleanField("כשירות סיוע",render_kw={'style':'margin:10px'})
    madrat = BooleanField('מדר"ט',render_kw={'style':'margin:10px'})
    submit = SubmitField("השלם עריכה")


class LoginForm(FlaskForm):
    id = StringField("שם משתמש", validators=[DataRequired()])
    password = PasswordField("סיסמה", validators=[DataRequired()])
    submit = SubmitField("התחבר")

class Search_review(FlaskForm):
    name = StringField("הקלד את שם המשתמש עליו תרצה לקרוא חוות דעת (השאר ריק כדי לראות את כל חוות הדעת)")
    submit = SubmitField("חפש")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

class UpdateDateForm (FlaskForm):
    last_15_date = DateField("כוננות 15' אחרונה",render_kw={'max':datetime.today() + timedelta(1)}, validators=[DataRequired("זהו סעיף חובה")])
    submit = SubmitField("עדכן")