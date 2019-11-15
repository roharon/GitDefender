import requests
import json
import os
from .crawl_tool_base import CrawlTool


class GetRepository(CrawlTool):
    def __init__(self):
        CrawlTool.__init__(self)
        self.__repositories = None
        self.__repositories_index = None
        self.api_route = '/user/repos'

    def test(self):
        print("---test start----")
        print("api root : " + self.github_api_root)
        print("api route : " + self.api_route)
        print("result : " + str(self.get_repo()))
        print("----test End ----")

    def get_repo(self):
        headers = {'Content-Type': 'application/json; charset=utf-8',
                'Authorization': self.user_token,
                'Accept': 'application/vnd.github.machine-man-preview+json',
                'User-Agent': self.user_agent
            }

        params = {
            'client_id':self.client_id,
            'client_secret': self.client_secret
            }

        res = requests.get(self.github_api_root + self.api_route, \
            headers=headers, params=params)

        try:
            if res.status_code == 401:
                raise Exception("Unvalid User Token")
            repo_list = list(map(self._get_repo_name, res.json()))
            # get repository_list

            self.repositories = repo_list
            return dict(
                repository_list=repo_list
                )

        except Exception as e:
            return dict(
                repository=[],
                error_message=str(e)
                )

    def _get_repo_name(self, data):
        """
        param: {'name': ~ , 'clone_url': ~ , 'commits_url': ~}
        return: 
        """
        try:
            repository_info = dict(
                name=data['name'],
                clone_url=data['clone_url'],
                commits_url=str(data['commits_url']).replace('{/sha}', '')
            )
            return repository_info

        except Exception as e:
            return e

    @property
    def repositories(self):
        return self.__repositories

    @repositories.setter
    def repositories(self, repo_list):
        self.__repositories = repo_list

    @property
    def repositories_index(self):
        return self.__repositories_index

    @repositories_index.setter
    def repositories_index(self, repo_ind):
        self.__repositories_index = repo_ind

if __name__ =="__main__":
    my1 = GetRepository()
    my1.user_token = "token 8b5aa78b499e2ca0cadc7839a8cadd8860bf5cef"
    my1.user_agent = "GitDefender"
    my1.test()
    #print(my1.user_agent)
    # my.user_token("216e53175a0b2fbe3ba21665de1d8b783ba2a4f2")

    