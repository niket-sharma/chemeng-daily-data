#!/usr/bin/env python3
"""
Daily update script for chem-eng-daily-data repository.
Reads one entry from the queue and appends it to the appropriate data file.
"""

import json
import os
from datetime import datetime

QUEUE_FILE = "queue/pending_entries.json"
COMPOUNDS_FILE = "data/compounds.json"
CORRELATIONS_FILE = "data/experiment_correlations.py"
CONSTANTS_FILE = "data/experiment_constants.py"
LOG_FILE = "logs/update_log.md"


def load_queue():
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)


def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)


def add_compound(entry):
    # Load existing compounds
    if os.path.exists(COMPOUNDS_FILE):
        with open(COMPOUNDS_FILE, "r") as f:
            compounds = json.load(f)
    else:
        compounds = []

    # Add new compound
    compounds.append({
        "name": entry["name"],
        "formula": entry["formula"],
        "molecular_weight": entry["molecular_weight"],
        "boiling_point_c": entry["boiling_point_c"],
        "density_kg_m3": entry["density_kg_m3"],
        "cas_number": entry["cas_number"],
        "date_added": datetime.now().strftime("%Y-%m-%d")
    })

    with open(COMPOUNDS_FILE, "w") as f:
        json.dump(compounds, f, indent=2)

    return f"Added compound: {entry['name']}"


def add_correlation(entry):
    func_name = entry["name"].lower().replace(" ", "_").replace("-", "_").replace("'", "")
    new_code = f'''
# {entry["name"]}
# {entry["description"]}
# Source: {entry["source"]}
# Added: {datetime.now().strftime("%Y-%m-%d")}
def {func_name}({entry["variables"]}):
    """
    {entry["description"]}

    Equation: {entry["equation"]}
    """
    pass  # Implement based on equation above

'''
    with open(CORRELATIONS_FILE, "a") as f:
        f.write(new_code)

    return f"Added correlation: {entry['name']}"


def add_constant(entry):
    new_code = f'''
# {entry["name"]}
# Context: {entry["context"]}
# Added: {datetime.now().strftime("%Y-%m-%d")}
{entry["symbol"]} = {entry["value"]}  # {entry["units"]}

'''
    with open(CONSTANTS_FILE, "a") as f:
        f.write(new_code)

    return f"Added constant: {entry['name']}"


def log_update(message):
    log_entry = f"- **{datetime.now().strftime('%Y-%m-%d')}**: {message}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)


def main():
    queue = load_queue()

    if not queue:
        print("Queue is empty! Please regenerate entries.")
        return

    # Pop first entry from queue
    entry = queue.pop(0)

    # Process based on type
    if entry["type"] == "compound":
        result = add_compound(entry)
    elif entry["type"] == "correlation":
        result = add_correlation(entry)
    elif entry["type"] == "constant":
        result = add_constant(entry)
    else:
        result = f"Unknown entry type: {entry['type']}"

    # Save updated queue
    save_queue(queue)

    # Log the update
    log_update(result)

    print(result)
    print(f"Remaining entries in queue: {len(queue)}")


if __name__ == "__main__":
    main()
