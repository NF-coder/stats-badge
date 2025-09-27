from dataclasses import dataclass

@dataclass
class FetcherSettings:
    GITHUB_APT_URL: str = "https://api.github.com/graphql"

    FIRST_K_REPOS_FETCH: int = 100
    TOP_K_LANGUAGES_IN_REPO: int = 10
    