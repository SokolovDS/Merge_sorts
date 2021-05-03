import json
import time
from pathlib import Path

from arg_parser import parse_args


def _merge_logs(log_1: Path, log_2: Path, output_path: Path) -> None:
    with open(log_1, mode='rb') as log_file_1, \
            open(log_2, mode='rb') as log_file_2, \
            open(output_path, mode='wb') as output_log_file:
        line_1 = log_file_1.readline()
        line_2 = log_file_2.readline()
        while True:
            if line_1 and line_2:
                if json.loads(line_1).get('timestamp') <= json.loads(line_2).get('timestamp'):
                    output_log_file.write(line_1)
                    line_1 = log_file_1.readline()
                else:
                    output_log_file.write(line_2)
                    line_2 = log_file_2.readline()
            elif line_1 and not line_2:
                output_log_file.write(line_1)
                line_1 = log_file_1.readline()
            elif not line_1 and line_2:
                output_log_file.write(line_2)
                line_2 = log_file_2.readline()
            elif not line_1 and not line_2:
                break


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
