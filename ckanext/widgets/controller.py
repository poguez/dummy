import ckan.plugins as p
import logging

_ = p.toolkit._

class WidgetsController(p.toolkit.BaseController):
    controller = 'ckanext.widgets.controller.WidgetsController'

    #def _template_setup_package(self, id):
    #    if not id:
    #        return
    #    context = {'for_view': True}
    #    try:
    #        p.toolkit.c.group_dict = p.toolkit.get_action('package_show')(context, {'id': id})
    #    except p.toolkit.ObjectNotFound:
    #        p.toolkit.abort(404, _('Package not found'))

    #The function must be decorated to allow anonymous access
    #def view_widget(self, id, package):
    @p.toolkit.auth_allow_anonymous_access
    def view_widget(self):
        #self._template_setup_package(id)
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

#    def view_widget(self, id, resource_id):
#        '''
#        Embeded page for a resource data-preview.
#
#        Depending on the type, different previews are loaded.  This could be an
#        img tag where the image is loaded directly or an iframe that embeds a
#        webpage, recline or a pdf preview.
#        '''
#        context = {
#            'model': model,
#            'session': model.Session,
#            'user': c.user or c.author,
#            'auth_user_obj': c.userobj
#        }
#
#        try:
#            c.resource = get_action('resource_show')(context,
#                                                     {'id': resource_id})
#            c.package = get_action('package_show')(context, {'id': id})
#
#            data_dict = {'resource': c.resource, 'package': c.package}
#
#            preview_plugin = datapreview.get_preview_plugin(data_dict)
#
#            if preview_plugin is None:
#                abort(409, _('No preview has been defined.'))
#
#            preview_plugin.setup_template_variables(context, data_dict)
#            c.resource_json = json.dumps(c.resource)
#        except NotFound:
#            abort(404, _('Resource not found'))
#        except NotAuthorized:
#            abort(401, _('Unauthorized to read resource %s') % id)
#        else:
#            return render(preview_plugin.preview_template(context, data_dict))
