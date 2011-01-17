from fabric.api import env, run, cd, sudo, local, get


env.hosts = ['wraithan.net', ]
deploy_dir = '/srv/wsgi/blog/'


def deploy():
    git_pull()


def git_pull():
    with cd(deploy_dir):
        run('git pull')

