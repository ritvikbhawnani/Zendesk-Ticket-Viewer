import requests


class APIModel:
    """
    The APIModel class interacts with the Zendesk API

    Args:
        subdomain (str): subdomain of the Zendesk account
        username (str): username of the Zendesk account
        api_token (str): api_token of the Zendesk account

    Attributes:
        tickets (dict): this is where store the ticket data
        subdomain (str): this is where we store the subdomain
        username (str): this is where we store the username
        api_token (str): this is where we store the api_token
    """

    def __init__(self, subdomain, username, api_token):
        self.ticket = {}
        self.subdomain = subdomain
        self.username = username
        self.api_token = api_token

    def get_all_tickets(self):
        """
        Sends request to the Zendesk API for all tickets

        Returns:
            list of tickets (list of dicts)
        """

        response = requests.get(f'https://{self.subdomain}.zendesk.com/api/v2/tickets.json', auth=(
            f'{self.username}/token', self.api_token))

        return response

    def get_ticket_detail(self, ticket_id):
        """
        Sends request to the Zendesk API for the ticket associated with
        ticket_id

        Args:
            ticket_id (int): ID associated with a ticket

        Returns:
            ticket (dict)
        """
        response = requests.get(f'https://{self.subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json', auth=(
            f'{self.username}/token', self.api_token))

        return response
