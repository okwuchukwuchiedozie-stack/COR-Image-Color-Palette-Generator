import os
from datetime import datetime, UTC
from dotenv import load_dotenv
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mailman import Mail, EmailMessage


load_dotenv()


bootstrap = Bootstrap5()
mail = Mail()


class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')


def extract_top_colors(image_file, num_colors=10, delta=24):

    img = Image.open(image_file).convert('RGB')

    img.thumbnail((300, 300))

    img_array = np.array(img)

    pixels = img_array.reshape(-1, 3)

    if len(pixels) == 0:
        return []

    quantized_pixels = (pixels // delta) * delta

    unique_colors, counts = np.unique(quantized_pixels, axis=0, return_counts=True)

    total_pixels = len(pixels)
    percentages = counts / total_pixels

    sorted_indices = np.argsort(counts)[::-1]

    top_colors = []

    for i in sorted_indices[:num_colors]:
        rgb = unique_colors[i]
        hex_code = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        pct = float(percentages[i])

        top_colors.append({
            "hex": hex_code,
            "rgb": tuple(map(int, rgb)),
            "percentage": round(pct * 100, 2)
        })

    return top_colors


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

    bootstrap.init_app(app)
    mail.init_app(app)

    @app.context_processor
    def inject_current_year():

        return {'current_year': datetime.now(UTC).year}

    @app.route('/', methods=['GET', 'POST'])
    def index():

        if request.method == 'POST':
            if 'image' not in request.files:
                flash('No image asset element found inside the upload pipeline.', 'danger')

                return redirect(request.url)

            file = request.files['image']

            if file.filename == '':
                flash('No distinct file selected for upload processing.', 'danger')

                return redirect(request.url)

            if file:
                try:
                    delta_val = int(request.form.get('delta', 24))
                    delta_val = max(1, min(255, delta_val))

                    colors = extract_top_colors(file.stream, num_colors=10, delta=delta_val)

                    return render_template('index.html', colors=colors, delta=delta_val)

                except Exception as error:
                    flash(f'An error occurred while analyzing the image matrix: {str(error)}', 'danger')

                    return redirect(request.url)

        return render_template('index.html', colors=None, delta=24)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():

        form = ContactForm()
        if form.validate_on_submit():
            try:

                subject = f"New Studio Inquiry from {form.name.data}"
                body = f"Name: {form.name.data}\nEmail: {form.email.data}\n\nMessage:\n{form.message.data}"

                msg = EmailMessage(
                    subject=subject,
                    body=body,
                    to=[app.config['MAIL_USERNAME']]
                )

                msg.send()

                flash(f'Thank you, {form.name.data}! Your message has been sent to our team.', 'success')
                return redirect(url_for('index'))

            except Exception as e:
                flash(f"Failed to dispatch message details due to a mail server error: {str(e)}", 'danger')

                return redirect(url_for('contact'))

        return render_template('contact.html', form=form)

    return app


if __name__ == '__main__':
    application = create_app()
    application.run(debug=True)
