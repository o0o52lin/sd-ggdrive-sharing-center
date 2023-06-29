# installer script for some PyPI packages we need...

import launch

pkgs = [
    {"requests": "requests"}
]

for pkg in pkgs:
    key, val = next(iter(pkg.items()))
    if not launch.is_installed(key):
        launch.run_pip(f'install {val}', "requirements for SD Google Drive Sharing Center")
