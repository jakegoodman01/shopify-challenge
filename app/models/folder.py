from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute

from app.constants import LOCAL_HOST


class FolderModel(Model):
    """
    A DynamoDB Folder
    """
    class Meta:
        table_name = 'Folder'
        region = 'us-east-1'
        host = LOCAL_HOST
        aws_access_key_id = "fake_key_id"
        aws_secret_access_key = "fake_access_key"
    title = UnicodeAttribute(hash_key=True)
    images = ListAttribute(default=[])

    def __repr__(self):
        return self.title
