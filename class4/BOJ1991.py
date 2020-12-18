import sys


class Tree:
    def __init__(self, value):
        self.center = value
        self.left = '.'
        self.right = '.'


def preorder(node):
    print(node.center, end='')
    if node.left != '.':
        preorder(tree_dic[node.left])
    if node.right != '.':
        preorder(tree_dic[node.right])


def inorder(node):
    if node.left != '.':
        inorder(tree_dic[node.left])
    print(node.center, end='')
    if node.right != '.':
        inorder(tree_dic[node.right])


def postorder(node):
    if node.left != '.':
        postorder(tree_dic[node.left])
    if node.right != '.':
        postorder(tree_dic[node.right])
    print(node.center, end='')


sys.stdin = open('input.txt')

input = sys.stdin.readline

tree_dic = dict()

N = int(input())
for _ in range(N):
    node, l, r = input().split()
    if node not in tree_dic:
        tree_dic[node] = Tree(node)

    current_tree = tree_dic[node]
    current_tree.left = l
    current_tree.right = r
preorder(tree_dic['A'])
print()
inorder(tree_dic['A'])
print()
postorder(tree_dic['A'])
