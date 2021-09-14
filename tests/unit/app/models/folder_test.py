class TestFolderModel:
    def test_create_folder_model(self, default_folder_model):
        assert default_folder_model.title == 'default-folder'
        assert default_folder_model.images == []

    def test_add_image(self, default_folder_model, default_image_model):
        default_folder_model.images.append(default_image_model)
        assert default_folder_model.images == [default_image_model]

    def test_repr(self, default_folder_model):
        assert repr(default_folder_model) == default_folder_model.title
