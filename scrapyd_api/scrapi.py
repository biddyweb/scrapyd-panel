__author__ = 'Marvin Laske'

import requests
import urlparse
from json import loads


class ScrapydApi:
    def __init__(self, scrapyd_url):
        """
        Initializes the api for a specific url

        :type scrapyd_url: str
        :param scrapyd_url: base url (including port if != 80) of the scrapyd installation
        """
        self.scrapyd_url = scrapyd_url

    def add_version(self, project_name, version, python_egg_path):
        """
        Uploads a new version of a python egg to the scrapyd installation

        :rtype: int
        :return: returns the count of spiders that were count in the egg
        :type python_egg_path: str
        :type version: str
        :type project_name: str
        :param project_name: name of the project to which the egg shall be uploaded
        :param version: version string of the egg
        :param python_egg_path: file path to the egg that shall be uploaded
        """
        url = urlparse.urljoin(self.scrapyd_url, "/addversion.json")
        response = requests.post(url, data={
            "project": project_name,
            "version": version
        }, files={
            "egg": open(python_egg_path, "rb")
        })

        if not response.ok:
            raise IOError("response was not ok")

        json = loads(response.text)

        if not "status" in json:
            raise IOError("status was not found")

        if json["status"] != "ok":
            raise IOError("status was not ok")

        if not "spiders" in json:
            raise IOError("spiders were not found")

        return json["spiders"]

    def del_version(self, project_name, version):
        """
        Deletes a version of a project

        :type version: str
        :type project_name: str
        :param project_name: name of the project
        :param version: projectversion
        """
        url = urlparse.urljoin(self.scrapyd_url, "/delversion.json")
        response = requests.post(url, data={
            "project": project_name,
            "version": version
        })

        if not response.ok:
            raise IOError("response was not ok")

        json = loads(response.text)

        if not "status" in json:
            raise IOError("status was not found")

        if json["status"] != "ok":
            raise IOError("status was not ok")

    def schedule(self, project_name, spider_name, settings=None, **kwargs):
        """
        Schedules a scrapy spider with the specific options and eventually arguments

        :type settings: str
        :type spider_name: str
        :type project_name: str
        :param project_name: name of the project, the spider is within
        :param spider_name: name of the spider, you want to schedule
        :param settings: optional - a scrapy setting to use when running the spider
        :param kwargs: these parameters will be passed as spider arguments
        """
        pass

    def cancel(self, project_name, job_id):
        """
        Cancel a spider run (aka. job). If the job is pending, it will be removed.
        If the job is running, it will be terminated.

        :type job_id: str
        :type project_name: str
        :param project_name: name of the project
        :param job_id: id of the job, that's what you get returned in schedule(...)
        """
        pass

    def list_projects(self):
        """
        Get the list of projects uploaded to this Scrapy server.

        :rtype : list
        """
        url = urlparse.urljoin(self.scrapyd_url, "/listprojects.json")
        response = requests.get(url)
        if not response.ok:
            raise IOError("response was not ok")

        json = loads(response.text)

        if not "status" in json:
            raise IOError("status was not found")

        if json["status"] != "ok":
            raise IOError("status was not ok")

        if not "projects" in json:
            raise IOError("projects was not found")

        return json["projects"]

    def list_versions(self, project_name):
        """
        Lists all the existing versions for a project

        :type project_name: str
        :rtype : list
        :param project_name: name of the project
        """
        url = urlparse.urljoin(self.scrapyd_url, "/listversions.json")
        response = requests.get(url, params={
            "project": project_name
        })

        if not response.ok:
            raise IOError("response was not ok")

        json = loads(response.text)

        if not "status" in json:
            raise IOError("status was not found")

        if json["status"] != "ok":
            raise IOError("status was not ok")

        if not "versions" in json:
            raise IOError("versions were not found")

        return json["versions"]

    def list_jobs(self, project_name):
        """
        Lists all the jobs for a project
        All job data is kept in memory and will be reset when the Scrapyd service is restarted.
        So there will only be the jobs since your last scrapyd-(re)start.

        :type project_name: str
        :param project_name: the name of the project
        """
        pass

    def del_project(self, project_name):
        """
        Delete a project and all its uploaded versions.

        :type project_name: str
        :param project_name: name of the project
        """
        pass

    def list_spiders(project_name):
        """
        Lists all available spiders within a project

        :type project_name: str
        :param project_name: name of the project
        """
        pass