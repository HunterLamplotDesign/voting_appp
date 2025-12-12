# Voting App

## Overview
This is a simple voting application built with **PyQt6**.  
Users can vote for either **John** or **Jane** by selecting a candidate and entering their ID.  
The app prevents duplicate votes by checking voter IDs, saves results in a CSV file, and reloads them when restarted.

---

## Features
- Graphical interface designed in **Qt Designer** (`vote_window.ui`).
- Vote for John or Jane using radio buttons.
- Enter a voter ID before casting a vote.
- Duplicate votes are blocked (shows "Already voted" in red).
- Results are displayed in a popup window.
- Votes are saved in `storage/votes.csv` and persist across runs.

---


---

## How to Run
1. Install dependencies:
   ```bash
   pip install PyQt6

python main.py
