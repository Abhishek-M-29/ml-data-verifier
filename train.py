import pandas as pd
import pickle
import hashlib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from blockchain import Blockchain

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def hash_row(row):
    """
    Hash a single row of data using SHA-256.
    """
    row_string = ",".join(map(lambda x: f"{x:.1f}" if isinstance(x, float) else str(x), row))
    hashed = hashlib.sha256(row_string.encode()).hexdigest()
    print(f"Hashing row: {row_string} -> {hashed}")
    return hashed

def train_model():
    """
    Train a machine learning model and build the blockchain.
    """
    # Load the dataset
    data = pd.read_csv("data.csv")
    
    # Split dataset into features (X) and target (y)
    X = data.iloc[:, :-1]  # All columns except the last one
    y = data.iloc[:, -1]   # The last column

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Build the blockchain
    blockchain = Blockchain()
    for _, row in X_train.iterrows():
        hashed_row = hash_row(row)
        blockchain.add_block(hashed_row)
        print(f"Training row: {row}, Hash: {hashed_row}")

    # Save the trained model
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)

    print("Model trained and saved as model.pkl.")
    for block in blockchain.chain:
        print(f"Block {block.index}: {block.data}")
    print("Blockchain created with training data.")

if __name__ == "__main__":
    train_model()