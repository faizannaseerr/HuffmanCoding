class BinaryTree:
    def __init__(self, c, d, l , r):
        self.Char = c
        self.Data = d
        self.Left = l
        self.Right = r


#input_message = "BCCABBDDAECCBBAEDDCC"
#input_message = "hello there friend!"
input_message = "big bob bites bananas"
characters_dict = {}

for character in input_message:
    if character in characters_dict:
        characters_dict[character] += 1
    else:
        characters_dict[character] = 1
print(characters_dict)

input_count_array = sorted(characters_dict.values())
input_characters_array = []
for value in input_count_array:
    for key in characters_dict:
        if characters_dict[key] == value and key not in input_characters_array:
            input_characters_array.append(key)

print(input_count_array)
print(input_characters_array)

"""MaxHeap.append(BinaryTree(input_array[0], None, None))
count += 1
MaxHeap.append(BinaryTree(input_array[1], None, None))
count += 1
MaxHeap.append(BinaryTree(input_array[count - 1] + input_array[count - 2], MaxHeap[count - 2], MaxHeap[count - 1]) """

#Use recursion
## parameter for function should be array of binary trees.

MaxHeap = []
input_tree = []
for x in range (len(input_count_array)):
    input_tree.append(BinaryTree(input_characters_array[x], input_count_array[x], 0, 0))

def CreateMaxHeap(input_tree):
    if len(input_tree) == 2:
        MaxHeap.append(BinaryTree(None, input_tree[0].Data + input_tree[1].Data, input_tree[0], input_tree[1]))
        return
    else:
        MaxHeap.append(input_tree[0])
        MaxHeap.append(input_tree[1])
        root = BinaryTree(None, input_tree[0].Data + input_tree[1].Data, input_tree[0], input_tree[1])
        MaxHeap.append(root)
        input_tree.pop(0)
        input_tree.pop(0)
        count = 0
        while count < len(input_tree) and input_tree[count].Data < root.Data:
            count += 1
        input_tree.insert(count, root)
        CreateMaxHeap(input_tree)

CreateMaxHeap(input_tree)

for node in MaxHeap:
    LeftNode = node.Left
    RightNode = node.Right
    print(node.Data, " ")
    if LeftNode == 0:
        print(0, " ", 0, "\n")
    else:
        print(LeftNode.Data, " ", RightNode.Data, "\n")

#DFS or BFS
def FindCode (key, code, root, flag):
    """TraversalQueue = []
    TraversalQueue.append(root)
    while len(TraversalQueue) > 0:
    Current = TraversalQueue.pop(0)
    if Current.Data == value:
        return code"""

    if root.Left == 0 and root.Right == 0:
        if root.Char == key:
            return code, True
        else:
            return code[:-1], False


    code, flag = FindCode(key, code + "1", root.Right, flag)

    if flag:
        return code, flag

    code, flag = FindCode(key, code + "0", root.Left, flag)

    if flag:
        return code, flag
    else:
        return code[:-1], flag



#duplicates are giving the same code, thus pass code dict as parameter






def EncodeMessage(input_message, characters_dict):
    character_to_code_dict = {}
    root = MaxHeap[len(MaxHeap) - 1]
    for key in characters_dict:
        code, flag= FindCode(key,  "", root, False)
        character_to_code_dict[key] = code
    #print characters_to_code_dict here
    print(character_to_code_dict)
    EncodedMessage = ""
    for char in input_message:
        EncodedMessage += character_to_code_dict[char]
    return EncodedMessage

encoded_input_message = EncodeMessage(input_message, characters_dict)
print(encoded_input_message)

def DecodeMessage(encoded_input_message):
    root = MaxHeap[len(MaxHeap) - 1]
    decoded_message = ""
    for bit in encoded_input_message:
        if bit == "0":
            root = root.Left
        else:
            root = root.Right
        if root.Left == 0 and root.Right == 0:
            decoded_message += root.Char
            root = MaxHeap[len(MaxHeap) - 1]
    return decoded_message


decoded_message = DecodeMessage(encoded_input_message)
print(decoded_message)
print(decoded_message == input_message)
print(len(encoded_input_message))
