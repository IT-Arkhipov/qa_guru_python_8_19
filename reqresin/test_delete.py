import requests
import utils


class TestDeleteUsers:
    endpoint = '/api/users'

    def test_delete_users_response_code_200(self):
        # given
        user_number = 2
        url = utils.base_url + self.endpoint + f"/{user_number}"
        expected_code = 204
        # when
        response = requests.delete(url)
        # then
        assert response.status_code == expected_code

    def test_delete_user_wrong_user_number(self):
        # given
        url = utils.base_url + self.endpoint + '/100'
        expected_code = 404
        # when
        response = requests.delete(url)
        # then
        assert response.status_code == expected_code

    def test_delete_user_wrong_endpoint(self):
        # given
        url = utils.base_url + '/wrong_endpoint'
        expected_code = 404
        # when
        response = requests.delete(url)
        # then
        assert response.status_code == expected_code
