from pathlib import Path
from codeguardian.config import load_config


def test_default_config(tmp_path):
    config = load_config(
        tmp_path / "missing.yml"
    )

    assert (
        config["rules"]["long_function"]["max_lines"]
        == 50
    )


def test_custom_config(tmp_path):
    config_file = tmp_path / "codeguardian.yml"

    config_file.write_text(
        """
rules:
  long_function:
    max_lines: 100
"""
    )

    config = load_config(config_file)

    assert (
        config["rules"]["long_function"]["max_lines"]
        == 100
    )


def test_disable_rule(tmp_path):
    config_file = tmp_path / "codeguardian.yml"

    config_file.write_text(
        """
rules:
  dead_code:
    enabled: false
"""
    )

    config = load_config(config_file)

    assert (
        config["rules"]["dead_code"]["enabled"]
        is False
    )