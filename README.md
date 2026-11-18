# Predicting breakout players in the football transfer market

Advanced Data Analytics, HEC Lausanne, Autumn 2026. Individual project by Jonathan Pacozzi.

**Question.** Using only information available at the end of a season, can we predict which football
players will see their market value at least double during the following season?

## Repository structure

| Folder / file | Content |
|---|---|
| `notebooks/` | One notebook per stage, run in order (see below) |
| `src/` | Python modules shared by the notebooks (`config.py`, `features.py`, `evaluation.py`) |
| `data/raw/` | Raw CSV files (not stored in the repository, see "Getting the data") |
| `data/processed/` | Cleaned tables produced by the notebooks |
| `figures/`, `tables/` | Every figure and table of the paper, produced by the notebooks |
| `paper/` | The research paper (PDF) |
| `requirements.txt` | Python packages needed |

## Notebooks

| # | Notebook | Stage |
|---|---|---|
| 1 | `01_get_data.ipynb` | Obtain the raw data |
| 2 | `02_build_panel.ipynb` | Clean and build the player-season table |
| 3 | `03_target_eda.ipynb` | Define the target, explore the data |
| 4 | `04_baseline.ipynb` | Baseline rule and logistic regression |
| 5 | `05_models.ipynb` | Comparison of the classification methods |
| 6 | `06_results.ipynb` | Scout test, feature importance, final figures and tables |

Each notebook runs from top to bottom in a fresh kernel.

## Getting the data

Transfermarkt dataset (dcaribou/transfermarkt-datasets), published on Kaggle:
https://www.kaggle.com/datasets/davidcariboo/player-scores

Licence: **[TO CHECK on the dataset page before submission, then write it here]**

Instructions: **[TO COMPLETE: how `01_get_data.ipynb` downloads the files into `data/raw/`]**

Files used: `appearances.csv`, `player_valuations.csv`, `players.csv`, `competitions.csv`, `clubs.csv`.
Note: the dataset is frozen at mid-2026 (no updates after that).

## Running the code

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

- Approximate running time: **[TO COMPLETE]**
- Resources beyond the provided Nuvolos workspace: **[TO COMPLETE: none, or what was used]**

## Declaration of tools

Generative AI tools and code assistants used are declared in the appendix of the paper.
