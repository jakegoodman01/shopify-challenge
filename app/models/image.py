from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from app.constants import LOCAL_HOST


class ImageModel(Model):
    """
    A DynamoDB Image
    """
    class Meta:
        table_name = 'Image'
        region = 'us-east-1'
        host = LOCAL_HOST
        aws_access_key_id = "fake_key_id"
        aws_secret_access_key = "fake_access_key"
    path = UnicodeAttribute(hash_key=True)

    def __repr__(self):
        return self.path.split('/')[-1]

