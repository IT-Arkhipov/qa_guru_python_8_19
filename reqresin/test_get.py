import requests
import schemas
import jsonschema
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

    def test_get_list_users_response_structure(self):
        # given
        url = utils.base_url + self.endpoint
        # when
        response = requests.get(url)
        # then
        jsonschema.validate(response.json(), schemas.list_users)


class TestGetUser:
    endpoint = '/api/users'

    def test_get_user_number_response_code_200(self):
        # given
        user_number = 2
        url = utils.base_url + self.endpoint + f"/{user_number}"
        expected_code = 200
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code

    def test_get_user_wrong_user_number(self):
        # given
        url = utils.base_url + self.endpoint + '/100'
        expected_code = 404
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code

    def test_get_user_response_structure(self):
        # given
        user_number = 2
        url = utils.base_url + self.endpoint + f"/{user_number}"
        # when
        response = requests.get(url)
        # then
        jsonschema.validate(response.json(), schemas.user)

    def test_get_user_check_all_users(self):
        # given
        expected_code = 200
        url = utils.base_url + self.endpoint
        # when
        response = requests.get(url)
        users_quantity = response.json().get('total')
        # then
        for user_number in range(1, users_quantity):
            url = utils.base_url + self.endpoint + f"/{user_number}"
            response = requests.get(url)
            assert response.status_code == expected_code


class TestGetListResource:
    endpoint = '/api/unknown'

    def test_get_list_resource_response_code_200(self):
        # given
        url = utils.base_url + self.endpoint
        expected_code = 200
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code

    def test_get_list_resource_wrong_endpoint(self):
        # given
        url = utils.base_url + '/wrong_endpoint'
        expected_code = 404
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code

    def test_get_list_resource_response_structure(self):
        # given
        url = utils.base_url + self.endpoint
        # when
        response = requests.get(url)
        # then
        jsonschema.validate(response.json(), schemas.list_resource)


class TestGetSingleResource:
    endpoint = '/api/unknown'

    def test_get_resource_number_response_code_200(self):
        # given
        resource_number = 2
        url = utils.base_url + self.endpoint + f"/{resource_number}"
        expected_code = 200
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code

    def test_get_resource_wrong_resource_number(self):
        # given
        url = utils.base_url + self.endpoint + '/100'
        expected_code = 404
        # when
        response = requests.get(url)
        # then
        assert response.status_code == expected_code

    def test_get_resource_response_structure(self):
        # given
        resource_number = 2
        url = utils.base_url + self.endpoint + f"/{resource_number}"
        # when
        response = requests.get(url)
        # then
        jsonschema.validate(response.json(), schemas.resource)
