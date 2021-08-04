import controllers
from models.APIModel import APIModel
from views.TicketView import TicketView
from controllers.TicketViewerController import TicketViewerController

import os
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

model = APIModel(config["subdomain"],
                 config["username"], config["api_token"])
view = TicketView()
controller = TicketViewerController(model, view)


def test_get_all_tickets():
    tickets = model.get_all_tickets()

    with open(os.path.join("tests", "all_tickets_test.json")) as f:
        correct_tickets = json.load(f)["tickets"]

    assert tickets == correct_tickets


def test_get_ticket_detail():
    ticket_id = 10

    ticket = model.get_ticket_detail(ticket_id)

    with open(os.path.join("tests", "10_ticket_detail_test.json")) as f:
        correct_ticket = json.load(f)

    assert ticket == correct_ticket
