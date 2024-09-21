# Title: McCulloch-Pitts Neuron in Soft Computing

def mcculloch_pitts_neuron(weights, threshold, inputs):
    # Weighted sum
    weighted_sum = sum(w * inp for w, inp in zip(weights, inputs))
    # Apply the threshold to the weighted sum
    output = 1 if weighted_sum >= threshold else 0
    return output


# Logical operations as McCulloch-Pitts neurons
def AND(input1, input2):
    weights = [1, 1]
    threshold = 2
    return mcculloch_pitts_neuron(weights, threshold, [input1, input2])


def OR(input1, input2):
    weights = [1, 1]
    threshold = 1
    return mcculloch_pitts_neuron(weights, threshold, [input1, input2])


def NOT(input1):
    weights = [-1]
    threshold = 0
    return mcculloch_pitts_neuron(weights, threshold, [input1])


def XOR(input1, input2):
    # XOR can be implemented using a combination of AND, OR, and NOT
    return OR(AND(input1, NOT(input2)), AND(NOT(input1), input2))


def ANDNOT(input1, input2):
    return AND(input1, NOT(input2))


# Main function to run the program
def main():
    print("Select the operation you want to perform:")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. ANDNOT")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 3:
        input1 = int(input("Enter input (0 or 1): "))
        output = NOT(input1)
        print(f"NOT({input1}) = {output}")
    else:
        input1 = int(input("Enter input 1 (0 or 1): "))
        input2 = int(input("Enter input 2 (0 or 1): "))

        if choice == 1:
            output = AND(input1, input2)
            print(f"AND({input1}, {input2}) = {output}")
        elif choice == 2:
            output = OR(input1, input2)
            print(f"OR({input1}, {input2}) = {output}")
        elif choice == 4:
            output = XOR(input1, input2)
            print(f"XOR({input1}, {input2}) = {output}")
        elif choice == 5:
            output = ANDNOT(input1, input2)
            print(f"ANDNOT({input1}, {input2}) = {output}")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
