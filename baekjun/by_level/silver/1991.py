import sys

n = int(sys.stdin.readline())

tree = [[0, 0] for _ in range(n)]

for _ in range(n):
    p, l, r = map(str, sys.stdin.readline().split())
    tree[ord(p) - 65][0], tree[ord(p) - 65][1] = ord(l) - 65, ord(r) - 65

preO = ""


def preorder(node):
    global preO
    preO += chr(node + 65)
    if tree[node][0] >= 0:
        preorder(tree[node][0])
    if tree[node][1] >= 0:
        preorder(tree[node][1])


preorder(0)
print(preO)

inO = ""


def inorder(node):
    global inO
    if tree[node][0] >= 0:
        inorder(tree[node][0])
    inO += chr(node + 65)
    if tree[node][1] >= 0:
        inorder(tree[node][1])


inorder(0)
print(inO)

postO = ""
def postorder(node):
    global postO
    if tree[node][0] >= 0:
        postorder(tree[node][0])
    if tree[node][1] >= 0:
        postorder(tree[node][1])
    postO += chr(node + 65)


postorder(0)
print(postO)
