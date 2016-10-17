from flask import Flask, Blueprint, jsonify, request, current_app
import re


def authenticate(data):
    current_app.logger.debug("Entering method authenticate of auth_validator.")
    error = None
    is_valid = True
    if not ('username' in data):
        error = "Field username is missing."
        is_valid = False
    if ('username' in data):
        if not (data['username']):
            error = "username cannot be empty."
            is_valid = False
    if not ('password' in data):
        error = "Field password is missing."
        is_valid = False
    if ('password' in data):
        if not (data['password']):
            error = "password cannot be empty."
            is_valid = False
    current_app.logger.debug("Exit method authenticate of auth_validator.")
    return is_valid, error


def logout(data):
    current_app.logger.debug("Entering method logout of auth_validator.")
    error = None
    is_valid = True
    if not ('uid' in data):
        error = "Field uid is missing."
        is_valid = False
    if ('uid' in data):
        if not (data['uid']):
            error = "uid cannot be empty."
            is_valid = False
    current_app.logger.debug("Exit method logout of auth_validator.")
    return is_valid, error


def authenticate_token(data):
    current_app.logger.debug("Entering method authenticate_token of auth_validator.")
    error = None
    is_valid = True
    if not ('access_token' in data):
        error = "Field access_token is missing."
        is_valid = False
    if ('access_token' in data):
        if not (data['access_token']):
            error = "access_token cannot be empty."
            is_valid = False
    if not ('uid' in data):
        error = "Field uid is missing."
        is_valid = False
    if ('uid' in data):
        if not (data['uid']):
            error = "uid cannot be empty."
            is_valid = False
    current_app.logger.debug("Exit method authenticate_token of auth_validator.")
    return is_valid, error
