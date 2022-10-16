from multiprocessing import shared_memory
from createProjectDriver import CreateProject
from signUpDriver import SignUp
from test6Driver import Account
import unittest
import random
import string
import os

# /-----------------------------------------------------------------------------
# With this test, we are looking to test the functionality of the account.html
# page, including access to the page, possible error messages that a user may
# incur, and relevant functionality of the page
# /-----------------------------------------------------------------------------


class Test(unittest.TestCase):
    # also username for any created rubrics
    email = "test" + random.choice(string.ascii_letters) + \
        str(random.getrandbits(12)) + "@gmail.com"
    password = "password123"
    test_bad_input = " "
    # empty input to test search box error handling
    test_2_error = "Can't find this user"
    test_3_error = "Can't find this rubric"
    shared_with_text = "This user hasn't attend other rubrics"
    proj_name = "Project Name Test"
    proj_descript = "Project Description"
    rost_file = os.getcwd() + "/sample_roster.xlsx"
    r_file = os.getcwd() + "/teamwork_scale3.json"

    # ensure we have a user signed up for the following tests

    def test0_sign_up_new_user(self):
        test_sign_up = SignUp()
        (username, password) = (self.email, self.password)
        test_sign_up.sign_up_user(username, password, password)
        del test_sign_up

    # log in and test if we reach correct page
    def test_1_access_page(self):
        access_page = Account()
        access_page.login_user(self.email, self.password)
        access_page.test_page_access
        text = "http://127.0.0.1:5000/account/success"
        is_text = access_page.test_page_access() == text
        del access_page
        self.assertTrue(is_text, is_text)

    # ensure error message pops up if entered user isn't found
    def test_2_first_search_box(self):
        sbox_1_test = Account()
        sbox_1_test.login_user(self.email, self.password)
        is_alert = sbox_1_test.test_2_first_search_error(
            self.test_bad_input) == self.test_2_error
        del sbox_1_test
        self.assertTrue(is_alert, "Failed")

    def test_3_second_search_box(self):
        sbox_2_test = Account()
        sbox_2_test.login_user(self.email, self.password)
        is_alert = sbox_2_test.test_3_second_search_error(
            self.test_bad_input) == self.test_3_error
        del sbox_2_test
        self.assertTrue(is_alert, "sure")

    # the sharing functionality works but doesn't populate the shared
    # project on the "Shared with me" section of this page thus it
    # will only be tested for its base state text
    def test_4_shared_section_text(self):
        shared_section = Account()
        shared_section.login_user(self.email, self.password)
        is_text = shared_section.test_4_shared_text(self.shared_with_text)
        self.assertTrue(is_text, "No Text")

    # create rubric and ensure it shows in "My Projects" after searching in first search field
    def test_7_project_exists_in_my_projects(self):
        create_rubric = CreateProject()
        create_rubric.create_project(
            self.email, self.password, self.proj_name, self.proj_descript, self.rost_file, self.r_file)
        del create_rubric
        my_proj = Account()
        my_proj.login_user(self.email, self.password)
        (is_element, elem_text) = my_proj.test_7_my_projects(self.email)
        is_element_there = is_element
        is_element_title_correct = elem_text == self.proj_name
        self.assertTrue(is_element_there, "Element Not Found")
        self.assertTrue(is_element_title_correct, "Project Name Incorrect")
        del my_proj


if __name__ == "__main__":
    unittest.main()
