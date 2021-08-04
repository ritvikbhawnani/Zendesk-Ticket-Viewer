from models import APIModel
from views import TicketView
from dotenv import dotenv_values


class TicketViewerController:
    """
    Accepts user input and delgates presentation to the view 
    and data handling to the model

    Args:
        model (object): model or data manager of the application
        view (object): view or presenter of the application
    """

    def __init__(self, model, view):

        self.model = model
        self.view = view
        self.has_quit = False
        self.config = dotenv_values(".env")

    def get_input(self):
        """
        Gets user input

        """

        pass

    def display_all_tickets(self):
        """
        Fetches all the tickets from the model and passes it to the 
        view

        """

        pass

    def display_ticket_detail(self, ticket_id):
        """
        Fetches the details of a ticket with the corresponding 
        ticket_id and passes it to the view

        Args:
            ticket_id (int): ID associated with a ticket
        """
        pass

    def display_error_message(self):
        """
        Passes appropriate error messages to the view

        """

        pass

    def start_ticket_viewer(self):
        """
        Starts the Zendesk Ticket Viewer

        """

        # prompts user until they decide to quit
        while not self.has_quit:
            self.get_input()


# initializes the controller and starts the Zendesk Ticket Viewer
if __name__ == "__main__":
    controller = TicketViewerController(APIModel, TicketView)
    controller.start_ticket_viewer()
