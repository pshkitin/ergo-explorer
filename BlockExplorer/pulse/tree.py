import requests
from pulse.models import nodeListCache
from datetime import datetime,timedelta
def getNodes(_root):
    nodes = []
    stack = [Node(_root)]
    links = []
    # TODO: add cache query
    cache = nodeListCache.objects.filter(validTill__gte = datetime.now()).values()
    # print(str(cache[0]["nodes"]))
    if len(cache)>0:
        print("cache used")
        print(str(cache[0]["nodes"]))
        return cache[0]["nodes"]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        if cur_node not in nodes:
            nodes.append(cur_node)
        children = cur_node.get_children(nodes)
        for child in children:
            links.append({"source":cur_node.id, "target":child.id, "value":10})
            stack.append(child)
    nodeList = []
    for node in nodes:
        nodeList.append({"id": node.id, "group": 0})
    result = {"nodes":nodeList, "links":links}
    cache = nodeListCache(nodes = result, validTill = datetime.now() + timedelta(seconds = 60) )
    cache.save()
    return {"nodes":nodeList, "links":links}
def getNodeState(_root):
    nodeList = getNodes(_root)
    # print(nodeList["links"])
    result = {"nodes":[], "links":nodeList["links"]}
    for node in nodeList["nodes"]:
        group = "0"
        if node["id"][:1] != "_":
            group = requests.get("http://" + node["id"] + ":9051/info").json()["fullHeight"]
        result["nodes"].append({"id":node["id"], "group":group})
    return result
class Node(object):
    def __init__(self, id_):
        self.id = id_
        self.children = []
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        return NotImplemented
    def __repr__(self):
        return self.id

    def add_child(self, node):
        self.children.append(node)

    def get_children(self, exclude):
        children = []
        if self.id[:1] != "_":
            peerList = requests.get("http://" + self.id + ":9051/peers/all").json()
            for peer in peerList:
                newChild = Node(peer["address"].split("/")[1].split(":")[0])
                if newChild not in exclude:
                    children.append(newChild)
            connectedList = requests.get("http://" + self.id + ":9051/peers/connected").json()
            for connectedPeer in connectedList:
                connectedChild = Node("_" + connectedPeer["name"])
                if connectedChild not in exclude:
                    children.append(connectedChild)
        return children

########################################################################
# if __name__ == "__main__":
#     # root = 
#     print(getNodes("159.203.94.149"))
