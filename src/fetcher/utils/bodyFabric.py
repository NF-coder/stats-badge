class BodyFabric:
    def __init__(
            self,
            username: str,
            first_k_repos_fetch: int,
            top_k_languages_in_repo: int
        ) -> None:
        self._username = username
        self._first_k_repos_fetch = first_k_repos_fetch
        self._top_k_languages_in_repo = top_k_languages_in_repo

    def create(self) -> dict[str, str]:
        return {
            "query":
                """query {user(login: \"""" + self._username + """\") {
                        repositories(ownerAffiliations: OWNER, isFork: false, first: """ +  str(self._first_k_repos_fetch) +  """) {
                            nodes {
                                name languages(
                                    first: """ + str(self._top_k_languages_in_repo) +""",
                                    orderBy: {
                                        field: SIZE,
                                        direction: DESC
                                    }
                                ) {
                                    edges {
                                        size
                                        node {
                                            color
                                            name
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            """.replace("\n","")
        }