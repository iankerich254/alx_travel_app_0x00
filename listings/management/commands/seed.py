import random
import uuid
from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, User
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample listings and bookings'

    def handle(self, *args, **kwargs):
        host = User.objects.filter(role='host').first()
        guest = User.objects.filter(role='guest').first()

        if not host or not guest:
            self.stdout.write(self.style.ERROR('Please create at least one host and one guest user.'))
            return

        for _ in range(5):
            listing = Listing.objects.create(
                host=host,
                name=f"Sample Home {uuid.uuid4().hex[:6]}",
                description="A cozy place to stay.",
                location="Nairobi",
                price_per_night=random.uniform(50.0, 150.0),
            )

            Booking.objects.create(
                property=listing,
                user=guest,
                start_date=timezone.now().date(),
                end_date=timezone.now().date() + timedelta(days=3),
                total_price=listing.price_per_night * 3,
                status='confirmed'
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))

