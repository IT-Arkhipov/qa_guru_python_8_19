import requests
import utils


class TestGetListUsers:
    endpoint = '/api/users'

    def test_get_list_users_response_code_200(self):
        # given
        url = utils.base_url + self.endpoint
        expected_code = 200
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code

    def test_get_list_users_wrong_endpoint(self):
        # given
        url = utils.base_url + self.endpoint + '/all'
        expected_code = 404
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code


class TestGetUser:
    endpoint = '/api/users'

    def test_get_user_number_response_code_200(self):
        user_number = 2

        url = utils.base_url + self.endpoint + f"/{user_number}"

        response = requests.get(url)
        # then
        ...
