import functools
import logging
import time
import sys
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

import json
from werkzeug.utils import secure_filename
from ficbot.tf_models.name.generation import generate_name

from requests_toolbelt.multipart import decoder

"""
logging.basicConfig(filename=f"logs/generate/{time.time()}.log",
                    format='%(asctime)s %(message)s',
                    level=logging.ERROR)
"""

bp = Blueprint('generation', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def render():
    return render_template("generation.html")


@bp.route('/upload_image/', methods=('GET', 'POST'))
def upload_image():
    if request.method == 'POST':
        image = request.files['file']
        if image.filename == '':
            flash('No selected file')
            return redirect(request.url)
        image.save(os.path.join('ficbotweb/static/images', image.filename))
        image_url = url_for('static', filename=f"images/{image.filename}")
        return json.dumps({'success': True, 'imgUrl': image_url}), 200, {'ContentType': 'application/json'}
    else:
        return render_template("generation.html")


@bp.route('/name/', methods=('GET', 'POST'))
def name():
    if request.method == 'POST':
        data = request.json
        img_path = f"ficbotweb/{data['imageSrc']}"
        # model = data['model']
        diversity = float(data['diversity'])
        name = generate_name(img_path,
                             "models/img_name/tf/simple.10-1.98.hdf5",
                             "models/img_name/tf/maps.pkl",
                             diversity=diversity)
        return json.dumps({'success': True, 'name': name}), 200, {'ContentType': 'application/json'}
    else:
        return render_template("generation.html")