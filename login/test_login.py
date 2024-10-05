import unittest
from login.login import login 
from config import EMAIL, PASSWORD 

class TestLogin(unittest.TestCase):

    def test_login_success(self):
        response = login("fulano@qa.com", "teste") 
        print("Success Response:", response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("message"), "Login realizado com sucesso")

    def test_login_failure(self):
        response = login("invalid_emaila.com", "wrong_password")
        print("Failure Response:", response.json())
        self.assertEqual(response.status_code, 400)
        
        response_json = response.json()
        self.assertIsNotNone(response_json)  
        self.assertIn("email", response_json)
        self.assertEqual(response_json.get("email"), "email deve ser um email válido")

if __name__ == "__main__":
    unittest.main()