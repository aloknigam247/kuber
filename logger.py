"""Module: logger """

class Logger:
    """ Log generator

        Support error, info, wait and warning messages
    """

    def error(message: str):
        """ Generates error messages

        Args:
            message (str): message to log
        """
        print("|ERROR|", message)

    def info(message: str):
        """ Generates info messages

        Args:
            message (str): message to log
        """
        print("|INFO|", message)
        
    def wait(message: str):
        """ Generates wait messages

        Args:
            message (str): message to log
        """
        print(message, "...")

    def warn(message: str):
        """ Generates warn messages

        Args:
            message (str): message to log
        """
        print("|WARNING|", message)