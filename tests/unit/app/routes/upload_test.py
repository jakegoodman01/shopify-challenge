from unittest.mock import patch

import pytest
from pynamodb.exceptions import DoesNotExist

from app.errors import NonRetryableError
from app.models import ImageModel
from app.models.folder import FolderModel
from app.routes.upload import upload_folder_command, upload_image_command


class TestUpload:
    @patch.object(FolderModel, 'get')
    def test_upload_folder_duplicate(self, patch_folder_model_get, default_folder_model, runner):
        # Arrange
        folder_title = default_folder_model.title
        patch_folder_model_get.return_value = default_folder_model
        # Act
        with pytest.raises(NonRetryableError):
            runner.invoke(upload_folder_command, [folder_title], catch_exceptions=False)
        # Assert
        patch_folder_model_get.assert_called_once_with(folder_title)

    @patch.object(FolderModel, 'get')
    @patch.object(FolderModel, 'save')
    def test_upload_folder_success(self, patch_folder_model_save, patch_folder_model_get, default_folder_model, runner):
        # Arrange
        folder_title = default_folder_model.title
        patch_folder_model_get.side_effect = DoesNotExist
        # Act
        runner.invoke(upload_folder_command, [folder_title], catch_exceptions=False)
        # Assert
        patch_folder_model_get.assert_called_once_with(folder_title)
        patch_folder_model_save.assert_called_once()

    @patch.object(FolderModel, 'get')
    @patch.object(FolderModel, 'save')
    @patch.object(ImageModel, 'save')
    def test_upload_image_success(
        self,
        patch_image_model_save,
        patch_folder_model_save,
        patch_folder_model_get,
        default_folder_model,
        default_image_model,
        runner,
    ):
        # Arrange
        folder_title = default_folder_model.title
        image_title = default_image_model.__repr__()
        patch_folder_model_get.return_value = default_folder_model
        # Act
        runner.invoke(upload_image_command, [image_title, folder_title], catch_exceptions=False)
        # Assert
        patch_folder_model_get.assert_called_once_with(folder_title)
        patch_image_model_save.assert_called_once()
        patch_folder_model_save.assert_called_once()
        assert default_folder_model.images[-1] == image_title

    @patch.object(FolderModel, 'get')
    def test_upload_image_duplicate(self, patch_folder_model_get, default_folder_model, default_image_model, runner):
        # Arrange
        folder_title = default_folder_model.title
        image_title = default_image_model.__repr__()
        default_folder_model.images.append(image_title)
        patch_folder_model_get.return_value = default_folder_model
        # Act
        with pytest.raises(NonRetryableError):
            runner.invoke(upload_image_command, [image_title, folder_title], catch_exceptions=False)
        # Assert
        patch_folder_model_get.assert_called_once_with(folder_title)
