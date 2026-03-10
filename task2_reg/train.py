from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
TRAIN_PATH = BASE_DIR / "train.csv"
MODEL_PATH = BASE_DIR / "model.joblib"


def train() -> None:
    df = pd.read_csv(TRAIN_PATH)

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        min_samples_leaf=5,
        n_jobs=-1,
        random_state=42,
    )

    model.fit(X_train, y_train)

    valid_preds = model.predict(X_valid)
    rmse = root_mean_squared_error(y_valid, valid_preds)
    print(f"Validation RMSE: {rmse:.4f}")

    # Refit on full training data before saving final model
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train()