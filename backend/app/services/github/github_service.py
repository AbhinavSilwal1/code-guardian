from backend.app.services.github.github_client import (
GitHubClient,
)
from backend.app.services.github.repository_manager import (
    RepositoryManager,
)
from backend.app.services.guardian_service import (
    analyze_project,
)


class GitHubService:
    def __init__(self):
        self.client = GitHubClient()
        self.repository_manager = RepositoryManager()


    def analyze_repository(self, url: str,):
        self.client.parse_repository_url(url)

        repository_path = (self.repository_manager.clone_repository(url))

        repository = self.client.parse_repository_url(url)

        try:
            return analyze_project(
                str(repository_path),
                source={
                    "type": "github",
                    "owner": repository["owner"],
                    "repository": repository["repository"],
                    "url": url,
                },
            )

        finally:
            self.repository_manager.cleanup(repository_path)