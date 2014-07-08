import ckan.plugins as p
import logging
import ckan.logic as logic

NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
get_action = p.toolkit.get_action

_ = p.toolkit._
c = p.toolkit.c

class WidgetsController(p.toolkit.BaseController):
    controller = 'ckanext.widgets.controller.WidgetsController'

    #@p.toolkit.auth_allow_anonymous_access
    #def view_widget(self):
    #    return p.toolkit.render('widget.html')

    def view_widget(self, id):
        '''
        Embeded page for  widget visualization.
        context = {'model': model, 'session': model.Session,
            'user': c.user or c.author, 'auth_user_obj': c.userobj}
        '''
        context = {#'model': model, 'session': model.Session,
                   #'user': c.user or c.author, 'auth_user_obj': c.userobj
		}
        
        print "--------------------------\n%s\n------------------------------" % str(id)
        
        try:
            c.package = get_action('package_show')(context, {'id': id})
            data_dict = {'resource': c.resource, 'package': c.package}
        except NotFound:
            abort(404, _('Resource not found'))
        except NotAuthorized:
            abort(401, _('Unauthorized to read resource %s') % id)
        
        return p.toolkit.render('widget.html', data_dict)

