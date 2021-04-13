from trello import TrelloApi

class Client:
    """
    Establish a connection
    """
    _connection = None

    def __init__(self, connection: dict) -> None:
        """
        Connection to Trello
        """

        self._connection = TrelloApi(connection['trello_api_key'], connection['trello_api_token'])