# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:26:25 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:23:15 2018

@author: Administrator
"""

# =============================================================================
# def simple_decorator(f):
#     def wrapper():
#         print('Entering Function')
#         f()
#         print('Existed Function')
#     
#     return wrapper
# 
# @simple_decorator
# def hello():
#     print('Hello world')
#     
# hello()
# 
# def decorator_factory(enter_message,exit_message):
#     def simple_decorator(f):
#         def wrapper():
#             print(enter_message)
#             f()
#             print(exit_message)
#     
#         return wrapper
#     return simple_decorator
# 
# @decorator_factory("start","end")
# def hello():
#     print("hello world")
#     
# hello()
# =============================================================================

# =============================================================================
# class NotFlask():
#     def __init__(self):
#         self.routes = {}
# 
#     def route(self,route_str):
#         def decorator(f):
#             self.routes[route_str] = f
#             return f
#         
#         return decorator
#     
#     def serve(self,path):
#         view_function = self.routes.get(path)
#         if view_function:
#             return view_function()
#         else:
#             raise ValueError('Route "{}"" has not been registered'.format(path))
#     
# app = NotFlask()
# @app.route('/')
# def hello():
#     return "hello world"
# 
# print(app.serve('/'))
# 
# class TestNotFlask(unittest,TestCase):
#     def setUp(self):
#         self.app = NotFlask()
#         
#     def test_valid_route(self):
#         @self.app.route('/')
#         def index():
#             return "hello world"
#         
#         self.assertEqual(self.app.serve('/'),'hello world')
#         
#     def test_invalid_route(self):
#         with self.assertRaises(ValueError):
#             self.app.serve('/invalid')
# 
# =============================================================================
# =============================================================================
# import re
# def build_route_pattern(route):
#     route_regex = re.sub(r'(<\w+>)',r'(?P\1.+)',route)
#     return re.compile("^{}$".format(route_regex))
# 
# print(build_route_pattern('/hello/<username>'))
# =============================================================================
import re
class NotFlask():
    def __init__(self):
        self.routes = []
        
    @staticmethod
    def build_route_pattern(route):
        route_regex = re.sub(r'(<\w+>)',r'(?P\1.+)',route)
        return re.compile("^{}$".format(route_regex))
    
    def route(self,route_str):
        def decorator(f):
            route_pattern = self.build_route_pattern(route_str)
            self.routes.append((route_pattern,f))
            
            return f
        
        return decorator
    

    def get_route_match(self,path):
        for route_pattern,view_function in self.routes:
            m = route_pattern.match(path)
            if m:
                return m.groupdict(),view_function
            
        return None
    
    def serve(self,path):
        route_match = self.get_route_match(path)
        if route_match:
            kwargs,view_function = route_match
            print(kwargs)
            return view_function(**kwargs)
        else:
            raise ValueError('Route "{}"" has not been registered'.format(path))



app = NotFlask()
@app.route("/hello/<username>")
def hello_user(username):
    return "hello {}!".format(username)

print(app.serve("/hello/hjacks"))



































