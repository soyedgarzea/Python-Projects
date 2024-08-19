import unittest
from main import do_stuff, run_guess


class TestMain(unittest.TestCase):
    '''
    TestMain

    Args:
        unittest ():
    '''

    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''
        test_do_stuff
        '''
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_error(self):
        '''
        test_do_stuff
        '''
        test_param = 'something'
        result = do_stuff(test_param)  # type: ignore
        self.assertIsInstance(result, ValueError)

    def tearDown(self) -> None:
        print('cleaning')

    def test_input(self):
        answer = 5
        guess = 5
        result = run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_incorrect(self):
        answer = 10
        guess = 5
        result = run_guess(guess, answer)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
