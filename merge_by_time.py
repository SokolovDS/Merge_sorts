import json
import time
from itertools import chain
from pathlib import Path

from arg_parser import parse_args


def _merge_logs(log_1: Path, log_2: Path, output_path: Path) -> None:
    print(f"merging logs...")
    with open(log_1, mode='rb') as log_1_file, \
            open(log_2, mode='rb') as log_2_file, \
            open(output_path, mode='wb') as output_log_file:
        output_log_file.writelines(sorted(chain(log_1_file, log_2_file), key=lambda x: json.loads(x).get('timestamp')))


def main() -> None:
    args = parse_args()
    log_1_path = Path(args.log1_file)
    log_2_path = Path(args.log2_file)
    output_path = Path(args.merged_log_file)

    t0 = time.time()

    _merge_logs(log_1_path, log_2_path, output_path)

    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == '__main__':
    main()
