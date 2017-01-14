from django.test import TestCase
from .models import Lease,Reservation,Book,Author,User
from datetime import datetime, timezone, timedelta
from django.utils import timezone
import time

# Create your tests here.
class modelsMethodsTest(TestCase):

    def test_Reservation_is_expired(self):
        reservation = Reservation()
        reservation.start_date=timezone.now()
        reservation.expiration_date=timezone.now()
        #time.sleep(1)
        expired=reservation.is_expired()
        reservation.expiration_date+=timedelta(days=14)
        expired=expired and not reservation.is_expired()
        self.assertIs(expired,True)

    def test_Lease_is_expired(self):
        lease = Lease()
        lease.start_date=timezone.now()
        lease.expiration_date=timezone.now()
        #time.sleep(1)
        expired=lease.is_expired()
        lease.expiration_date+=timedelta(days=14)
        expired=expired and not lease.is_expired()
        self.assertIs(expired,True)

    def test_db(self):
        user = User(first_name='Janez',last_name='Novak',password='geslo123',username='user')
        user.save()
        author = Author(firstName='John', lastName='Smith')
        author.save()
        book = Book(title='Izmisljotina',author=author,genre='fiction')
        book.save()
        lease = Lease(user_id=user,book_id=book)
        lease.save()
        reservation = Reservation(user_id=user,book_id=book)
        reservation.save()
        self.assertIs(reservation.user_id.first_name=='Janez' and lease.book_id.genre=='fiction',True)



