from APIModel import APIModel
from TicketView import TicketView
from TicketViewerController import TicketViewerController

import os
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

model = APIModel(config["subdomain"],
                 config["username"], config["api_token"])
view = TicketView()
controller = TicketViewerController()


def test_get_all_tickets_status_code():
    response = model.get_all_tickets()
    assert response.status_code == 200


def test_get_all_tickets_content():
    response = model.get_all_tickets()
    tickets = response.json()["tickets"]

    with open(os.path.join("tests", "all_tickets_test.json")) as f:
        correct_tickets = json.load(f)["tickets"]

    assert tickets == correct_tickets


def test_get_ticket_detail_status_code():
    valid_ticket_id = 10

    response = model.get_ticket_detail(valid_ticket_id)
    assert response.status_code == 200


def test_get_ticket_detail_content():
    valid_ticket_id = 10

    response = model.get_ticket_detail(valid_ticket_id)
    ticket = response.json()

    with open(os.path.join("tests", "10_ticket_detail_test.json")) as f:
        correct_ticket = json.load(f)

    assert ticket == correct_ticket
