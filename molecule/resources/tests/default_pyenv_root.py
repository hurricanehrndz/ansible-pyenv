def get_pyenv_root():
    return "/usr/local/pyenv"


def get_user():
    return "root"


def get_group():
    return "root"


def get_rc_file():
    return "/etc/profile.d/pyenv.sh"


def get_python_test_case():
    return "3.9.0", True


def get_venv_test_case():
    return "neovim", True
