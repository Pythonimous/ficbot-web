import os
import imghdr

from flask import (
    Blueprint, render_template, request, url_for, current_app
)

import json
from werkzeug.utils import secure_filename
from ficbot.character.name.generation import generate_name

"""
logging.basicConfig(filename=f"logs/generate/{time.time()}.log",
                    format='%(asctime)s %(message)s',
                    level=logging.ERROR)
"""


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


bp = Blueprint('generation', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def render():
    return render_template("generation.html")


@bp.errorhandler(413)
def too_large(e):
    return "File is too large. Only .jpg, .png, .gif up to 2MB are allowed.",\
           413


@bp.route('/upload_image/', methods=('GET', 'POST'))
def upload_image():
    """ Saves the uploaded image and returns in to the client """
    if request.method == 'POST':
        image = request.files['file']
        filename = secure_filename(image.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in current_app.config["UPLOAD_EXTENSIONS"]:
                return "Wrong extension: " \
                       "only .jpg, .png, .gif files are allowed", 415
            if file_ext != validate_image(image.stream):
                return "Broken file: " \
                       "only valid .jpg, .png, .gif files are allowed.\n" \
                       "Please check your image and try again.", 415

            image.save(os.path.join('ficbotweb/static/images', filename))
            image_url = url_for('static', filename=f"images/{filename}")
            return json.dumps({'success': True, 'imgUrl': image_url}), 200,\
                {'ContentType': 'application/json'}
    else:
        return render_template("generation.html")


@bp.route('/name/', methods=('GET', 'POST'))
def name():
    """ Generates the name based on the request image """
    if request.method == 'POST':
        data = request.json
        img_path = f"ficbotweb/{data['imageSrc']}"
        # model = data['model']
        diversity = float(data['diversity'])
        min_name_length = int(data['min_name_length'])
        name = generate_name(img_path,
                             "models/img_name/tf/simple.10-1.98.hdf5",
                             "models/img_name/tf/maps.pkl",
                             diversity=diversity,
                             min_name_length=min_name_length)
        return json.dumps({'success': True, 'name': name}), 200,\
            {'ContentType': 'application/json'}
    else:
        return render_template("generation.html")
