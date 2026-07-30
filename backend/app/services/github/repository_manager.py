from pathlib import Path
import tempfile
from git import Repo


class RepositoryManager:
    def clone_repository(self, url: str,) -> Path:
        directory = Path(tempfile.mkdtemp(prefix="codeguardian-"))

        Repo.clone_from(url, directory,)

        return directory