# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1590427541.7490222
_enable_loop = True
_template_filename = '/home/zohrarezgui/nikola/lib/python3.7/site-packages/nikola/data/themes/base/templates/tagindex.tmpl'
_template_uri = 'tagindex.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'index.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        def content_header():
            return render_content_header(context)
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('        <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('        <div class="metadata">\n            ')
        __M_writer(str(feeds_translations.feed_link(tag, kind)))
        __M_writer('\n            ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n        </div>\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(tag, kind, rss_override=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/zohrarezgui/nikola/lib/python3.7/site-packages/nikola/data/themes/base/templates/tagindex.tmpl", "uri": "tagindex.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "48": 2, "49": 3, "54": 24, "59": 29, "65": 5, "80": 5, "81": 7, "82": 7, "83": 8, "84": 9, "85": 9, "86": 9, "87": 11, "88": 12, "89": 12, "90": 12, "91": 14, "92": 15, "93": 15, "94": 15, "95": 15, "96": 15, "97": 17, "98": 19, "99": 20, "100": 20, "101": 21, "102": 21, "108": 26, "120": 26, "121": 27, "122": 27, "123": 28, "124": 28, "130": 124}}
__M_END_METADATA
"""
