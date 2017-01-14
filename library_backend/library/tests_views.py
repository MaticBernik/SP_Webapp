from django.test import TestCase
from django.http import HttpRequest,HttpResponse
from .models import Author,Book,User,Group,Lease
from lxml import etree
from .views import newBook,users,leases

class viewsMethodsTest(TestCase):

    def test_newBook(self):
        user = User(first_name='Janez', last_name='Novak', password='geslo123', username='user')
        user.save()
        group=Group(name='Librarian')
        group.save()
        #group = Group.objects.get(name='Librarian')
        group.user_set.add(user)

        author = Author(firstName='John', lastName='Smith')
        author.save()
        title = 'Izmisljotina'
        author = author
        genre = 'fiction'

        request=HttpRequest()
        request.user=user
        request.path='/library/books/add'
        request.method='POST'
        request.POST['title']=title
        request.POST['author']=author
        request.POST['genre']=genre
        newBook(request)
        self.assertIs(Book.objects.filter(title=title,author=author,genre=genre).exists(),True)

    def test_users(self):
        user1 = User(first_name='Janez', last_name='Novak', password='geslo123', username='janez')
        user1.save()
        group = Group(name='User')
        group.save()
        group.user_set.add(user1)
        user2 = User(first_name='Primoz', last_name='Novak', password='geslo123', username='primoz')
        user2.save()

        request=HttpRequest
        request.method="GET"
        request.user=user1
        response = users(request)
        tree = etree.HTML(response.content)
        users_list = tree.xpath('//table/tr/td')
        self.assertIs(users_list[1].text=='Janez' and users_list[6].text=='Primoz',True)

    def test_leases(self):
        #Pokazati mora samo lease od User1, ki posilja zahtevek
        user1 = User(first_name='Janez', last_name='Novak', password='geslo123', username='janez')
        user1.save()
        group = Group(name='User')
        group.save()
        group.user_set.add(user1)
        user2 = User(first_name='Primoz', last_name='Novak', password='geslo123', username='primoz')
        user2.save()

        author = Author(firstName='John', lastName='Smith')
        author.save()
        book1 = Book(title='Izmisljotina', author=author, genre='fiction')
        book1.save()
        book2 = Book(title='Resnica', author=author, genre='thriller')
        book2.save()
        lease1 = Lease(user_id=user1, book_id=book1)
        lease1.save()
        lease2 = Lease(user_id=user2, book_id=book2)
        lease2.save()


        request=HttpRequest
        request.method="GET"
        request.user=user1
        response = leases(request)
        tree = etree.HTML(response.content)
        leases_list = tree.xpath('//table/tr/td')
        self.assertIs(leases_list[0].text == '1 John Smith: Izmisljotina', True)
