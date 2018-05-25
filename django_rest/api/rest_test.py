#rest_test.py
import unittest
import requests

'''唯一需要注意的是，接口的访问需要签名,在发送get()请求时需要制定auth参数'''

class UserTest(unittest.TestCase):
    """用户查询测试"""
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/users"
    #admin
    def test_user1(self):
        '''test user 1'''
        r = requests.get(self.base_url + '/1/',auth = ('admin','admin12345'))
        result = r.json()
        self.assertEqual(result['username'],'admin')
        self.assertEqual(result['email'],'admin@mail.com')

    #tom
    def test_user2(self):

        '''test user 2'''
        r = requests.get(self.base_url + '/2/',auth = ('admin','admin12345'))
        result = r.json()
        self.assertEqual(result['username'],'tom')
        self.assertEqual(result['email'],'tom@mail.com')


    #jack
    def test_user3(self):
        '''test user 3'''
        r = requests.get(self.base_url + '/3/',auth = ('admin','admin12345'))
        result = r.json()
        self.assertEqual(result['username'],'jack')
        self.assertEqual(result['email'],'jack@mail.com')


class GroupsTest(unittest.TestCase):
    """docstring for GroupsTest"""
    def setUp(self):
        #base链接地址
        self.base_url = 'http://127.0.0.1:8000/groups'

    def test_groups1(self):
        '''test group 1'''
        r = requests.get(self.base_url + '/1/',auth = ('admin','admin12345'))
        result = r.json()
        self.assertEqual(result['name'],'test')

    def test_groups2(self):

        '''test group 2'''
        r = requests.get(self.base_url + '/2/',auth = ('admin','admin12345'))
        result = r.json()
        self.assertEqual(result['name'],'developer')


if __name__ == '__main__':
    unittest.main()




