from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreateReviewForm(FlaskForm):
    subject = SelectField("שם המוערך", validators=[DataRequired()])
    keep_pts = StringField("נקודות לשימור", validators=[DataRequired()])
    improve_pts = StringField("נקודות לשיפור", validators=[DataRequired()])
    op_level = SelectField("רמת הפעלה", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    knowledge_level = SelectField("רמת ידע מקצועי", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    submit = SubmitField("הוסף חוות דעת")

class EditReviewForm(FlaskForm):
    keep_pts = StringField("נקודות לשימור", validators=[DataRequired()])
    improve_pts = StringField("נקודות לשיפור", validators=[DataRequired()])
    op_level = SelectField("רמת הפעלה", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    knowledge_level = SelectField("רמת ידע מקצועי", choices=[(4, '4'), (5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')], validators=[DataRequired()])
    submit = SubmitField("ערוך חוות דעת")

class RegisterForm(FlaskForm):
    id = IntegerField("מספר אישי", validators=[DataRequired()])
    password = PasswordField("סיסמה", validators=[DataRequired()])
    name = StringField("שם מלא", validators=[DataRequired()])
    op_flight_time = StringField("שעות טיסה מבצעיות", validators=[DataRequired()])
    tr_flight_time = StringField("שעות טיסת אימון", validators=[DataRequired()])
    last_flight_date = StringField("תאריך טיסה אחרונה", validators=[DataRequired()])
    qualified = StringField("כשירות", validators=[DataRequired()])
    madrat = StringField("מדרט", validators=[DataRequired()])
    coach = StringField("מאמן", validators=[DataRequired()])

    submit = SubmitField("הוסף משתמש")

class EditUserForm(FlaskForm):
    name = StringField("שם מלא", validators=[DataRequired()])
    op_flight_time = StringField("שעות טיסה מבצעיות", validators=[DataRequired()])
    tr_flight_time = StringField("שעות טיסת אימון", validators=[DataRequired()])
    last_flight_date = StringField("תאריך טיסה אחרונה", validators=[DataRequired()])
    qualified = StringField("כשירות", validators=[DataRequired()])
    madrat = StringField("מדרט", validators=[DataRequired()])
    coach = StringField("מאמן", validators=[DataRequired()])
    submit = SubmitField("השלם עריכה")


class LoginForm(FlaskForm):
    id = StringField("מספר אישי", validators=[DataRequired()])
    password = PasswordField("סיסמה", validators=[DataRequired()])
    submit = SubmitField("התחבר")

class Search_review(FlaskForm):
    name = StringField("הקלד את שם המשתמש עליו תרצה לקרוא חוות דעת")
    submit = SubmitField("חפש")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
