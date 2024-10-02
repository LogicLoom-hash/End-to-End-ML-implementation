import pickle

print("Starting test_load.py...")

# Try to load model.pkl
try:
    print("Attempting to load model.pkl...")
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except FileNotFoundError as fnf_error:
    print(f"File not found: {fnf_error}")
except Exception as e:
    print(f"Failed to load model.pkl: {e}")

# Try to load scaling.pkl
try:
    print("Attempting to load scaling.pkl...")
    with open('scaling.pkl', 'rb') as f:
        scalar = pickle.load(f)
    print("Scaler loaded successfully.")
except FileNotFoundError as fnf_error:
    print(f"File not found: {fnf_error}")
except Exception as e:
    print(f"Failed to load scaling.pkl: {e}")

print("Finished test_load.py.")
