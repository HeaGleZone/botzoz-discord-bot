import os


def debug_env(isProduction):
    if (isProduction):
        print('Production Environment')
    else:
        print('Development Environment')


def get_token(enableLog):
    'Gets token based on the current environment'

    # Setting up Production or Dev Env
    isProd = os.environ.get('IS_PRODUCTION', None)
    TOKEN = os.environ.get('TOKEN', None)

    # Get Token
    if not(isProd):
        # Libs
        from os.path import join, dirname
        from dotenv import load_dotenv

        # Local Env
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        TOKEN = os.getenv('TOKEN')

    # Log
    debug_env(isProd)

    return TOKEN
