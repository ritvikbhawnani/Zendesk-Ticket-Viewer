from datetime import datetime


class TicketView:
    """
    The TicketView presents the data to the user

    """

    def display_menu(self):
        """
        Displays the menu of available options

        """
        print("Menu Options:")
        print("  ENTER 1 to display all tickets")
        print("  ENTER 2 to display a single ticket by ID")
        print("  ENTER q to quit the program")
        print("  ENTER m to display the menu")
        print()

    def display_ticket_helper(self, id, status, priority, created_at):
        print("{:<15} {:<15} {:<15} {:<25}".format(
            str(id), str(status), str(priority), str(created_at)))

    def display_goodbye_message(self):
        """
        Displays a thank you message

        """

        print("Goodbye")

    def display_all_tickets(self, tickets):
        """
        Displays all the tickets

        """

        print("all tickets")

    def display_ticket_detail(self, ticket):
        """
        Displays the details of a single ticket

        """

        print("{:<15} {:<15} {:<15} {:<25}".format(
            'Ticket ID', 'Status', 'Priority', 'Created At'))

        created_at = ticket["created_at"]
        created_at = datetime.fromisoformat(created_at[:-1])
        created_at = created_at.strftime('%Y-%m-%d')

        self.display_ticket_helper(ticket["id"], ticket["status"],
                                   ticket["priority"], created_at)

        print()

    def display_error_message(self, error_message):
        """
        Displays error messages

        """

        print(error_message)
