import json
import os



def before_all(context):
    userdata = context.config.userdata
    context.configfile = userdata.get('configfile', 'blog_api_tests/resources/config/local.json')
    if os.path.exists(context.configfile):
        assert context.configfile.endswith(".json"), 'configfile is not json type'
        more_userdata = json.load(open(context.configfile))
        context.config.update_userdata(more_userdata)
    context.blog_url = context.config.userdata.get("blog_url")