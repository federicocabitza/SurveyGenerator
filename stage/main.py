import os
import datetime
import subprocess
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_wtf import FlaskForm
from wtforms import TextAreaField, MultipleFileField, SubmitField, SelectField
from wtforms import SelectMultipleField, StringField, IntegerField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired, Optional, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'csv', 'xlsx', 'lsg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def validate_six_digits( form, field ):
    if field.data is not None:
        if not ( 100000 <= field.data <= 999999 ):
            raise ValidationError( 'The integer must be exactly 6 digits.' )

class UploadFileForm( FlaskForm ):
    files = MultipleFileField("Select Files", validators=[InputRequired()])

    admin_name = StringField( "Admin Name", validators=[Optional()])
    admin_email = StringField( "Admin Email", validators=[InputRequired()])
    survey_id = IntegerField( "Survey ID", validators=[Optional(), validate_six_digits])
    primary_language = SelectField( "Base Language",
                        choices=[('en', 'English'), ('it', 'Italian')],
                        validators=[InputRequired()])
    secondary_languages = SelectMultipleField( "Other Languages",
                        choices=[('en', 'English'), ('it', 'Italian'), ('fr', 'French'), ('de', 'German'), ('es', 'Spanish'), ('nl', 'Dutch') ],
                        validators=[Optional()])
    survey_title = StringField( "Title", validators=[InputRequired()])
    survey_description = TextAreaField( "Description", validators=[InputRequired()])
    survey_welcometext = TextAreaField( "Welcome Message", validators=[Optional()])
    survey_endtext = TextAreaField( "End Message", validators=[Optional()])
    survey_alias = StringField( "Alias", validators=[Optional()])
    iterate_group = IntegerField( "Iterate Files", validators=[InputRequired()] )

    submit = SubmitField("Upload File")



@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        files = form.files.data #Grab the files
        filenames = []

        admin_name = form.admin_name.data
        admin_email = form.admin_email.data
        survey_id = form.survey_id.data
        primary_language = form.primary_language.data
        secondary_languages = form.secondary_languages.data
        survey_title = form.survey_title.data
        survey_description = form.survey_description.data
        survey_welcometext = form.survey_welcometext.data
        survey_endtext = form.survey_endtext.data
        survey_alias = form.survey_alias.data
        iterate_group = form.iterate_group.data

        for file in files:
            filename = secure_filename( file.filename )
            if allowed_file(filename):
                ospath = os.path.abspath(os.path.dirname(__file__))
                file.save(os.path.join(ospath, app.config['UPLOAD_FOLDER'], filename))
                filenames.append(filename)
            else:
                flash(f'File "{filename} has an invalid extension. Only .txt, .csv, .xlsx, .lsg file are allowed"')
                return redirect(request.url)

        return redirect( url_for('run_script',
                        filenames=','.join(filenames),
                        admin_name = admin_name if admin_name is not None else "",
                        admin_email = admin_email,
                        survey_id = survey_id,
                        primary_language = primary_language,
                        survey_title = survey_title,
                        survey_description = survey_description,
                        survey_welcometext = survey_welcometext,
                        survey_endtext = survey_endtext,
                        survey_alias = survey_alias,
                        iterate_group = iterate_group,
                        secondary_languages = ','.join(secondary_languages) if secondary_languages is not None else None
                        ))

    return render_template('index.html', form=form)

@app.route('/run_script')
def run_script():
    filenames = request.args.get('filenames').split(',')
    admin_email = request.args.get('admin_email', '')
    admin_name = request.args.get('admin_name')
    survey_id = request.args.get('survey_id')
    primary_language = request.args.get('primary_language')
    survey_title = request.args.get('survey_title')
    survey_description = request.args.get('survey_description')
    survey_welcometext = request.args.get('survey_welcometext')
    survey_endtext = request.args.get('survey_endtext')
    survey_alias = request.args.get('survey_alias')
    secondary_languages = request.args.get('secondary_languages')
    iterate_group = request.args.get('iterate_group')

    if not secondary_languages or secondary_languages == "" or secondary_languages == "['']":
        secondary_languages = []
    else:
        secondary_languages = secondary_languages.split(',')

    filepaths = [os.path.join(app.config['UPLOAD_FOLDER'], filename) for filename in filenames]

    try:
        result = subprocess.run(
                ['python3', 'process_files.py', admin_email, admin_name, str(survey_id), primary_language,
                survey_title, survey_description, survey_welcometext, survey_endtext, survey_alias, iterate_group] +
                secondary_languages + filepaths, #passa i file caricati come argomenti
                capture_output = True, text = True, check = True
        )

        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        generated_file = f"Survey_{today_date}.txt"

        return send_file( generated_file, as_attachment=True, download_name=os.path.basename( generated_file ))

    except subprocess.CalledProcessError as e:
        return f"Error executing script: <br>{e.stderr}"

if __name__ == '__main__':
    app.run(debug=True)
