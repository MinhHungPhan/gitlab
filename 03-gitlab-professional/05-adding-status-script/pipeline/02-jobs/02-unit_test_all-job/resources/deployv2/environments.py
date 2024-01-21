from fabric.api import *
import os

# You may want to change this line by the technology name you are using or a project specific keyword
#from smile.techno.magento import *


env.distrib = 'debian'
env.project = 'accor-magento'
env.project_suffix = 'magento'

# SSH Keepalive connection
env.keepalive = 300

env.local_release_tarball_dir = os.path.expanduser('~') + '/fabric_releases'
env.local_merge_folder = '.fab_repo'
env.repository_url = 'git@git.smile.fr:accor/magento.git'
env.delivery_root_path = '/var/www/project'


# Akeneo git history
env.akeneo_repository_url = 'git@git.smile.fr:accor/akeneo.git'
env.akeneo_project = 'akeneo-accor'
env.bkp_repository_url = ''
env.bkp_projet = ''

# Can be folders or files
env.shared_resources = [
    'src/var',
    'src/media',
]
env.apache_writable_dirs = [
    'src/var',
    'src/media',
]

# Redis cache parameters, configure if you use redis
#env.redis_db_cache = "0"
#env.redis_db_session = "1"

# Uncomment if you need to hope onto several servers and use your ssh config
#env.use_ssh_config = True

# Enable this in order to use hard links for the copy of diff releases
env.diff_hardlink = False

# Set to True to remove prompt when deleting a release using the delete_release feature
env.delete_ok = False

# Set the number of release to keep, the older ones will be removed
env.release_retention = 4

# New Relic configuration
#env.newrelic_api_key = ''

env.forward_agent = True

env.ops_directory = "aws-platform"

#redmine configuration
env.redmine_url = 'https://redmine-projets.smile.fr/'
env.redmine_api_key = 'REDMINE_API_KEY'
env.redmine_curl_request = 'curl  -H "Content-Type: application/json" -H "X-Redmine-API-Key: {key}" "{url}{request}.json{filter}"'

def staging():
    env.environment = 'staging'
    env.bastion = {
        'host': 'smile@astoreshop-coreprod-bastion1.aws.smile.fr',
        'path': '~'
    }
    env.s3 = {
        'bucket': 'newaccorshop-releases',
        'path': 'magento/staging01',
        'profile': 'accor-prod'
    }
    env.s3_copy = {
        'magento/staging02',
    }
    env.merge = {
        'dest': 'release-2.9.0'
    }

def st02():
    env.environment = 'staging'
    env.bastion = {
        'host': 'smile@astoreshop-coreprod-bastion1.aws.smile.fr',
        'path': '~'
    }
    env.s3 = {
        'bucket': 'newaccorshop-releases',
        'path': 'magento/staging02',
        'profile': 'accor-prod'
    }
    env.s3_copy = {
    }
    env.merge = {
        'dest': 'develop-akeneo-connector'
    }

def master():
    env.environment = 'master'
    env.bastion = {
        'host': 'smile@astoreshop-coreprod-bastion1.aws.smile.fr',
        'path': '~'
    }
    env.s3 = {
        'bucket': 'newaccorshop-releases',
        'path': 'magento/training01',
        'profile': 'accor-prod'
    }
    env.s3_copy = {
        'magento/preprod',
        'magento/prod'
    }
    env.merge = {
        'dest': 'master'
    }

def inte():
    env.environment = 'inte'
    env.s3 = {
        'bucket': 'newaccorshop-releases',
        'path': 'magento/inte01',
        'profile': 'accor-prod'
    }
    env.merge = {
        'dest': 'develop'
    }
    env.s3_copy = {
    }

def master_hotfix(): #Name it as you wish, but understandable this will be your DEPLOY_NAME
    env.environment = 'master' #Must be master for package name
    env.bastion = {
        'host': 'smile@astoreshop-coreprod-bastion1.aws.smile.fr', #Don't change
        'path': '~' #Don't change
    }
    env.s3 = {
        'bucket': 'newaccorshop-releases', #Don't change
        'path': 'magento/training01', #Don't change, your package will be available for delivery on TRAINING if needed
        'profile': 'accor-prod' #Don't change
    }
    env.s3_copy = {
        'magento/preprod', #Don't change, your package will be available for delivery on PREPROD if needed
        'magento/prod' #Don't change
    }
    env.merge = {
        'dest': 'master-2.4.2' #This MUST be the name of your HOTFIXBRANCH
    }
