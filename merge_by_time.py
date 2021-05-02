import argparse
import json
import time
from itertools import chain
from json import JSONDecodeError
from pathlib import Path
from typing import List

from memory_profiler import profile

from timer import timer


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Tool to merge two log files.')

    parser.add_argument(
        'log1_file',
        metavar='<path/to/log1>',
        type=str,
        help='path to 1st log file',

    )
    parser.add_argument(
        'log2_file',
        metavar='<path/to/log2>',
        type=str,
        help='path to 2nd log file',
    )
    parser.add_argument(
        'merged_log_file',
        metavar='<path/to/merged/log>',
        type=str,
        help='path to output file',
    )

    return parser.parse_args()

# @timer
# @profile
def _merge_logs(log_1: Path, log_2: Path) -> List[dict]:
    print(f"merging logs...")
    with open(log_1, mode='rb') as log_1_file, open(log_2, mode='rb') as log_2_file:
        return sorted(chain(log_1_file, log_2_file), key=lambda x: json.loads(x).get('timestamp'))


@timer
def _put_logs_to_file(file_path: Path, logs: List[dict]):
    print(f"saving logs to {file_path.name}...")

    with file_path.open('wb') as log_file:
        log_file.writelines(logs)


def main() -> None:
    args = _parse_args()
    log_1_path = Path(args.log1_file)
    log_2_path = Path(args.log2_file)
    output_path = Path(args.merged_log_file)

    t0 = time.time()

    merged_logs = _merge_logs(log_1_path, log_2_path)
    _put_logs_to_file(output_path, merged_logs)

    print(f"finished in {time.time() - t0:0f} sec")



if __name__ == '__main__':
    main()