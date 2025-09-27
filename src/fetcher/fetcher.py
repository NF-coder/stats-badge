import requests

from .fetcherSettings import FetcherSettings
from .utils.bodyFabric import BodyFabric

from .langElem import LangElem

class FetchLangStats:
    def __init__(self, token: str) -> None:
        self._token = token

    def fetch_user(self, username: str) -> list[LangElem]:
        headers = {
            'Authorization': f'token {self._token}',
            'Content-Type': 'application/json'
        }

        body_fabric = BodyFabric(
            username=username,
            first_k_repos_fetch=FetcherSettings.FIRST_K_REPOS_FETCH,
            top_k_languages_in_repo=FetcherSettings.TOP_K_LANGUAGES_IN_REPO
        )

        response = requests.post(
            url=FetcherSettings.GITHUB_APT_URL,
            headers=headers,
            json=body_fabric.create()
        )
        
        if response.status_code == 200:
            response = response.json()

            result = []

            for repo in response["data"]["user"]["repositories"]["nodes"]:
                for languages in repo["languages"]["edges"]:
                    result.append(
                        LangElem(
                            languages["size"],
                            languages["node"]["color"],
                            languages["node"]["name"]
                        )
                    )
            return result
        
        raise RuntimeError("Github returnrd non-200 responce")