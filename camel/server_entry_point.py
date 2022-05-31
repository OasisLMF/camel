from flask import Flask
from flask_cors import CORS

from camel.storage.components.profile import Profile
from camel.

# define the flask app configurations
app = Flask(__name__, template_folder="model_template")
# api = Api(app)
app.secret_key = "nothing"
cors = CORS(app)


@app.route("/")
def home():
    return "This is the camel server"


@app.route("/profiles")
def get_profiles():
    string_buffer = ""
    for profile in Profile.get_profiles():
        string_buffer += f" {profile}"
    return string_buffer


@app.route("/projects/remote")
def get_remote_projects():
    return "remote projects"


@app.route("projects/remote/get")
def get_remote_project():
    return "remote project"


@app.route("project/remote/start")
def project_remote_start():
    return "remote project start"


@app.route("project/remote/finish")
def project_remote_finish():
    return "remote project finish"


@app.route("ssh/get/all")
def ssh_get_all():
    return "ssh get all"


@app.route("ssh/get/stashed")
def ssh_get_stashed():
    return "ssh get stashed"


@app.route("ssh/stash/")
def ssh_stash():
    return "ssh stash"


@app.route("basecampe/stash/")
def basecamp_stash():
    return "basecamp stash"


# @app.teardown_request
# def teardown_request(*args, **kwargs):
#     "Expire and remove the session after each request"
#     dal.session.expire_all()
#     dal.session.remove()
#     dal.session.close()
#
#
# @app.teardown_appcontext
# def teardown_request_two(*args, **kwargs):
#     "Expire and remove the session after each request"
#     dal.session.expire_all()
#     dal.session.remove()
#     dal.session.close()
#
#
# api.add_resource(PatientApi, "/v0/patient")
#
# for view in get_all_views():
#     api_object, view_url = view
#     api.add_resource(api_object, view_url)


# if __name__ == "__main__":
#     app.run(use_reloader=True, port=5002, threaded=True)

def main():
    app.run(use_reloader=True, port=5002, threaded=True)
