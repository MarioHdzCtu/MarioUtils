class ConnectionException(Exception):
    """Raised when trying to access a connection that has not been declared
    """
    def __init__(self) -> None:
        super().__init__("The connection has not been properly set up")

class CursorException(Exception):
    """Raised when trying to access a cursos that has not been declared
    """
    def __init__(self) -> None:
        super().__init__("The Cursor has not been properly set up")

class SelectionException(Exception):
    """Raised when a SELECT query does not starts with 'SELECT'
    """
    def __init__(self) -> None:
        super().__init__("The query does not have the proper format. It should start with a 'SELECT' word")

class GroupException(Exception):
    """Raised when a group column is not in the selected columns
    """
    def __init__(self) -> None:
        super().__init__("Every Group column should be in the ")