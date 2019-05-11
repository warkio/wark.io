import jinja2

import wark.settings

loader = jinja2.FileSystemLoader(
    wark.settings.TEMPLATES_DIRECTORY,
    followlinks=True,
)

env = jinja2.Environment(
    loader=loader,
    autoescape=jinja2.select_autoescape([
        'html',
        'xml',
    ]),
    auto_reload=wark.settings.DEBUG,
    enable_async=True,
)

env.policies['urlize.rel'] = 'nofollow noopener'

GLOBALS = {
    #'title': wark.settings.TITLE,
}


def template_filter(name, environment=env):
    def wrapper(fn):
        environment.filters[name] = fn
        return fn

    return wrapper


async def render(template_name, **kwargs):
    template = env.get_template(template_name, globals=GLOBALS)
    return await template.render_async(kwargs)


@template_filter('page_title')
def page_title(value):
    if not value:
        return wark.settings.TITLE

    return value + ' | ' + wark.settings.TITLE
