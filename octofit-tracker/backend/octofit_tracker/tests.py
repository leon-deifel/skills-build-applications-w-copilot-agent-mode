from django.test import TestCase
from .models import Team, Activity, Workout, Leaderboard
from django.contrib.auth import get_user_model

User = get_user_model()

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', type='Run', duration=30, team='Test Team')
        self.assertEqual(activity.type, 'Run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='testuser', team='Test Team', points=10)
        self.assertEqual(lb.points, 10)

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')
