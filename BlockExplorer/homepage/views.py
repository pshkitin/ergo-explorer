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
