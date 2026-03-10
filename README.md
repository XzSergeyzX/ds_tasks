# DS Engineer Test Task

This repository contains solutions for the ML/DS test tasks.

The project uses **uv** for fast Python dependency management.

## Project Structure
- `task1_isl/` - Task 1: Counting islands (DFS algorithm)
- `task2_reg/` - Task 2: Tabular data regression (EDA, Train, Predict)
- `task3_archtr/` - Task 3: OOP MNIST Classifier architecture

## Environment Setup

Install **uv** (Python package manager):

Run `uv sync` to install dependencies (or use `pip install -r requirements.txt`).

## Task 1: Counting Islands

This task counts the number of islands in a 2D grid using an iterative DFS flood-fill algorithm.

### Run the solution:
Linux / macOS:
```bash
python task1_isl/solution.py < task1_isl/input.txt
```
Windows:
```bash
Get-Content task1_isl/input.txt | uv run task1_isl/solution.py
```

### Approach
The algorithm uses iterative DFS with an explicit stack.
Each time a land cell (`1`) is found, a flood-fill is performed to mark the whole island as visited.

### Complexity
- Time: O(m * n)
- Space: O(m * n) in the worst case due to the stack

### Input format
The program reads from standard input:
- first line: `m n`
- next `m` lines: `n` integers (`0` or `1`)

## Task 2: Tabular Data Regression
Goal: predict a continuous target value for a hidden test dataset.

### Approach

The workflow includes:

- `exploratory data analysis (analysis.ipynb)`
- `model training (train.py)`
- `inference (predict.py)`

A **Random Forest Regressor** was selected as a robust non-linear baseline for tabular data.

Model performance is evaluated using **RMSE** on a validation split.

### Files
- `task2_reg/analysis.ipynb`    - EDA
- `task2_reg/train.py`          - model training script
- `task2_reg/predict.py`        - inference script
- `task2_reg/predictions.csv`   - predictions for hidden test set

### Training
```bash
uv run python task2_reg/train.py
```

### Prediction
```bash
uv run python task2_reg/predict.py
```

## Task 3: OOP MNIST Classifier Architecture
Demostrating a clean object-oriented design for a digit classification system.

### Architecture Components
- `DigitClassificationInterface` — abstract model interface
- `CNNModel` — CNN-style classifier
- `RFModel` — Random Forest classifier
- `RandomModel` — baseline random predictor
- `DigitClassifier` — wrapper that selects the model

### File
- `task3_archtr/classifier.py`

#### This design demonstrates:
- abstraction
- polymorphism
- separation of concerns



## To run all tasks sequentially:
#### Task 1
```bash
Get-Content task1_isl/input.txt | uv run task1_isl/solution.py
```
#### Task 2
```bash
uv run python task2_reg/train.py
uv run python task2_reg/predict.py
```
#### Task 3
```bash
# Architecture implementation is located in:
task3_archtr/classifier.py
```


## Requirements

The project uses **uv** for dependency management.

However, to comply with the task requirements, a `requirements.txt` file was generated from the uv environment.

Dependencies can be installed either with:

```bash
uv sync
```

or:

```bash
pip install -r requirements.txt
``` 