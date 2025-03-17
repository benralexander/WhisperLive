import unittest
from  whisper_live.states.cap import Cap
from  whisper_live.states.punc import Punc


class ProgState(unittest.TestCase):
    def test_base(self):
        self.assertEqual( 'we can init',  'we can init')  # add assertion here
    def test_cap(self):
        c= Cap()
        self.assertEqual(c.initiaize(),  'we can init')
    def test_cap_cmds(self):
        c= Cap()
        self.assertEqual(c.test_cmds(), 'all ok')
    def test_punc(self):
        p=Punc()
        self.assertEqual(p.initiaize(),  'we can init')
    def test_punc_cmds(self):
        p=Punc()
        self.assertEqual(p.test_cmds(), 'all ok')


if __name__ == '__main__':
    unittest.main()



