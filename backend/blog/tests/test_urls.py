from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, about

class TestUrls(SimpleTestCase):
	def test_list_url_is_resolved1(self):
		url = reverse('blog-home')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PostListView)

	def test_list_url_is_resolved2(self):
		url = reverse('post-detail',  args = [5])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PostDetailView)

	def test_list_url_is_resolved3(self):
		url = reverse('post-create')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PostCreateView)

	def test_list_url_is_resolved4(self):
		url = reverse('post-update',  args = [5])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PostUpdateView)

	def test_list_url_is_resolved5(self):
		url = reverse('post-delete',  args = [5])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PostDeleteView)

	def test_list_url_is_resolved6(self):
		url = reverse('blog-about')
		print(resolve(url))
		self.assertEquals(resolve(url).func, about)