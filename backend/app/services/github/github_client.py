from urllib.parse import urlparse


class GitHubClient:
    def parse_repository_url(self,url: str,):
        parsed_url = urlparse(url)

        if parsed_url.netloc != "github.com":
            raise ValueError("URL must be a GitHub repository.")

        parts = parsed_url.path.strip("/").split("/")

        if len(parts) < 2:
            raise ValueError("Invalid GitHub repository URL.")

        owner = parts[0]
        repository = parts[1]

        return {
            "owner": owner,
            "repository": repository,
        }