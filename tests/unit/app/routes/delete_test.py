from unittest.mock import patch, MagicMock

from app import FolderModel
from app.models import ImageModel
from app.routes.delete import delete_folder_command, delete_image_command


class TestDelete:
    @patch.object(FolderModel, 'get')
    @patch.object(FolderModel, 'delete')
    @patch.object(ImageModel, 'get')
    def test_delete_folder(
        self,
        patch_image_model_get,
        patch_folder_model_delete,
        patch_folder_model_get,
        default_folder_model,
        runner
    ):
        # Arrange
        default_folder_model.images = ['i1.jpg', 'i2.jpg']
        patch_folder_model_get.return_value = default_folder_model
        # Act
        runner.invoke(delete_folder_command, ['folder'], catch_exceptions=False)
        # Assert
        patch_folder_model_get.assert_called_once_with('folder')
        patch_image_model_get.assert_called()
        patch_folder_model_delete.assert_called_once()

    @patch.object(FolderModel, 'get')
    @patch.object(ImageModel, 'get')
    def test_delete_image(self, patch_image_model_get, patch_folder_model_get, default_folder_model, runner):
        default_folder_model.images = ['image']
        patch_folder_model_get.return_value = default_folder_model
        runner.invoke(delete_image_command, ['image', 'folder'], catch_exceptions=False)
        patch_folder_model_get.assert_called_once_with('folder')
        patch_image_model_get.assert_called()
