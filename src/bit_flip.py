 # a function to accept 0 or 1 and turn it into the three bit repetiting code
import random

def encode(bit):
    return(bit,bit,bit)

# a function to introduce errors on the three bit repetition code
def error(code):
    for i in range(3):
        if random.random() < 0.1:  # 10% chance to flip each bit
            code[i] ^= 1  # Flip the bit
    return code 

# a function to obtain syndromes
def syndrome(code):
    s1= code[0] ^ code[1]
    s2= code[1] ^ code[2]
    if s1==0 and s2==0:
        return -1
    elif s1==1 and s2==0:
        return 0
    elif s1==1 and s2==1:
        return 1
    elif s1==0 and s2==1:
        return 2
    
# a function to correct the error based on the syndrome
def correct(code):
    syn=syndrome(code)
    if syn != -1:
        code[syn] ^= 1
    return code

# a function to decode the three bit repetition code back to a single bit
def decode(code):
    if code.count(1) > code.count(0):
        return 1
    else:
        return 0 

if __name__ == "__main__":
    Num_trials=10
    success_count=0
    bit= 0
    for _ in range(Num_trials):
        encoded= encode(bit)
        errored= error(list(encoded))  # Convert tuple to list for mutability
        corrected= correct(errored)
        decoded= decode(corrected)
        if decoded != bit:
            print(f"Failure in trial with original bit {bit}. Decoded: {decoded}")
        else:
            print(f"Success in trial with original bit {bit}. Decoded: {decoded}")
            success_count += 1
    print(f"Success rate: {success_count/Num_trials*100}%")

            