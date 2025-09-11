"""
Process dog_breeds.json from the Dog CEO API to summarize:
- total number of breeds
- total number of sub-breeds
- a sample list of breed names.

JSON structure example:
{"message": {breed: [subbreeds...]}, "status": "success"}
"""


#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################


FETCHED_DATA_DIR: str = "brendon_data"
PROCESSED_DIR: str = "brendon_processed"

#####################################
# Define Functions
#####################################

def summarize_dog_breeds(file_path: pathlib.Path) -> dict:
    """Summarize dog breeds JSON: total breeds, total sub-breeds, sample listing."""
    try:
        with file_path.open('r', encoding='utf-8') as f:
            data = json.load(f)  # {"message": {breed: [subbreeds...]}, "status": "success"}
        breeds: dict = data.get("message", {})
        total_breeds = len(breeds)
        total_subbreeds = sum(len(subs) for subs in breeds.values())
        sample_breeds = sorted(breeds.keys())[:10]
        return {
            "total_breeds": total_breeds,
            "total_subbreeds": total_subbreeds,
            "sample_breeds": sample_breeds,
        }
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""

    # TODO: Replace with path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "astros.json")

    # TODO: Replace with path to your JSON processed file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_astronauts_by_craft.txt")
    
    # TODO: Call your new function to process YOUR JSON file
    # TODO: Create a new local variable to store the result of the function call
    craft_counts = count_astronauts_by_craft(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write("Astronauts by spacecraft:\n")
        for craft, count in craft_counts.items():
            file.write(f"{craft}: {count}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")