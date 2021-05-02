import argparse
import heapq
import json
import time
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


def decorated_file(f, key):
    for line in f:
        yield (key(line), line)

# @timer
# @profile
def _merge_logs(log_1: Path, log_2: Path, output_path: Path) -> None:
    filenames = [log_1, log_2]
    files = map(open, filenames)
    with open(output_path, mode='w') as outfile:
        for line in heapq.merge(*[decorated_file(f, lambda x: json.loads(x).get('timestamp')) for f in files]):
            outfile.write(line[1])

    for file in files:
        file.close()

def main() -> None:
    args = _parse_args()
    log_1_path = Path(args.log1_file)
    log_2_path = Path(args.log2_file)
    output_path = Path(args.merged_log_file)

    t0 = time.time()

    _merge_logs(log_1_path, log_2_path, output_path)

    print(f"finished in {time.time() - t0:0f} sec")



if __name__ == '__main__':
    main()