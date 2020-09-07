"Handls Bot API Tokens"

import os


def debug_env(is_production):
    "Logs Current Environment"

    if is_production:
        print('Production Environment')
    else:
        print('Development Environment')


def get_token(enable_log):
    'Gets token based on the current environment'

    # Setting up Production or Dev Env
    is_prod = os.environ.get('IS_PRODUCTION', None)
    token = os.environ.get('TOKEN', None)

    # Get Token
    if not is_prod:
        # Libs
        from os.path import join, dirname  # pylint: disable=import-outside-toplevel
        from dotenv import load_dotenv  # pylint: disable=import-outside-toplevel

        # Local Env
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        token = os.getenv('TOKEN')

    # Log
    if enable_log:
        debug_env(is_prod)

    return token
