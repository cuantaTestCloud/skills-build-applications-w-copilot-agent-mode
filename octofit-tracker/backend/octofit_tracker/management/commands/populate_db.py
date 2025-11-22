from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        Team.objects.create(name='Marvel', description='Marvel superheroes')
        Team.objects.create(name='DC', description='DC superheroes')

        # Crear usuarios
        User.objects.create(name='Tony Stark', email='tony@stark.com', team_name='Marvel', is_superhero=True)
        User.objects.create(name='Steve Rogers', email='steve@rogers.com', team_name='Marvel', is_superhero=True)
        User.objects.create(name='Bruce Wayne', email='bruce@wayne.com', team_name='DC', is_superhero=True)
        User.objects.create(name='Clark Kent', email='clark@kent.com', team_name='DC', is_superhero=True)

        # Crear actividades
        Activity.objects.create(user_email='tony@stark.com', type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user_email='steve@rogers.com', type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user_email='bruce@wayne.com', type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user_email='clark@kent.com', type='Flying', duration=120, date=timezone.now().date())

        # Crear workouts
        Workout.objects.create(name='Push Ups', description='Upper body', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Lower body', difficulty='Medium')

        # Crear leaderboard
        Leaderboard.objects.create(user_email='tony@stark.com', score=150)
        Leaderboard.objects.create(user_email='steve@rogers.com', score=120)
        Leaderboard.objects.create(user_email='bruce@wayne.com', score=180)
        Leaderboard.objects.create(user_email='clark@kent.com', score=200)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
