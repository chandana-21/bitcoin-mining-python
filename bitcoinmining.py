# Current difficulty level for bitcoin mining is 20
from hashlib import sha256
import time
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    for nonce in range(MAX_NONCE):
        prefix_str = '0'*prefix_zeros
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Hurray! You have successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Sorry! Couldn't find the correct hash after trying for {MAX_NONCE} times")

if __name__ == "__main__":

    transactions="""
    cassian -> nesta -> 20,
    yennefer -> geralt -> 40
    """

    difficulty = 4
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(SHA256(new_hash))
