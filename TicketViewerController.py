from dotenv import dotenv_values
from TicketView import TicketView
from APIModel import APIModel


class TicketViewerController:
    """
    Accepts user input and delgates presentation to the view 
    and data handling to the model

    """

    def __init__(self):

        self.config = dotenv_values(".env")
        self.model = APIModel(
            self.config["subdomain"], self.config["username"], self.config["api_token"])
        self.view = TicketView()
        self.input = None

    def get_input(self):
        """
        Gets user input

        """

        self.view.display_menu()
        self.input = input("Enter Menu Option: ")
        pass

    def display_all_tickets(self):
        """
        Fetches all the tickets from the model and passes it to the 
        view

        """

        self.model.get_all_tickets()
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
        while True:
            self.get_input()

            if not self.input or self.input[0] == "q":
                self.view.display_goodbye_message()
                break
            elif self.input.isdigit():
                if int(self.input) == 1:
                    response = self.model.get_all_tickets()
                    error_message = self.check_response(response)

                    if error_message:
                        self.view.display_error_message(error_message)
                        continue

                    self.view.display_all_tickets(response.json()["tickets"])

                if int(self.input) == 2:
                    ticket_id = input("Enter Ticket ID: ")

                    if not (ticket_id and ticket_id.isdigit() and int(ticket_id) >= 0):
                        self.view.display_error_message(
                            "ID must be a postive integer. Please try again.")
                        continue

                    response = self.model.get_ticket_detail(ticket_id)
                    error_message = self.check_response(response)

                    if error_message:
                        self.view.display_error_message(error_message)
                        continue

                    self.view.display_ticket_detail(response.json()["ticket"])

    def check_response(self, response):
        if response.status_code == 200:
            return None

        if response.status_code == 401:
            return "Could not authenticate you. Please try again."

        return "We could not find the ticket(s) you were looking for"


# initializes the controller and starts the Zendesk Ticket Viewer
if __name__ == "__main__":
    controller = TicketViewerController()
    controller.start_ticket_viewer()
