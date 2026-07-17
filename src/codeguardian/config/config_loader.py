from pathlib import Path
import yaml


DEFAULT_CONFIG = {
    "rules": {
        "unused_import": {
            "enabled": True,
        },
        "dead_code": {
            "enabled": True,
        },
        "long_function": {
            "enabled": True,
            "max_lines": 50,
        },
        "too_many_arguments": {
            "enabled": True,
            "max_arguments": 5,
        },
        "circular_dependency": {
            "enabled": True,
        },
    }
}


def load_config(path: Path = Path("codeguardian.yml")):
    if not path.exists():
        return DEFAULT_CONFIG

    with open(path, "r", encoding="utf-8") as file:
        user_config = yaml.safe_load(file) or {}

    config = DEFAULT_CONFIG.copy()

    if "rules" in user_config:
        for rule, settings in user_config["rules"].items():
            if rule in config["rules"]:
                config["rules"][rule].update(settings)

    return config