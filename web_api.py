#!/usr/bin/python 
# -*- coding:utf-8 -*- 
import json, sys 
import ast 
import cgi, cgitb 
cgitb.enable() 
print("Content-Type: text/html\n\n") 
if __name__ == '__main__':
    form = cgi.FieldStorage()
    input_str =  json.loads(form.getvalue('data'))
    print(json.dumps({'res': input_str}))
    
