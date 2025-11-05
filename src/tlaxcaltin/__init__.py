from argparse import ArgumentParser
from pathlib import Path
from typing import Literal

from argcomplete import autocomplete
from pydantic import BaseModel

from .update import update


class UpdateArgs(BaseModel):
    mode: Literal["update"]
    project_path: Path | None


Args = UpdateArgs


def run():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="mode")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("project_path", nargs="?")

    autocomplete(parser)
    args = Args.model_validate(vars(parser.parse_args()))

    match args:
        case UpdateArgs():
            update(args.project_path or Path.cwd())
