class ApiError(Exception):
    def __init__(self, status_code: int, description: str):
        self.status_code = status_code
        self.description = description


class NotFoundError(ApiError):
    def __init__(self, description):
        super().__init__(404, description)


class NonRetryableError(ApiError):
    def __init__(self, description):
        super().__init__(422, description)