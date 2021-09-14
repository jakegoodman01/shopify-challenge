import click
from flask import Blueprint
from flask.cli import with_appcontext

from app.models import ImageModel
from app.models.folder import FolderModel

get = Blueprint('get', __name__)


@get.cli.command('folders')
@with_appcontext
def get_folders() -> None:
    click.echo([f for f in FolderModel.scan()])


@get.cli.command('images')
@with_appcontext
def get_images() -> None:
    click.echo([f.path for f in ImageModel.scan()])


@get.cli.command('image_from_folder')
@click.argument('folder_name')
@with_appcontext
def get_images_from_folder(folder_name) -> None:
    fm = FolderModel.get(folder_name)
    click.echo(f'{folder_name}: {[img for img in fm.images]}')


@get.cli.command('overview')
@with_appcontext
def get_overview() -> None:
    output_str = ''
    folder_models = list(FolderModel.scan())
    if len(folder_models) < 1:
        output_str += 'No active folders\n'
    else:
        for fm in folder_models:
            output_str += f'{fm.title}: {[img for img in fm.images]}\n'
    click.echo(output_str)
