import pickle
import hashlib
from blockchain import Blockchain
import pandas as pd
from train import hash_row

def hash_input(data):
    """
    Hash the input data using SHA-256.
    """
    input_list = [float(x) for x in data.split(",")]
    input_string = ",".join(map(lambda x: f"{x:.1f}" if isinstance(x, float) else str(x), input_list))
    hashed = hashlib.sha256(input_string.encode()).hexdigest()
    print(f"Hashing input: {input_string} -> {hashed}")
    return hashed

def load_model():
    """
    Load the trained model from model.pkl.
    """
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def load_blockchain():
    """
    Recreate the blockchain using the training data.
    """
    blockchain = Blockchain()
    data = pd.read_csv("data.csv")
    X = data.iloc[:, :-1]  # All columns except the last one
    for _, row in X.iterrows():
        hashed_row = hash_row(row)
        blockchain.add_block(hashed_row)
    print("Blockchain recreated with training data.")
    return blockchain

def predict():
    """
    Main function to handle user input, verify data, and make predictions.
    """
    # Load the model and blockchain
    model = load_model()
    blockchain = load_blockchain()

    # Accept user input
    user_input = input("Enter input data (comma-separated values): ").strip()
    hashed_input = hash_input(user_input)
    print(f"User input: {user_input}, Hashed input: {hashed_input}")

    # Verify the input against the blockchain
    if blockchain.verify_data(hashed_input):
        # Convert input to the format expected by the model
        input_data = [float(x) for x in user_input.split(",")]
        input_df = pd.DataFrame([input_data], columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"])
        prediction = model.predict(input_df)
        print(f"Prediction: {prediction[0]}")
    else:
        print("Input data verification failed. Prediction not allowed.")

if __name__ == "__main__":
    predict()