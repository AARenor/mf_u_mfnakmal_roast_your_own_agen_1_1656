"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda."""

import os
import pathlib
import sys

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. "
    "The comment is still maintained."
)


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, len(text)
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
