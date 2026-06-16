## Human-AI Mental Alignment Experiment
# Overview

This experiment investigates how well AI-generated responses align with human expectations in conversation. Using a Discourse Completion Task (DCT), participants are presented with short scenarios and asked to provide a continuation.
AI responses are then generated and rated on their alignment with the participant's own response.
EEG measures (N400) are recorded to explore neural correlates of congruency between human expectations and AI outputs.

# Experiment Flow
1. Participant Setup

- Participants provide consent and demographic information.
- Optional personality questionnaire.

2. Trial Procedure

- Display a scenario (prompt) to the participant.
- Participant types their response in a textbox and presses Enter.
- A 3-second pause occurs to separate participant response from EEG recording.
- AI generates three responses:
  - High Match (AIHigh) — closely matches expected human continuation.
  - Medium Match (AIMed) — plausible but less likely continuation.
  - Low Match (AILow) — unusual or unlikely continuation.
- One of the three AI responses is displayed.
- Participant rates how closely the AI matched their response on a visual analog scale (VAS).

3. End of Experiment

- Optional post-experiment interview or debriefing.
- Data is saved for analysis (scenario, participant response, AI responses, ratings).

# Software Requirements

PsychoPy & Python:

- PsychoPy (v2023.2 or newer recommended)
- Python 3.10+

Required Python packages:

- psychopy
- numpy
- pandas

Additional Python packages (for analysis/utilities):

- sentence-transformers (and its dependencies: torch)
- language-tool-python (requires Java for LanguageTool server)
- ollama (only if using the local Ollama server for LLM responses)

# Setup
1. Create and activate a virtual environment (recommended)
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```


2. Install required packages

`pip install psychopy numpy pandas sentence-transformers language-tool-python ollama`

Note:

- language-tool-python requires Java; ensure a Java runtime is installed.

- ollama requires a local Ollama server with the chosen model (e.g., llama3) running.

# Running the Experiment

Edit human-llm-alignment.psyexp in PsychoPy Builder to modify stimuli or trial flow.
The Builder exports the corresponding Python script human-llm-alignment.py.

Run the experiment locally: `python human-llm-alignment.py`


For quick testing or debugging, use test01.py.
However, human-llm-alignment.py is the current production script.

# Data Management

Experiment output files are written to the data/ folder.
Typical files per run:

<participant>_human-llm-alignment_<timestamp>.csv — main CSV data

*.log — PsychoPy logs

*.psydat — PsychoPy binary session data

# Archive Script (Recommended)

Instead of deleting test files, move them to an archive/ folder.
Example PowerShell commands:

- From repository root
`New-Item -ItemType Directory -Force -Path archive\data`

- Move test participant runs
```
Move-Item data\01_human-llm-alignment_* -Destination archive\data\ -Force
Move-Item data\pilot_human-llm-alignment_* -Destination archive\data\ -Force
```


- Move legacy experiment files
```
New-Item -ItemType Directory -Force -Path archive\legacy
Move-Item test01* -Destination archive\legacy\ -Force
```


# Cleaning Git History / Applying .gitignore

After updating .gitignore, remove already-tracked files with:

```
git rm -r --cached __pycache__
git rm --cached test01* dct_ai_psychopy.psyexp.py
git rm --cached data\01_* data\pilot_*
git add .gitignore
git commit -m "Update .gitignore and untrack test data and cache files"
```


# Notes & Troubleshooting

If language_tool_python raises errors, ensure Java is installed and available in PATH.

If you plan to generate LLM responses locally, verify that the Ollama server is running and accessible.
Calls to ollama.chat may fail if the model name differs or the server is offline.
