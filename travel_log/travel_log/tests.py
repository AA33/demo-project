from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from travel_log.models import Trip

'''
Test Cases for 'Trip View' view
'''
class TripViewTests(TestCase):
    def setUp(self):
        # Create 2 users
        self.userPassword = '123xyz'
        self.user1 = User.objects.create_user('user1', 'user1@example.com', self.userPassword)
        self.user2 = User.objects.create_user('user2', 'user2@example.com', self.userPassword)
        # Create a trip for first user
        Trip.objects.create(trip_name="User1 Trip", start_date=timezone.now(), end_date=timezone.now(),
                            trip_description='description', user=self.user1)
        self.trip_id = str(Trip.objects.get(user=self.user1).id)

    # Case 0: successful login
    def login_as_user(self, username, password):
        response = self.client.post('/travel_log/userlogin/', {'username': username, 'password': password})
        self.assertEquals(response.status_code, 302)

    # Case 1: Logged in users see logout button
    def test_logged_in_user_can_logout(self):
        self.login_as_user(self.user1.username, self.userPassword)
        response = self.client.get('/travel_log/' + self.trip_id + '/view/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/travel_log/userlogout/")

    # Case 2: User is logged in, and viewing his own trip -- Should be able to access 'Edit' functionality
    def test_logged_in_user_can_edit_their_trip(self):
        self.login_as_user(self.user1.username, self.userPassword)
        response = self.client.get('/travel_log/' + self.trip_id + '/view/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/travel_log/edit/")

    # Case 3: User is logged in, viewing some other user's trip -- Should not be able to access 'Edit" functionality
    def test_logged_in_user_cannot_edit_others_trip(self):
        self.login_as_user(self.user2.username, self.userPassword)
        response = self.client.get('/travel_log/' + self.trip_id + '/view/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "/travel_log/edit/")

    # Case 4: User is not logged in -- Should see Login link
    def test_not_logged_in_user_can_login(self):
        response = self.client.get('/travel_log/' + self.trip_id + '/view/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/travel_log/userlogin/")

    # Case 5: User is not logged in -- Should not see Logout link
    def test_not_logged_in_user_cannot_logout(self):
        response = self.client.get('/travel_log/' + self.trip_id + '/view/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "/travel_log/userlogout/")

    # Case 6: User is not logged in -- Should not see Edit link
    def test_not_logged_in_user_cannot_edit(self):
        response = self.client.get('/travel_log/' + self.trip_id + '/view/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "/travel_log/edit/")


