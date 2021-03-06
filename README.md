# hurricanehrndz.pyenv

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/hurricanehrndz/ansible-pyenv/CI?style=for-the-badge)](https://github.com/hurricanehrndz/ansible-pyenv/actions)
[![Ansible Role](https://img.shields.io/ansible/role/d/44292?style=for-the-badge)](https://galaxy.ansible.com/hurricanehrndz/pyenv)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](https://raw.githubusercontent.com/hurricanehrndz/ansible-pyenv/master/LICENSE)

An Ansible Role to install pyenv on Ubuntu, Fedora and RedHat systems. By
default, installs pyenv system-wide, but can be configured for deployment to a
specific user.

Additionally, role install several plugins to achieve a sane configuration.
Plugins include:

- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
- [pyenv-update](https://github.com/pyenv/pyenv-update)
- [xxenv-latest](https://github.com/momo-lab/xxenv-latest)

## Role Variables

| Variable Name            | Default Value | Value Type | Description                                                                |
| ------------------------ | ------------- | ---------- | -------------------------------------------------------------------------- |
| pyenv_user               | root          | String     | Default installs systems-wide or user specified                            |
| pyenv_update_git_install | no            | Boolean    | Performs git pull on install                                               |
| pyenv_root               | undefined     | String     | Install path, \$HOME/.pyenv or /usr/local/pyenv                            |
| pyenv_update_plugin      | yes           | Boolean    | Install pyenv-update plugin                                                |
| xxenv_update_plugin      | yes           | Boolean    | Install xxenv-latest plugin                                                |
| pyenv_virtualenv_plugin  | yes           | Boolean    | Install pyenv-virtualenv plugin                                            |
| pyenv_enable_rc          | yes           | Boolean    | Install runtime config                                                     |
| pyenv_rc_settings_file   | Blank         | String     | Default, auto-detects and modifies shell rc or installs system-wide script |
| pyenv_init_options       | --no-rehash   | String     | Init options for pyenv in rc file                                          |
| pyenv_python_versions    | undefined     | Array      | python version to install                                                  |
| pyenv_virtualenv         | undefined     | Dictionary | Virtual envs to create                                                     |

### Example

```yaml
---
pyenv_root: "/home/hurricanehrndz/.local/pyenv"
pyenv_user: "hurricanehrndz"
pyenv_update_git_install: no
pyenv_update_plugin: yes
xxenv_latest_plugin: yes
pyenv_virtualenv_plugin: yes
pyenv_install_rc: no
# auto detect
pyenv_rc_settings_file: ""

# For a system install, the shims dir will not be writable by users, disable rehashing
pyenv_init_options: "--no-rehash"

# additional options for the build process, e.g "--enable-shared"
pyenv_python_configure_opts: ""
```

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  tasks:
    - name: Add test user
      user:
        name: test
        shell: /bin/bash
    - name: Run pyenv role
      include_role:
        name: hurricanehrndz.pyenv
      vars:
        pyenv_user: test
```

[Other Example](./molecule/default/playbook.yml)

## License

[MIT](LICENSE)

## Author Information

[Carlos Hernandez aka HurricaneHrndz](https://github.com/hurricanehrndz)
