import ckan.plugins as p
import logging

_ = p.toolkit._

class WidgetsController(p.toolkit.BaseController):
    controller = 'ckanext.extwidget.controller.WidgetsController'
    

    def _template_setup_package(self, id):
        if not id:
            return
        context = {'for_view': True}
        try:
            p.toolkit.c.group_dict = p.toolkit.get_action('package_show')(context, {'id': id})
        except p.toolkit.ObjectNotFound:
            p.toolkit.abort(404, _('Package not found'))

    #The function must be decorated to allow anonymous access
    @p.toolkit.auth_allow_anonymous_access
    def package_show(self, id, package):
        self._template_setup_package(id)
        #if package is '':
        #    return self._org_list_pages(id)
        #_page = p.toolkit.get_action('ckanext_pages_show')(
        #    data_dict={'org_id': p.toolkit.c.group_dict['id'],
        #               'page': page,}
        #)
        #if _page is None:
        #    return self._org_list_pages(id)
        #p.toolkit.c.page = _page
        return p.toolkit.render('widget.html')
