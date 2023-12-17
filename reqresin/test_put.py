import datetime
import jsonschema
import requests
import schemas
import utils


class TestPutUser:
    endpoint = '/api/users'

    def test_put_user_number_response_code_200(self):
        # given
        user_number = 2
        user = {
            "name": "morpheus",
            "job": "zion resident"
        }
        url = utils.base_url + self.endpoint + f"/{user_number}"
        expected_code = 200
        # when
        response = requests.put(url, json=user)
        # then
        assert response.status_code == expected_code

    def test_put_user_number_response_structure(self):
        # given
        user_number = 2
        user = {
            "name": "morpheus",
            "job": "zion resident"
        }
        url = utils.base_url + self.endpoint + f"/{user_number}"
        # when
        response = requests.put(url, json=user)
        # then
        jsonschema.validate(response.json(), schemas.update_user)

    def test_put_user_number_wrong_endpoint(self):
        # given
        expected_code = 404
        user = {
            "name": "morpheus",
            "job": "zion resident"
        }
        url = utils.base_url + '/wrong_endpoint'
        # when
        response = requests.put(url, json=user)
        # then
        assert response.status_code == expected_code

    def test_put_user_check_update_date(self):
        # given
        user_number = 2
        user = {
            "name": "morpheus",
            "job": "zion resident"
        }
        url = utils.base_url + self.endpoint + f"/{user_number}"
        expected_code = 200
        # when
        response = requests.put(url, json=user)
        # then
        assert (response.json().get('updatedAt').split('T')[0] ==
                str(datetime.datetime.now() - datetime.timedelta(hours=3)).split()[0])
