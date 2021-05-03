import heapq
import json
import time
from pathlib import Path

from arg_parser import parse_args


def _decorated_file(f, key):
    for line in f:
        yield (key(line), line)


def _merge_logs(log_1: Path, log_2: Path, output_path: Path) -> None:
    filenames = [log_1, log_2]
    files = map(open, filenames)
    with open(output_path, mode='w') as outfile:
        for line in heapq.merge(*[_decorated_file(f, lambda x: json.loads(x).get('timestamp')) for f in files]):
            outfile.write(line[1])

    for file in files:
        file.close()


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
