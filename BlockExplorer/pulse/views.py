import time
from django.shortcuts import render
import requests
from django.http import JsonResponse
from pulse.tree import getNodeState
# Create your views here.


def pulse(request):
    # State = {
    #     "peer1": 0,
    #     "peer2": 0,
    #     "peer3": 0,
    #     "peer4": 0,
    # }
    # State["peer1"] = int(time.time() / 20) % 4
    # if State["peer1"] == 1:
    #     State["peer2"] = 0
    #     State["peer3"] = 0
    #     State["peer4"] = 0
    # if State["peer1"] == 2:
    #     State["peer2"] = 1
    #     State["peer3"] = 2
    #     State["peer4"] = 0
    # if State["peer1"] == 3:
    #     State["peer2"] = 3
    #     State["peer3"] = 2
    #     State["peer4"] = 2
    # deadNodeList = requests.get(
    #     "http://88.198.13.202:9051/peers/connected").json()
    # activeNodeList = requests.get("http://88.198.13.202:9051/peers/all").json()
    # parent_address = "88.198.13.202"

    # stub = {
    #     "nodes": [
    #         {"id": "One", "group": State["peer1"]},
    #         {"id": "Two", "group": State["peer2"]},
    #         {"id": "Three", "group": State["peer3"]},
    #         {"id": "Four", "group": State["peer4"]}
    #     ],
    #     "links": [
    #         {"source": "One", "target": "Two", "value": 10},
    #         {"source": "Two", "target": "Three", "value": 10},
    #         {"source": "Three", "target": "One", "value": 10},
    #         {"source": "Two", "target": "Four", "value": 10}
    #     ]
    # }
    resp = JsonResponse(getNodeState("159.203.94.149"))
    resp['Access-Control-Allow-Origin'] = '*'
    return resp
