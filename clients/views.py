from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404

from selenium import webdriver
from selenium.common.exceptions import WebDriverException



browser_instance = ""

def index():
    return HttpResponse(status=200)


def start(request):
    global browser_instance

    try:
        browser = request.GET['browser']
        url = request.GET['url']
    except Exception as err:
        return Http404("Invalid URL query")

    if browser == "firefox" or browser == "mozilla":
        browser_instance = webdriver.Firefox()
    elif browser == "google" or browser == "chrome":
        browser_instance = webdriver.Chrome()

    browser_instance.get(url)
    return HttpResponse(status=200)


def geturl(request, browser):
    global browser_instance

    try:
        active_url = browser_instance.current_url
    except WebDriverException as w_err:
        print("Invalid URL : ", w_err)
        return HttpResponse(status=500)

    return HttpResponse(active_url)


def stop(request, browser):
    global browser_instance
    try:
        browser_instance.close()
    except WebDriverException as w_err:
        print("Web driver exception : ", w_err)
        return HttpResponse(status=500)
    return HttpResponse(status=200)


def cleanup(request, browser):
    global browser_instance
    try:
        browser_instance.delete_all_cookies()
    except WebDriverException as w_err:
        print("Web driver exception : ", w_err)
        return HttpResponse(status=500)
    return HttpResponse(status=200)
