# -*- coding: utf-8 -*-
# @Author: huangnan
# @Date:   2016-10-20 20:22:33
# @Last Modified by:   HUANG NAN
# @Last Modified time: 2016-11-13 14:18:58
# @E-mail: foxstarx@gmail.com


from django.conf.urls import patterns, url

from .views import Indexpage
from .views import Listpage
from .views import Testpage

urlpatterns = patterns('pages.home.views',

    # List View
    url(r'^$', 'Indexpage'),

    # Detail View
    url(r'^detail/(?P<uri>[\w\-\/]+)/$', 'Listpage'),
    # url(r'^(?P<slug>[^/]+)/$', StaffDetailView.as_view(), name='staffmember_detail'),

    # Test View
    url(r'^test$', 'Testpage')
)