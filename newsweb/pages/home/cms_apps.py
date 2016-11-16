# -*- coding: utf-8 -*-
# @Author: huangnan
# @Date:   2016-10-20 20:22:27
# @Last Modified by:   huangnan
# @Last Modified time: 2016-10-20 20:33:09
# @E-mail: foxstarx@gmail.com


from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class HomeApp(CMSApp):
	name = _('Home')
	urls = ['pages.home.urls']
	app_name = 'home'

apphook_pool.register(HomeApp)
