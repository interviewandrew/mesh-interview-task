# Python/cherrypy based RESTy server for getting user info
by andrew pedelty, for a mesh interview question.

## Intro 
This is the couple-hours version of the project.

Things not included which would go into a backlog for further work after building a POC/discovery version/MVP: 
- Logging & analytics
- Test coverage (might actually want to do this as a part of initial work but eh)
- CI/CD Pipleine with quality gates and test automation as required or desired
- Actual docs and doc process (swagger or similar for API, knowledge base like client Confluence for process, inline docstrings for devs)
- Determine practice for non-2XX response pages/codes (ie, do we want 404s to expose internals? probably not. Do we want to pretend all 404s are 403s a la AWS? etc.)


## Quickstart
1. Install python3 using your favorite package manager or just via https://python.org
2. Optionally create a virtualenv or container using your favorite method
3. `pip install -r requirements.txt`
4. `python3 src/server.py`
5. Server should be running on port 8080. 
