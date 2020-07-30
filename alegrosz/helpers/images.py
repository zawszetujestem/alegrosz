import os
from datetime import datetime
from secrets import token_hex

from werkzeug.utils import secure_filename


base_dir = os.path.join(os.path.dirname(__file__), "..", "..", "uploads")


def save_image_upload(image):
    print(image)
    format = "%Y%m%dT%H%M%S"
    now = datetime.utcnow().strftime(format)
    random_string = token_hex(2)
    filename = f"{random_string}_{now}_{image.filename}"
    filename = secure_filename(filename)
    image.save(os.path.join(base_dir, filename))
    return filename
