from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import homePage, topicsPage, room, createRoom, updateRoom, deleteRoom, deleteMessage

class testUrls(SimpleTestCase):
		"""
		This class is a test class of Urls inherited from SimpleTestCase.
		"""
		def testHomeUrlResolves(self):
				"""
				This function tests home url.
				"""
				url = reverse('home')
				self.assertEquals(resolve(url).func, homePage)

		def testTopicsPageUrlResolves(self):
				"""
				This function tests topic page url.
				"""
				url = reverse('topics')
				self.assertEquals(resolve(url).func, topicsPage)

		def testRoomUrlResolves(self):
				"""
				This function tests room url.
				"""
				url = reverse('room', args=['1'])
				self.assertEquals(resolve(url).func, room)

		def testCreateRoomUrlResolves(self):
				"""
				This function tests create-room url.
				"""
				url = reverse('create-room')
				self.assertEquals(resolve(url).func, createRoom)


		def testUpdateRoomUrlResolves(self):
				"""
				This function tests update room url.
				"""
				url = reverse('update-room', args=['1'])
				self.assertEquals(resolve(url).func, updateRoom)

		def testDeleteRoomUrlResolves(self):
				"""
				This function tests delete room url.
				"""
				url = reverse('delete-room', args=['1'])
				self.assertEquals(resolve(url).func, deleteRoom)

		def testDeleteMessageUrlResolves(self):
				"""
				This function tests delete message url.
				"""
				url = reverse('delete-message', args=['1'])
				self.assertEquals(resolve(url).func, deleteMessage)




