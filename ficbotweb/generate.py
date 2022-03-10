import functools
import logging
import time

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.utils import secure_filename
from ficbot.tf_models.name.generation import generate_name

"""
logging.basicConfig(filename=f"logs/generate/{time.time()}.log",
                    format='%(asctime)s %(message)s',
                    level=logging.ERROR)
"""
bp = Blueprint('generate', __name__, url_prefix='/generate')


@bp.route('/img_name', methods=('GET', 'POST'))
def img_to_name():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'img-char' not in request.files:
            flash('No file part')
            return redirect(request.url)
        image = request.files['img-char']
        diversity = float(request.form['diversity'])
        error = None

        if not image:
            error = f"{__name__}: Please provide an image."

        filename = 'ficbotweb/static/images/' + str(secure_filename(image.filename))
        image.save(filename)

        if error is None:
            # try:
            name = generate_name(filename,
                                 "models/img_name/tf/simple.10-1.98.hdf5",
                                 "models/img_name/tf/maps.pkl",
                                 diversity=diversity)
            """
            except Exception as e:
                error = f"{__name__}: {str(e)}"
                logging.error(error)
            """
            return render_template("generate/img_name.html",
                                   char_image=url_for('static', filename=f"images/{image.filename}"),
                                   generated_name=name)
        flash(error)

    return render_template("generate/img_to_name.html")
