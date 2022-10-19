import os

import fixtup
from django.test.utils import setup_test_environment, teardown_test_environment, setup_databases, teardown_databases
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

@pytest.fixture(autouse=True, scope="session")
def setupenvironment():
    # Fixtup automatically starts docker containers
    # during the execution of one or more tests.
    #
    with fixtup.up('mysql'):
        try:
            setup_test_environment()
            old_config=setup_databases(True, True, keepdb=False)
            try:
                yield
            finally:
                teardown_databases(old_config, True)
        finally:
            teardown_test_environment()


