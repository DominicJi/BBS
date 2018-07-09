# import json
# from datetime import datetime
#
# ret={'time':datetime.now()}
#
# class MyJsonEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o,datetime):
#             return o.strftime('%Y-%m-%d %H:%M:%S')
#         else:
#             return json.JSONEncoder.default(self,o)
# print(json.dumps(ret,cls=MyJsonEncoder))




# class MymetaClass(type):
#     def __init__(self,name,bases,attrs):
#         super().__init__(name,bases,attrs)
#         self.__instance=object.__new__(self)
#         self.__init__(self.__instance,setting.host,setting.port)
#     def __call__(self, *args, **kwargs):
#         if args or kwargs:
#             obj=object.__new__(self)
#             self.__init__(obj,*args,**kwargs)
#             return obj
#         return self.__instance
#
# def singleton(cls):
#     cls.__instance=cls(settings.host,settings.port)
#     def inner(*args,**kwargs):
#         if args or kwargs:
#             obj=cls(*args,**kwargs)
#             return obj
#         return cls.__instance
#     return inner
#
# class Mysql:
#     __instance=None
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#     @classmethod
#     def singleton(cls):
#         if not cls.__instance:
#             cls.__instance=cls('127.0.0.1',3306)
#         return cls.__instance
# print(Mysql.singleton().__dict__)
# print(Mysql('162.4.5.3',8080).__dict__)