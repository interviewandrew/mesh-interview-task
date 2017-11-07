#!/usr/bin/env python3

'''
The main function, basically. Will run our server. 
'''

import cherrypy
import github_service as github



class GithubUserReporter(object):
    '''
    Basic af cherrypy-compatible api class
    '''
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def githubPayload(self, user_name='interviewandrew'):
        user_data = github.get_user_data(user_name)
        ret = {
            'githubHandle': user_name,
            'githubUrl': user_data['url'],
            'avatarUrl': user_data['avatar_url'],
            'email': user_data['email'],
            'follower_count': user_data['followers']
        }
        user_repos = github.get_repos_for_user(user_name)
        formatted_repos = [{
            'name': repo['name'],
            'url': repo['url'],
            'commitCount': len(github.get_commits(user_name, repo['name'])),
            'pullRequestCount': len(github.get_pull_requests(user_name, repo['name']))
        } for repo in user_repos]
        ret['repos'] = formatted_repos
        return ret


if __name__ == '__main__':
    cherrypy.quickstart(GithubUserReporter())
