"""Pyramid initializedb script"""

import os
import sys
# import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from mynutiae.models.models import (
    DBSession,
#    User,
    Base,
    )


def usage(argv):
    """Print usage and quit"""
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    """Main logic of DB initialization"""
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    # TODO: Add initial users?
#    with transaction.manager:
#        model = MyModel(name='one', value=1)
#        DBSession.add(model)
