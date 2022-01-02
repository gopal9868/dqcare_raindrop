from raindrop.viewsets import testcasesviewset,dbconnectionviewset,applicationviewset,Appnameviewset,Connnameviewset,tcresultviewset,Resulttypeviewset,Tcrescompareviewset
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('testcases',testcasesviewset,basename='testcases')
router.register('dbconnection',dbconnectionviewset,basename='dbconnection')
router.register('application',applicationviewset,basename='application')
router.register('appname',Appnameviewset,basename='appname')
router.register('connname',Connnameviewset,basename='connname')
router.register('tcresultview',tcresultviewset,basename='tcresultview')
router.register('resulttype',Resulttypeviewset,basename='resulttype')
router.register('tcrescompareview',Tcrescompareviewset,basename='tcrescompareview')

