import argparse
import importlib
import os
import sys

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run solutions for specific days.")
    parser.add_argument(
        "day",
        type=str,
        help="The day number to execute (e.g., '01', '02')."
    )
    parser.add_argument(
        "part",
        type=int,
        choices=[1, 2],
        help="The part number to execute (1 or 2)."
    )
    args = parser.parse_args()

    # Construct the module path (e.g., day-01.part1-soln for day 01)
    day_folder = f"day-{args.day.zfill(2)}"
    part = args.part
    module_name = f"{day_folder}.part{part}-soln"  # Dynamic module path

    # Check if the solution script exists
    soln_filename = f"part{part}-soln.py"
    soln_path = os.path.join(day_folder, soln_filename)
    if not os.path.exists(soln_path):
        print(f"Error: Solution for day {args.day}, part {part} not found at {soln_path}.")
        return

    # Add the project root to sys.path
    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(project_root)

    # Import and run the module
    try:
        # Dynamically import the module
        module = importlib.import_module(module_name)

        # Check if the module has a 'main' function and call it
        if hasattr(module, "main"):
            module.main()
        else:
            print(f"The module '{module_name}' does not have a 'main' function.")
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except Exception as e:
        print(f"An error occurred while executing the module: {e}")

if __name__ == "__main__":
    main()
