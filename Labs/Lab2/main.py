def divideMessage(message, m):
    """
    Divides the message into blocks of size m. \n If last block is not a multiple of m, it pads the message with ' '. \n
    :param message: message to be divided
    :param m: size of a block
    :return: list of words divided
    """
    words = [message[i:i + m] for i in range(0, len(message), m)]  # Split the message into blocks of size m
    if len(words[-1]) != m:
        for i in range(0, m - len(words[-1])):
            words[-1] += ' '
    return words


def encrypt(block):
    """
    Encrypts the given block. \n
    :param block: message to be encrypted
    :return: the encrypted block
    """
    permutation = [2, 1, 3]
    result = ''
    for i in range(len(block)):  # For all char positions in the block: 0,1..n-1
        pos = permutation[i]  # We take the position of the char that will be placed on index i from the permutation
        result += block[pos-1]  # We add to the result the character with pos-1 because positioning starts from 0 in python
    return result


def decrypt(block):
    """
    Decrypts the given block. \n
    :param block: message to be decrypted
    :return: the decrypted block
    """
    permutation = [2, 1, 3]
    result = ''
    for i in range(1, len(block)+1):  # For all positions in the block 1,2...n
        pos = permutation.index(i)  # We take the position where index i was placed in the permutation
        result += block[pos]  # We add to the result the character with that obtained position
    return result


if __name__ == '__main__':
    words = divideMessage("Scooby Dooby Dooo", 3)
    print(words)

    # Encrypt message
    ciphertext = ''  # Build ciphertext by:
    for word in words:  # Encrypting every block and adding it to result
        ciphertext += encrypt(word)

    print(ciphertext)

    # Decrypt message
    words1 = divideMessage(ciphertext, 3)
    plaintext = ''  # Build plaintext by:
    for word in words1:  # Decrypting every bloc and adding it to result
        plaintext += decrypt(word)

    print(plaintext)
