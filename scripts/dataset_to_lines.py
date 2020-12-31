import json
import argparse
import logging


def jsonl_to_lines(jsonl_file, output_file): 
    with open(jsonl_file, 'r') as json_file:
        json_list = list(json_file)

    f = open(output_file, "a")

    for json_str in json_list:
        result = json.loads(json_str)
        f.write(result['text'] + "\n")

    f.close() 

def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument(
        "--jsonl_file", default=None, type=str, required=True, help="Path to input JSONL file"
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=True,
        help="The output filepath with raw lines",
    )

    args = parser.parse_args()

    # Setup logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO 
    )
    logger.warning(
        "Processing: %s", args.jsonl_file
    )

    jsonl_to_lines(args.jsonl_file, args.output_file)

if __name__ == "__main__":
    main()
