import unittest
import transaction

from pyramid import testing

from mynutiae.models._user import DBSession

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from mynutiae.models._user import (
            Base,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
#        with transaction.manager:
#            model = MyModel(name='one', value=55)
#            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_it(self):
        from mynutiae.views.views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['one']['something'], 'whatever')
        self.assertEqual(info['project'], 'mynutiae')
