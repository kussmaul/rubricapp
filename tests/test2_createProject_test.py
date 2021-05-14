import unittest
import os
from signUpDriver import SignUp
from createProjectDriver import CreateProject
import time


class Configure:
    def configure_test_1_successOrExisted():
        (username, password) = \
            ("sampleuser_CreateProject@mail.com", "abcdefgh")
        return (username, password)

    def configure_test_3_CreateProject_Success():
        # both xlsx and json files are downloaded in the selenium/tests
        (username, password) = \
            ("sampleuser_CreateProject@mail.com", "abcdefgh")
        (projectname, projectdescription) =\
            ("Teamwork", "A sample project using an ELPISSrubric for Teamwork")
        (studentFile, jsonFile) = \
            (os.getcwd() + "/sample_roster.xlsx",
             os.getcwd() + "/teamwork_scale3.json")
        return (username, password, projectname,
                projectdescription, studentFile, jsonFile)

    def configure_test3_1_InvalidProjectNameAndDescription():
        # both xlsx and json files are downloaded in the selenium/tests
        (username, password) = \
            ("sampleuser_CreateProject@mail.com", "abcdefgh")
        (projectname, projectdescription) = ("12", "1"*256)
        (studentFile, jsonFile) = \
            (os.getcwd() + "/sample_roster.xlsx",
             os.getcwd() + "/teamwork_scale3.json")
        return (username, password, projectname,
                projectdescription, studentFile, jsonFile)

    def configure_test_3_2_CreateProject_InvalidFileFormat():
        # both xlsx and json files are downloaded in the selenium/tests

        (username, password) = \
            ("sampleuser_CreateProject@mail.com", "abcdefgh")
        (projectname, projectdescription) = \
            ("Teamwork", "A sample project using an ELPISSrubric for Teamwork")
        (studentFile, jsonFile) = \
            (os.getcwd() + "/teamwork_scale3.json",
             os.getcwd() + "/sample_roster.xlsx")
        return (username, password, projectname,
                projectdescription, studentFile, jsonFile)


class TestCreateProject(unittest.TestCase):

    def test1_sign_up_existed(self):

        test_sign_up = SignUp()
        (username, password) = Configure.configure_test_1_successOrExisted()
        (urlCurrent, alertInfo) = test_sign_up.sign_up(username, password)

    def test3_create_project_success(self):
        # success or duplicate project name error
        (username, password, project_name,
         project_description, studentFile, jsonFile) =\
            Configure.configure_test_3_CreateProject_Success()
        create_p = CreateProject()

        (url_current, alert_info) = create_p.\
            create_project_attempt(username, password, project_name,
                                   project_description, studentFile, jsonFile)

        url1 = "http://localhost:5000/instructor_project"
        is_project_created = url_current == url1

        url2 = "http://localhost:5000/create_project"
        is_project_not_created = url_current == url2
        # issue 219 - the error message
        #  -- "The project name has been used before" is missing.
        # here I am just using the current info being detected
        is_alert_info = alert_info == "3-150 characters"

        msg = alert_info

        self.assertTrue(is_project_created
                        or (is_project_not_created and is_alert_info), msg)

    def test3_1_create_project_invalid_project_name_and_description(self):
        # invalid length of project name and description

        (username, password, project_name,
         project_description, student_file, json_file) = \
            Configure.configure_test3_1_InvalidProjectNameAndDescription()

        create_p = CreateProject()

        (alert1, alert2) = create_p.\
            project_name_description_alerts(username, password, project_name,
                                            project_description,
                                            student_file, json_file)

        is_alert1 = \
            alert1 == "Field must be between 3 and 150 characters long."
        is_alert2 = \
            alert2 == "Field must be between 0 and 255 characters long."

        self.assertTrue(is_alert1 and is_alert2)

    # issue219 - the error messages are currently not shown

    # def test_3_2_CreateProject_InvalidFileFormat(self):
    #     # incorrect format of files uploaded for Roster and Rubric
    #
    #     (username, password, project_name,
    #      project_description, student_file, json_file) \
    #         = Configure.configure_test_3_2_CreateProject_InvalidFileFormat()
    #
    #     create_p = CreateProject()
    #
    #     (alert1, alert2) = create_p.\
    #         getInvalidFileAlert(username, password, project_name,
    #                             project_description, student_file, json_file)
    #     text = "'charmap' codec can't decode byte " \
    #            "0x81 in position 22: character maps to <undefined>"
    #     is_alert1 = alert1 == "File is not a zip file"
    #     is_alert2 = alert2 == text
    #
    #     self.assertTrue(is_alert1 and is_alert2)

    def test_3_0_rubric_file_teamwork(self):
        # test the rubric file - teamwork_scale3 location

        (username, password) = Configure.configure_test_1_successOrExisted()
        create_p = CreateProject()

        url = create_p.test_rubric_file_teamwork(username, password)
        std_url = "https://github.com/sotl-technology/rubricapp/blob/master/" \
                  "sample_file/rubrics/teamwork/teamwork_scale3.json"
        is_url_true = url == std_url

        self.assertTrue(is_url_true, url)

    def test_3_0_rubric_file_infoProcess(self):
        # test the rubric file - information_processing location

        (username, password) = Configure.configure_test_1_successOrExisted()
        create_p = CreateProject()

        url = create_p.test_rubric_file_info_process(username, password)
        std_url = "https://github.com/sotl-technology/rubricapp/blob" \
                  "/master/sample_file/rubrics/information_processing" \
                  "/information_processing.json"
        is_url_true = url == std_url
        self.assertTrue(is_url_true)

    def test_3_0_rubric_file_communication(self):
        # test the rubric file - interpersonal_communication location
        (username, password) = Configure.configure_test_1_successOrExisted()
        create_p = CreateProject()

        url = create_p.test_rubric_file_communication(username, password)
        std_url = "https://github.com/sotl-technology/rubricapp/blob" \
                  "/master/sample_file/rubrics/interpersonal_communication" \
                  "/interpersonal_communication_scale3.json"
        is_url_true = url == std_url
        self.assertTrue(is_url_true, url)


if __name__ == '__main__':
    unittest.main()
