"""
Entrypoint for running skill via Yandex Cloud Functions.

If you will use this function only via Alica it will cost nothing and can be deployed manually via
interface or via Yandex Cloud CLI in CI/CD.

But it is hard to test in actively development stage, so instead locally you can use
alice_gotovo.server.
"""
from alice_gotovo import skill


def entry(event, context):
    return skill.dispatcher(event)
