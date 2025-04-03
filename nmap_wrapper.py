#!/usr/bin/env python3
# Nmap Wrapper
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Requires nmap. Runs Nmap scans and logs output.

import subprocess
import argparse
import logging
import json

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='nmap_wrapper.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"default_options": "-sS"}

def run_nmap(target: str, options: str) -> str:
    """Run Nmap with specified options and return output."""
    try:
        cmd = ["nmap"] + options.split() + [target]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Nmap failed: {e.stderr}")
        return f"Error: {e.stderr}"
    except FileNotFoundError:
        logging.error("Nmap not installed")
        return "Error: Nmap is not installed"

def main():
    """Main function to parse args and run Nmap."""
    parser = argparse.ArgumentParser(description="Nmap Wrapper")
    parser.add_argument("--target", required=True, help="Target IP or hostname")
    parser.add_argument("--options", help="Nmap options (e.g., -sS -p 1-100)")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)
    options = args.options or config["default_options"]

    logging.info(f"Running Nmap on {args.target} with options: {options}")
    output = run_nmap(args.target, options)
    logging.info(f"Nmap output:\n{output}")
    print(output)

if __name__ == "__main__":
    main()
