from pathlib import Path

from PyInstaller.__main__ import run

SRC: Path = Path('prog.py')
EXE: Path = SRC.with_suffix('.exe')


def clean():
    if EXE.is_file():
        EXE.unlink()


def build_exe():
    pyinstaller_params = [
        '--clean',
        '--noconfirm',
        f'--name={SRC.stem}',
        '--paths=.',
        f'--icon={SRC.stem}.ico',
        '--optimize',
        '1',
        str(SRC),
    ]
    run(pyinstaller_params)


def main() -> None:
    clean()
    build_exe()


if __name__ == '__main__':
    main()
