import argparse
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


# @timer
# @profile
def _merge_logs(log_1: Path, log_2: Path, output_path: Path) -> None:
    line_1 = None
    line_2 = None
    with open(log_1, mode='rb') as log_file_1:
        with open(log_2, mode='rb') as log_file_2:
            with open(output_path, mode='wb') as output_log_file:
                while True:
                    line_1 = log_file_1.readline() if line_1 is None else line_1
                    line_2 = log_file_2.readline() if line_2 is None else line_2

                    if line_1 and line_2:
                        if json.loads(line_1).get('timestamp') <= json.loads(line_2).get('timestamp'):
                            output_log_file.write(line_1)
                            line_1 = None
                        else:
                            output_log_file.write(line_2)
                            line_2 = None
                    elif not line_1 and not line_2:
                        break
                    elif line_1 and not line_2:
                        output_log_file.write(line_1)
                        line_1 = None
                    elif not line_1 and line_2:
                        output_log_file.write(line_2)
                        line_2 = None





def main() -> None:
    args = _parse_args()
    log_1_path = Path(args.log1_file)
    log_2_path = Path(args.log2_file)
    output_path = Path(args.merged_log_file)

    t0 = time.time()

    merged_logs = _merge_logs(log_1_path, log_2_path, output_path)

    print(f"finished in {time.time() - t0:0f} sec")



if __name__ == '__main__':
    main()