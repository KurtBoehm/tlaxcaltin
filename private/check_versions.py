# This file is part of https://github.com/KurtBoehm/tlaxcaltin.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from argparse import ArgumentParser
from configparser import ConfigParser
from contextlib import closing
import getpass
from hashlib import sha256
from pathlib import Path

from colorama import Fore
from github import Auth, Github
from pydantic import BaseModel
from requests import get
from secretstorage import dbus_init, get_default_collection


class Args(BaseModel):
    user_name: str
    password: str | None = None
    skip_checksums: bool
    names: list[str]


parser = ArgumentParser(
    description="Check whether the wraps use the most up-to-date version on GitHub."
)
parser.add_argument("--user-name", "-u", default="KurtBoehm")
parser.add_argument("--password", "-p")
parser.add_argument("--skip-checksums", "-c", action="store_true")
parser.add_argument("names", nargs="*")
args = Args.model_validate(vars(parser.parse_args()))

password = args.password
if password is None:
    with closing(dbus_init()) as connection:
        collection = get_default_collection(connection)
        items = [
            item
            for item in collection.get_all_items()
            if item.get_label().startswith(f"GitHub {args.user_name}")
        ]
        if items:
            [item] = items
            password = item.get_secret().decode()
        else:
            password = getpass.getpass("Password: ")

gh = Github(auth=Auth.Login(args.user_name, password))
del password


tlaxcaltin = Path(__file__).parents[1]
names = set(args.names) if len(args.names) > 0 else None
for path in sorted(tlaxcaltin.iterdir()):
    if path.suffix != ".wrap":
        continue
    if names is not None and path.stem not in names:
        continue

    parser = ConfigParser()
    with open(path, "r") as f:
        parser.read_file(f)
    if "wrap-file" not in parser:
        continue

    url = parser["wrap-file"]["source_url"]
    wrap_hash = parser["wrap-file"]["source_hash"]

    def verify_hash():
        if not args.skip_checksums:
            hash = sha256(get(url).content).hexdigest()
            color = Fore.GREEN if wrap_hash == hash else Fore.RED
            print(f"{color}{wrap_hash} → {hash}{Fore.RESET}")

    prefix = "https://github.com/"
    if not url.startswith(prefix):
        print(url)
        verify_hash()
        continue
    if "/archive" not in url:
        print(url)
        continue
    user, repo = url[len(prefix) : url.index("/archive")].split("/")
    release = url[url.rfind("/") + 1 : -len(".tar.gz")]

    repo = gh.get_repo(f"{user}/{repo}")
    try:
        tarball = repo.get_latest_release().tarball_url
        tarver = tarball[tarball.rfind("/") + 1 :]

        color = Fore.GREEN if release == tarver else Fore.RED
        print(f"{color}{repo.html_url}{Fore.RESET}", release, tarver)
        verify_hash()
    except Exception as ex:
        print(f"{Fore.MAGENTA}{repo.html_url}{Fore.RESET}", release, ex)
        verify_hash()
