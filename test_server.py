import unittest
from server import app
import json
from unittest.mock import patch

class TestServerEventsAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<html>', response.data)  # Check if HTML content is returned

    def test_events_api(self):
        response = self.app.get('/events', headers={'Accept': 'text/event-stream'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/event-stream')
        # Check if the response contains the expected keys in the JSON data
        data = next(response.response).decode('utf-8')
        self.assertIn('data:', data)
        parsed_data = json.loads(data.split('data: ')[1])
        self.assertIn('message', parsed_data)
        self.assertIn('timestamp', parsed_data)
        self.assertEqual(parsed_data['message'], 'Hello from Server using Flask!')

class TestUsersAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('server.get_db_connection')
    def test_get_users(self, mock_get_db_connection):
        mock_conn = mock_get_db_connection.return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [(1, 'Test User', 'testuser@example.com')]
        mock_cursor.description = [('id',), ('name',), ('email',)]

        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        users = json.loads(response.data)
        self.assertIsInstance(users, list)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['name'], 'Test User')

    @patch('server.get_db_connection')
    def test_create_user(self, mock_get_db_connection):
        mock_conn = mock_get_db_connection.return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = [1]

        new_user = {
            'name': 'Test User',
            'email': 'testuser@example.com'
        }
        response = self.app.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        created_user = json.loads(response.data)
        self.assertIn('id', created_user)
        self.assertEqual(created_user['name'], new_user['name'])
        self.assertEqual(created_user['email'], new_user['email'])

if __name__ == '__main__':
    unittest.main()