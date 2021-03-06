import os

import testinfra.utils.ansible_runner
import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleOSFamily(host):
    return host.ansible("setup")["ansible_facts"]["ansible_os_family"]


@pytest.fixture()
def AnsibleVars(host, AnsibleOSFamily):
    if AnsibleOSFamily == "RedHat":
        vars_file = "RedHat.yml"
    elif AnsibleOSFamily == "Debian":
        vars_file = "Debian.yml"
    elif AnsibleOSFamily == "Archlinux":
        vars_file = "Archlinux.yml"
    else:
        vars_file = "default.yml"
    vars_file_path = os.path.join("../../vars/", vars_file)
    return host.ansible("include_vars", vars_file_path)["ansible_facts"]


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_pyenv_packages_are_installed(host, AnsibleVars):
    print(host.system_info)
    if host.system_info.distribution != "arch":
        for pyenv_pkg in AnsibleVars["pyenv_packages"]:
            pkg = host.package(pyenv_pkg)
            assert pkg.is_installed


def test_pyenv_is_installed(host, scenario):
    pyenv_root = scenario.get_pyenv_root()
    pyenv_user = scenario.get_user()
    pyenv_group = scenario.get_group()
    pyenv = host.file(pyenv_root)
    assert pyenv.exists
    assert pyenv.is_directory
    assert pyenv.user == pyenv_user
    assert pyenv.group == pyenv_group


@pytest.mark.parametrize("plugin", [
    "pyenv-virtualenv",
    "pyenv-update",
    "xxenv-latest"
])
def test_pyenv_plugins_are_installed(host, scenario, plugin):
    pyenv_root = scenario.get_pyenv_root()
    pyenv_user = scenario.get_user()
    pyenv_group = scenario.get_group()
    pyenv_plugin = host.file("%s/plugins/%s" % (pyenv_root, plugin))
    assert pyenv_plugin.exists
    assert pyenv_plugin.is_directory
    assert pyenv_plugin.user == pyenv_user
    assert pyenv_plugin.group == pyenv_group


def test_pyenv_rc_enabled(host, scenario):
    rc_settings_file = host.file(scenario.get_rc_file())
    assert rc_settings_file.exists
    assert rc_settings_file.is_file
    assert rc_settings_file.contains('.*/pyenvrc$')


def test_python_install(host, scenario):
    python_ver, installed = scenario.get_python_test_case()
    pyenv_root = scenario.get_pyenv_root()
    python_path = f"{pyenv_root}/versions/{python_ver}"
    python = host.file(python_path)
    assert python.exists == installed


def test_venv_creation(host, scenario):
    venv_name, created = scenario.get_venv_test_case()
    pyenv_root = scenario.get_pyenv_root()
    venv_path = f"{pyenv_root}/versions/{venv_name}"
    venv = host.file(venv_path)
    assert venv.exists == created
