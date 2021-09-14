class TestImageModel:
    def test_create_image_model(self, default_image_model):
        assert default_image_model.path == 'default-folder/default_image.jpg'

    def test_repr(self, default_image_model):
        assert repr(default_image_model) == default_image_model.path.split('/')[-1]
