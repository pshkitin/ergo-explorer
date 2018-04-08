from django.shortcuts import render
import requests
# from django.Http import HttpResponse
# Create your views here.


def homepage(request):
    a = requests.get("http://88.198.13.202:9051/blocks/lastHeaders/5")
    blocklist = a.json()
    lastBlocksInfo = []
    for block in blocklist:
        lastBlocksInfo.append({
            "height": block["height"],
            "id": block["id"],
            "timestamp": block["timestamp"],
            "difficulty": block["difficulty"]
        })
    # print(lastBlocksInfo[0]["difficulty"])
    # print(blocklist)
    return render(request, 'homepage/index.html', context={"blocklist": lastBlocksInfo})


def blockinfo(request):
    # blockId = 0
    blockId = request.GET["id"]
    txlist = [{"id":0}]
    block = requests.get("http://88.198.13.202:9051/blocks/" +blockId+"/transactions").json()
    print(block)
    return render(request,'homepage/blockInfo.html', context = {"txlist": block,
    "blockId":blockId})

def graph(request):
    return render(request,'homepage/egro.html')