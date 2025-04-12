import pickle
import hashlib
from blockchain import Blockchain

def hash_input(data):
    """
    Hash the input data using SHA-256.
    """
    return hashlib.sha256(data.encode()).hexdigest()

def load_model():
    """
    Load the trained model from model.pkl.
    """
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def load_blockchain():
    """
    Load the blockchain from a saved state or recreate it.
    """
    # For simplicity, assume the blockchain is recreated here.
    # You can extend this to load a saved blockchain state.
    blockchain = Blockchain()
    return blockchain

def predict():
    """
    Main function to handle user input, verify data, and make predictions.
    """
    # Load the model and blockchain
    model = load_model()
    blockchain = load_blockchain()

    # Accept user input
    user_input = input("Enter input data (comma-separated values): ")
    hashed_input = hash_input(user_input)

    # Verify the input against the blockchain
    if blockchain.verify_data(hashed_input):
        # Convert input to the format expected by the model
        input_data = [float(x) for x in user_input.split(",")]
        prediction = model.predict([input_data])
        print(f"Prediction: {prediction[0]}")
    else:
        print("Input data verification failed. Prediction not allowed.")

if __name__ == "__main__":
    predict()