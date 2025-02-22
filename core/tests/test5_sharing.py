from signUpDriver import SignUp
from sharingDriver import Sharing
import unittest
import random
import os
 
class TestSharing(unittest.TestCase):
    email = "signupname" + str(random.getrandbits(12)) + str(random.getrandbits(12)) + str(random.getrandbits(12)) + "@gmail.com"
    password = "abcdefgh"
    projectname = "Project Name Test"
    projectdescription = "Project Description"
    rosterfile = os.getcwd().replace(os.path.join(os.path.sep, "tests"), "") + os.path.join(os.path.sep, "sample_file") + os.path.join(os.path.sep, "rosters") + os.path.join(os.path.sep, "sample_roster.xlsx")
    rubricfile = os.getcwd().replace(os.path.join(os.path.sep, "tests"), "") + os.path.join(os.path.sep, "sample_file") + os.path.join(os.path.sep, "rubrics") + os.path.join(os.path.sep, "teamwork") + os.path.join(os.path.sep, "teamwork_scale3.json")
    evaluationname = "Evaluation Name Test"
    evaluationdescription = "This is a test description for the Evaluation!"

    # New Test for signing up
    def test0_signup_new_user (self):
        signup = SignUp()
        signup.sign_up_user(self.email, self.password, self.password)
        del signup

    # Manage Projects Page
    # New Test for checking project name link works
    def test1_check_project_name_link_works(self):
        create_sharing = Sharing()
        url = create_sharing.create_sharing_return_current_url_after_clicking_project_name_link(self.email, self.password, self.projectname, self.projectdescription, self.rosterfile, self.rubricfile, self.evaluationname, self.evaluationdescription)
        del create_sharing
        self.assertTrue(url.find("load_project"))

    # New Test for checking if manage button works
    def test2_check_if_manage_button_works(self):
        create_sharing = Sharing()
        url = create_sharing.create_sharing_return_current_url_after_clicking_manage_projects_button(self.email, self.password)
        del create_sharing
        self.assertTrue(url.find("project_profile"))

    # New Test for checking if delete button works
    def test3_check_if_delete_button_works(self):
        create_sharing = Sharing()
        text = create_sharing.create_sharing_return_text_after_clicking_delete_project_button(self.email, self.password, self.projectname)
        del create_sharing
        self.assertTrue(text=="not found")

    # New Test for checking if downloading button works
    def test4_check_if_downloading_button_works(self):
        create_sharing = Sharing()
        url = create_sharing.create_sharing_return_current_url_after_clicking_downloading_button(self.email, self.password)
        del create_sharing
        self.assertTrue(url.find("download"))

    # Page After Clicking Manage Projects Page
    # New Test for checking if Manage Projects Link in the .breadcrumbs element works
    def test5_check_if_manage_project_link_in_breadcrumbs_works(self):
        create_sharing = Sharing()
        url = create_sharing.create_sharing_return_current_url_after_clicking_projects_link_in_the_breadcrumbs(self.email, self.password)
        del create_sharing
        self.assertTrue(url.find("project_profile_jumptool"))

    # New Test for checking if send email button works
    def test6_check_if_send_email_button_works(self):
        create_sharing = Sharing()
        text = create_sharing.create_sharing_return_text_after_clicking_send_email_button(self.email, self.password, self.projectname, self.evaluationname)
        del create_sharing
        self.assertTrue(text=="Sending...")

    # New Test for checking if send with scores switch works
    def test7_check_if_send_with_scores_switch_works(self):
        create_sharing = Sharing()
        checked = create_sharing.create_sharing_return_checked_after_clicking_send_with_scores_switch(self.email, self.password)
        del create_sharing
        self.assertTrue(checked)

    # New Test for checking if grade complete see details link works

    # New Test for checking if clicking meta group that is complete after clicking grade complete see details link works

    # New Test for checking if grade incomplete see details link works

    # New Test for checking if clicking meta group that is incomplete after clicking grade incomplete see details link works

    # New Test for checking if display all details link works

    # New Test for checking if after clicking display all details link, if delete button works

    # New Test for checking if create new permission button works.

    # New Test for checking if after clicking create new permission button, if entering valid email to share works

    # New Test for checking if after clicking create new permission button, if entering invalid email to share works

    # New Test for checking if clicking update group button after editing a student's email that is valid works

    # New Test for checking if clicking update group button after editing a student's email that is invalid works
    
if __name__ == "__main__":
    unittest.main()