import click
from flask import Blueprint
from flask.cli import with_appcontext
from pynamodb.exceptions import DoesNotExist

from app.models.folder import FolderModel
from app.models.image import ImageModel

delete = Blueprint('delete', __name__)


def delete_folder(folder_title) -> None:
    """
    Deletes the given folder and all the images inside of it
    """
    fm = FolderModel.get(folder_title)
    for image_title in fm.images:
        try:
            ImageModel.get(image_title).delete()
        except DoesNotExist:
            pass
    fm.delete()


def delete_image(image_title, folder_title) -> None:
    """
    Deletes the given image from the given folder (if it exists)
    """
    fm = FolderModel.get(folder_title)
    if image_title in fm.images:
        fm.images.remove(image_title)
        fm.save()
        ImageModel.get('/'.join([folder_title, image_title])).delete()


@delete.cli.command('folder')
@click.argument('folder_title')
@with_appcontext
def delete_folder_command(folder_title) -> None:
    delete_folder(folder_title)


@delete.cli.command('image')
@click.argument('image_title')
@click.argument('folder_title')
@with_appcontext
def delete_image_command(image_title, folder_title) -> None:
    delete_image(image_title, folder_title)


@delete.cli.command('all')
@with_appcontext
def delete_all() -> None:
    for fm in FolderModel.scan():
        delete_folder(fm.title)
