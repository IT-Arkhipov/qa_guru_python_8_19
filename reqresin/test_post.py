import jsonschema
import requests

import schemas
import utils


class TestPostCreateUser:
    endpoint = '/api/users'

    def test_post_create_user_response_code_200(self):
        # given
        url = utils.base_url + self.endpoint
        expected_code = 201
        new_user = {
            "name": "morpheus",
            "job": "leader"
        }
        # when
        response = requests.post(url, json=new_user)
        # then
        assert response.status_code == expected_code

    def test_post_create_user_empty_name(self):
        # given
        url = utils.base_url + self.endpoint
        expected_code = 201
        new_user = {}
        # when
        response = requests.post(url, json=new_user)
        # then
        assert response.status_code == expected_code

    def test_post_create_user_wrong_endpoint(self):
        # given
        url = utils.base_url + self.endpoint + '/wrong_endpoint'
        expected_code = 201
        new_user = {
            "name": "morpheus",
            "job": "leader"
        }
        # when
        response = requests.post(url, json=new_user)
        # then
        assert response.status_code == expected_code

    def test_post_create_user_response_structure(self):
        # given
        url = utils.base_url + self.endpoint
        new_user = {
            "name": "morpheus",
            "job": "leader"
        }
        # when
        response = requests.post(url, json=new_user)
        # then
        jsonschema.validate(response.json(), schemas.created_user)

    def test_post_create_user_check_created_user(self):
        # given
        url = utils.base_url + self.endpoint
        new_user = {
            "name": "morpheus",
            "job": "leader"
        }
        # when
        response = requests.post(url, json=new_user)
        # then
        assert response.json().get('name') == new_user.get('name')
        assert response.json().get('job') == new_user.get('job')


class TestPostRegister:
    endpoint = '/api/register'

    def test_post_register_response_code_200(self):
        # given
        url = utils.base_url + self.endpoint
        expected_code = 200
        credentials = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        # when
        response = requests.post(url, json=credentials)
        # then
        assert response.status_code == expected_code

    def test_post_register_missed_password(self):
        # given
        url = utils.base_url + self.endpoint
        expected_code = 400
        credentials = {
            "email": "eve.holt@reqres.in",
        }
        # when
        response = requests.post(url, json=credentials)
        # then
        assert response.status_code == expected_code
        assert response.json().get('error') == 'Missing password'

    def test_post_register_missed_email(self):
        # given
        url = utils.base_url + self.endpoint
        expected_code = 400
        credentials = {
            "password": "pistol"
        }
        # when
        response = requests.post(url, json=credentials)
        # then
        assert response.status_code == expected_code
        assert response.json().get('error') == 'Missing email or username'

    def test_post_register_response_structure(self):
        # given
        url = utils.base_url + self.endpoint
        credentials = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        # when
        response = requests.post(url, json=credentials)
        # then
        jsonschema.validate(response.json(), schemas.registered_user)
