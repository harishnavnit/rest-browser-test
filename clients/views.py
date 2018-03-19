from django.shortcuts import render
from django.http import HttpResponse

from selenium import webdriver
from selenium.common.exceptions import WebDriverException



browser_instance = ""

def index():
    return HttpResponse(status=200)


def start(request):
    global browser_instance
    browser_name = request.GET['browser']
    browrser_url = request.GET['url']

    if browser_name == "firefox" or browser_name == "mozilla":
        browser_instance = webdriver.Firefox()
    elif browser_name == "google" or browser_name == "chrome":
        browser_instance = webdriver.Chrome()

    browser_instance.get(browrser_url)
    return HttpResponse(status=200)


def geturl(request):
    global browser_instance

    try:
        active_url = browser_instance.current_url
    except WebDriverException as w_err:
        print("Invalid URL : ", w_err)
        return HttpResponse(status=500)

    return HttpResponse(active_url)


def stop(request):
    global browser_instance
    try:
        browser_instance.close()
    except WebDriverException as w_err:
        print("Web driver exception : ", w_err)
        return HttpResponse(status=500)
    return HttpResponse(status=200)


def cleanup(request):
    global browser_instance
    try:
        browser_instance.delete_all_cookies()
    except WebDriverException as w_err:
        print("Web driver exception : ", w_err)
        return HttpResponse(status=500)
    return HttpResponse(status=200)
