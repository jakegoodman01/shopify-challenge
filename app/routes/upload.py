import click
from flask import Blueprint
from flask.cli import with_appcontext
from pynamodb.exceptions import DoesNotExist

from app.errors import NonRetryableError
from app.models.folder import FolderModel
from app.models.image import ImageModel

upload = Blueprint('upload', __name__)


def upload_folder(folder_title) -> None:
    """
    Uploads a new folder to the repository
    Each folder title must be unique
    """
    try:
        FolderModel.get(folder_title)
        raise NonRetryableError(f'Each folder title must be unique: \'{folder_title}\' already exists')
    except DoesNotExist:
        fm = FolderModel(folder_title)
        fm.save()


def upload_image(image_title, folder_title) -> None:
    """
    Uploads a new image to the given folder
    The image title must be unique in the given folder
    """
    fm = FolderModel.get(folder_title)
    if image_title in fm.images:
        raise NonRetryableError(f'Duplicate image in folder: \'{image_title}\' already exists in \'{folder_title}\'')
    im = ImageModel('/'.join([folder_title, image_title]))
    fm.images.append(im.__repr__())
    fm.save()
    im.save()


@upload.cli.command('folder')
@click.argument('folder_title')
@with_appcontext
def upload_folder_command(folder_title) -> None:
    upload_folder(folder_title)


@upload.cli.command('image')
@click.argument('image_title')
@click.argument('folder_title')
@with_appcontext
def upload_image_command(image_title, folder_title) -> None:
    upload_image(image_title, folder_title)
