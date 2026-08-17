from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)


def main() -> None:
    """Download the UCI Student Performance dataset and save the math data."""
    student_performance = fetch_ucirepo(id=320)
    features = student_performance.data.features.copy()
    targets = student_performance.data.targets.copy()

    # Keep the mathematics-course data as the first analysis dataset.
    math_data = pd.concat([features, targets], axis=1)
    output_path = DATA_DIR / "student_performance.csv"
    math_data.to_csv(output_path, index=False)

    print(f"Saved {len(math_data)} rows to {output_path}")


if __name__ == "__main__":
    main()
