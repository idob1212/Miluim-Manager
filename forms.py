from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, URL, NumberRange, InputRequired
from wtforms.fields.html5 import DateField
from flask_ckeditor import CKEditorField


##WTForm
class CreateReviewForm(FlaskForm):
    subject = SelectField("שם המוערך", validators=[DataRequired()])
    keep_pts = StringField("נקודות לשימור", validators=[DataRequired()])
    improve_pts = StringField("נקודות לשיפור", validators=[DataRequired()])
    op_level = SelectField("רמת הפעלה", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    co_op_level = SelectField("עבודת צוות", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    last_flight_date = DateField("תאריך טיסה", validators=[DataRequired("זהו סעיף חובה")])
    flight_type = SelectField("סוג טיסה", choices=[("op", 'מבצעית'), ("tr", 'אימון'),("gu", 'הדרכה')], validators=[DataRequired()])
    flight_time = SelectField("שעות טיסה", choices=[(0, '0'), (1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'), (7,'7'), (8,'8'),(9,'9'),(10,'10'), (11,'11'), (12, '12')], validators=[DataRequired()])
    submit = SubmitField("הוסף חוות דעת")

class EditReviewForm(FlaskForm):
    keep_pts = StringField("נקודות לשימור", validators=[DataRequired()])
    improve_pts = StringField("נקודות לשיפור", validators=[DataRequired()])
    op_level = SelectField("רמת הפעלה", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    co_op_level = SelectField("עבודת צוות", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    last_flight_date = DateField("תאריך טיסה ", validators=[DataRequired("זהו סעיף חובה")])
    flight_type = SelectField("סוג טיסה", choices=[("op", 'מבצעית'), ("tr", 'אימון'),("gu", 'הדרכה')], validators=[DataRequired()])
    flight_time = SelectField("שעות טיסה", choices=[(0, '0'), (1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'), (7,'7'), (8,'8'),(9,'9'),(10,'10'), (11,'11'), (12, '12')], validators=[DataRequired()])
    submit = SubmitField("ערוך חוות דעת")

class RegisterForm(FlaskForm):
    id = IntegerField("מספר אישי", validators=[DataRequired("זהו סעיף חובה")])
    password = PasswordField("סיסמה", validators=[DataRequired("זהו סעיף חובה")])
    name = StringField("שם מלא", validators=[DataRequired("זהו סעיף חובה")])
    status = StringField("סטטוס", validators=[DataRequired("זהו סעיף חובה")])
    qualified = StringField("כשירות", validators=[DataRequired("זהו סעיף חובה")])
    qualified_assist = StringField("כשירות סיוע", validators=[DataRequired("זהו סעיף חובה")])
    madrat = StringField('מדר"ט', validators=[DataRequired("זהו סעיף חובה")])
    qualified_status = StringField("סטטוס הסמכה", validators=[DataRequired("זהו סעיף חובה")])
    op_flight_time = IntegerField("שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    op_flight_time_goal = IntegerField("יעד שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time = IntegerField("שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time_goal = IntegerField("יעד שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    guide_flight_time = IntegerField("שעות טיסת הדרכה", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    last_15_date = DateField("כוננות 15' אחרונה", validators=[DataRequired("זהו סעיף חובה")])
    last_flight_date = DateField("תאריך טיסה אחרונה ", validators=[DataRequired("זהו סעיף חובה")])
    coach = BooleanField("ביצע מאמן")
    submit = SubmitField("הוסף משתמש")

class EditUserForm(FlaskForm):
    name = StringField("שם מלא", validators=[DataRequired("זהו סעיף חובה")])
    status = StringField("סטטוס", validators=[DataRequired("זהו סעיף חובה")])
    qualified = StringField("כשירות", validators=[DataRequired("זהו סעיף חובה")])
    qualified_assist = StringField("כשירות סיוע", validators=[DataRequired("זהו סעיף חובה")])
    madrat = StringField('מדר"ט', validators=[DataRequired("זהו סעיף חובה")])
    qualified_status = StringField("סטטוס הסמכה", validators=[DataRequired("זהו סעיף חובה")])
    op_flight_time = IntegerField("שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    op_flight_time_goal = IntegerField("יעד שעות טיסה מבצעיות", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time = IntegerField("שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    tr_flight_time_goal = IntegerField("יעד שעות טיסת אימון", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    guide_flight_time = IntegerField("שעות טיסת הדרכה", validators=[InputRequired("זהו סעיף חובה"), NumberRange(min=-1, max=100000)])
    last_15_date = DateField("כוננות 15' אחרונה ", validators=[DataRequired("זהו סעיף חובה")])
    last_flight_date = DateField("תאריך טיסה אחרונה ", validators=[DataRequired("זהו סעיף חובה")])
    coach = BooleanField("ביצע מאמן")
    submit = SubmitField("השלם עריכה")


class LoginForm(FlaskForm):
    id = StringField("מספר אישי", validators=[DataRequired()])
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
    last_15_date = DateField("כוננות 15' אחרונה", validators=[DataRequired("זהו סעיף חובה")])
    submit = SubmitField("עדכן")