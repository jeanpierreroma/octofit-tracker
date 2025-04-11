from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe')
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith')

        # Create Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create Activities
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-04-10')
        Activity.objects.create(user=user2, type='Cycling', duration=45, date='2025-04-10')

        # Create Leaderboard
        Leaderboard.objects.create(team=team1, points=100)

        # Create Workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
