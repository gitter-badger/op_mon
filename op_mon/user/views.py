#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# op_mon (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# This file is part of op_mon.
#
#    op_mon is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename:  by: andrek
# Timesamp: 10/1/16 :: 09:42 AM
from flask import Blueprint, render_template, session, current_app
from flask_login import login_required
from flask_themes2 import render_theme_template

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_theme_template(session.get('theme', current_app.config['DEFAULT_THEME']), 'users/members.html')


@blueprint.route('/dashboard/')
@login_required
def dashboard():
    """About page."""
    return render_theme_template(session.get('theme', current_app.config['DEFAULT_THEME']), 'users/dashboard.html')