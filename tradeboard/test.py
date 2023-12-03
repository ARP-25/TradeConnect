from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from tradeboard.views import TradePostList
from .forms import TradePostForm
from .models import TradePost, Rating, Comment, ContactMessage


class TradePostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.post = TradePost.objects.create(
            title='Test Post',
            author=self.user,
            description='Test description'
        )
        self.rating = Rating.objects.create(
            post=self.post,
            user=self.user,
            rating=5
        )
        self.comment = Comment.objects.create(
            tradepost=self.post,
            name='Test User',
            email='test@example.com',
            body='This is a test comment'
        )
        self.contact_message = ContactMessage.objects.create(
            name='Test Contact',
            email='contact@example.com',
            phone_number='1234567890',
            body_message='Test message body'
        )

    def test_trade_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.description, 'Test description')

    def test_rating_creation(self):
        self.assertEqual(self.rating.post, self.post)
        self.assertEqual(self.rating.user, self.user)
        self.assertEqual(self.rating.rating, 5)

    def test_comment_creation(self):
        self.assertEqual(self.comment.tradepost, self.post)
        self.assertEqual(self.comment.name, 'Test User')
        self.assertEqual(self.comment.email, 'test@example.com')
        self.assertEqual(self.comment.body, 'This is a test comment')

    def test_contact_message_creation(self):
        self.assertEqual(self.contact_message.name, 'Test Contact')
        self.assertEqual(self.contact_message.email, 'contact@example.com')
        self.assertEqual(self.contact_message.phone_number, '1234567890')
        self.assertEqual(self.contact_message.body_message, 'Test message body')


class TradePostListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser')
        self.trade_post_1 = TradePost.objects.create(title='Post 1', status=1, author=self.user)
        self.trade_post_2 = TradePost.objects.create(title='Post 2', status=1, author=self.user)

    def test_get_queryset(self):
        url = reverse('home')  
        request = self.factory.get(url)
        request.user = self.user
        response = TradePostList.as_view()(request)

        queryset = TradePost.objects.filter(status=1).order_by('-created_at')
       
        self.assertQuerysetEqual(
            response.context_data['object_list'],
            queryset,
            transform=lambda x: x
        )


class TradePostRatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.trade_post = TradePost.objects.create(title='Test Post', slug='test-post', author=self.user, description='Test Description')
        self.client = Client()

    def test_post_rating(self):
        url = reverse('tradepost_rating', kwargs={'slug': self.trade_post.slug})
        self.client.force_login(self.user)
        response = self.client.post(url, {'rating': 5})

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Rating.objects.filter(post=self.trade_post, user=self.user, rating=5).exists())

        storage = list(get_messages(response.wsgi_request))
        messages = [m.message for m in storage]
        self.assertIn('Thank you for rating this trade post!', messages)

    def tearDown(self):
        self.user.delete()
        self.trade_post.delete()


class TradePostEditViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        self.trade_post = TradePost.objects.create(
            title='Test Post',
            author=self.user,
            description='This is a test description.'
        )

    def test_edit_trade_post(self):
        edit_url = reverse('tradepost_edit', args=[self.trade_post.slug])
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)

        form_data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
        }

        response = self.client.post(edit_url, form_data)
        self.assertEqual(response.status_code, 302) 
        self.trade_post.refresh_from_db()
        self.assertEqual(self.trade_post.title, 'Updated Title')
        self.assertEqual(self.trade_post.description, 'Updated Description')


class TradePostDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.trade_post = TradePost.objects.create(title='Test Trade Post', slug='test-trade-post', author=self.user)

    def test_trade_post_deletion(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('tradepost_delete', args=[self.trade_post.slug]))
        self.assertEqual(response.status_code, 302) 

        trade_post_exists = TradePost.objects.filter(slug='test-trade-post').exists()
        self.assertFalse(trade_post_exists, "Trade post was not deleted")

    def tearDown(self):
        self.user.delete() 


class TradePostCreateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)
        self.url = reverse('tradepost_create')

    def test_get_trade_post_create(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tradepost_create.html')
        self.assertContains(response, '<form')

    def test_post_trade_post_create_valid(self):
        data = {
            'title': 'Test Title',
            'description': 'Test Description',
        }
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, 200)

    def test_post_trade_post_create_invalid(self):
        data = {
            'title': '',
            'description': 'Test Description',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')

    def tearDown(self):
        self.user.delete()


class SubmitFormViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_submit_form(self):
        url = reverse('submit_form')  

        response = self.client.post(url, {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message for form submission.',
            'phone': '1234567890'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)

        self.assertContains(response, 'Thank you for submitting a Message.')