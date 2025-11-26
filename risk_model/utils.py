import yaml
import sys

def load_config(path: str) -> dict:
    try:
        with open(path, 'r') as file:
            config = yaml.safe_load(path)
            return config
    
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None
    
    except yaml.YAMLError as exc:
        print(f"Error: Failed to parse YAML file '{path}'.")
        if hasattr(exc, 'problem_mark'):
            mark = exc.problem_mark
            print(f"Position: line {mark.line + 1}, column {mark.column + 1}")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None