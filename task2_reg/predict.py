from pathlib import Path
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"
TEST_PATH = BASE_DIR / "hidden_test.csv"
OUTPUT_PATH = BASE_DIR / "predictions.csv"


def predict() -> None:
    """Load the trained model and generate predictions for the hidden test set."""
    print("--- Prediction Phase ---")

    model = joblib.load(MODEL_PATH)
    test_df = pd.read_csv(TEST_PATH)
    predictions = model.predict(test_df)

    pd.DataFrame(predictions).to_csv(OUTPUT_PATH, index=False, header=False)
    print(f"Done! Predictions saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    predict()