# Student Score Manager



![Python](https://img.shields.io/badge/Python-3.x-blue)![License](https://img.shields.io/badge/license-MIT-green)![Status](https://img.shields.io/badge/status-active-brightgreen)



A modular CLI tool for processing, grading, and ranking student scores with dynamic pass mark support.

## Problem it Solves
Manual grading and ranking is error-prone. This tool automates score input, grade assignment, and ranking for any class size.

## Features
- Accepts 5+ students (enforced)
- Dynamic pass mark per session
- Handles duplicate names
- Tied ranking support
- Pass/fail split output

## Tech Stack
- Python 3 (no external dependencies)
- Modular architecture: `main.py`, `grading_system.py`, `detail_input_system.py`

## Setup
```bash
git clone https://github.com/kaluokekelawrence-web/student_score_manager
cd student-score-manager
python main.py
```

## Project Structure
```text
student_score_manager/
├── main.py                  # Entry point and orchestrator
├── grading_system.py        # Cutoff logic and grade computation
└── detail_input_system.py   # Input collection and validation
```

## Known Issues / Roadmap
- [ ] Export results to CSV
- [ ] FP refactor (functions currently mix computation + display)

## Author

Lawrence Kalu-Okeke

GitHub Repository: https://github.com/kaluokekelawrence-web/student_score_manager