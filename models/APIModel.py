class APIModel:
    """
    The APIModel class interacts with the Zendesk API

    Args:
        subdomain (str): subdomain of the Zendesk account
                username (str): username of the Zendesk account
                password (str): password of the Zendesk account

        Attributes:
                tickets (dict): this is where store the ticket data
                subdomain (str): this is where we store the subdomain
                username (str): this is where we store the username
                password (str): this is where we store the password
    """

    def __init__(self, subdomain, username, password):
        self.ticket = {}
        self.subdomain = subdomain
        self.username = username
        self.password = password

    def get_all_tickets(self):
        """
        Sends request to the Zendesk API for all tickets

        Returns:
            list of tickets (list of dicts)
        """
        pass

    def get_ticket_detail(self, ticket_id):
        """
        Sends request to the Zendesk API for the ticket associated with
        ticket_id

        Args:
            ticket_id (int): ID associated with a ticket

        Returns:
            ticket (dict)
        """
        pass
