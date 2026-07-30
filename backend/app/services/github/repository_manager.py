from pathlib import Path
import tempfile
from git import Repo
import shutil


class RepositoryManager:
    def clone_repository(self, url: str,) -> Path:
        directory = Path(tempfile.mkdtemp(prefix="codeguardian-"))

        Repo.clone_from(url, directory,)

        return directory


    def cleanup(self, path: Path,):
        shutil.rmtree(path, ignore_errors=True,)