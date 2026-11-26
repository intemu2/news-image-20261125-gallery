"""Copy entry.png to the grader output directory.

Standard library only. Deterministic: a plain byte copy, so two runs
write identical bytes.
"""
import os
import shutil


def main():
    # entry.png sits next to this file in the repository root.
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
