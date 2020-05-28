import django_heroku


# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "8)_fhs^$tf-y083*i#zre2e3$z(zztus+o=jyu3=@)#2@w2qy*"
NEVERCACHE_KEY = "_*h$b)yce43tguq0ua^4&3-spylxw1h4b1%^ax*vd!z69rr9#m"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        # DB name or path to database file if using sqlite3.
        #"NAME": "dev.db",
        # Not used with sqlite3. 不适用sqlite3
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# heroku 只支持postgrespool数据库 来自：https://www.jianshu.com/p/610c670eabed
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Allowed development hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1","simon-mblog.herokuapp.com"]

###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": [""],  # Will be used as ALLOWED_HOSTS in production
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "/static/"

django_heroku.settings(locals())