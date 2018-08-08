#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# thoth-user-api
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Configuration of user-facing API service."""

import os
import datetime

from thoth.common import get_service_account_token


class Configuration:
    """Configuration of user-facing API service."""

    APP_SECRET_KEY = os.environ['THOTH_USER_API_APP_SECRET_KEY']
    SWAGGER_YAML_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'swagger.yaml')

    KUBERNETES_API_URL = os.getenv('KUBERNETES_API_URL', 'https://kubernetes.default.svc.cluster.local')
    OPENSHIFT_API_URL = os.getenv('OPENSHIFT_API_URL', 'https://openshift.default.svc.cluster.local')
    KUBERNETES_VERIFY_TLS = bool(int(os.getenv('KUBERNETES_VERIFY_TLS', True)))
    KUBERNETES_API_TOKEN = os.getenv('KUBERNETES_API_TOKEN') or get_service_account_token()
    THOTH_FRONTEND_NAMESPACE = os.environ['THOTH_FRONTEND_NAMESPACE']
    THOTH_MIDDLETIER_NAMESPACE = os.environ['THOTH_MIDDLETIER_NAMESPACE']
    THOTH_BACKEND_NAMESPACE = os.environ['THOTH_BACKEND_NAMESPACE']
    THOTH_INFRA_NAMESPACE = os.environ['THOTH_BACKEND_NAMESPACE']
    THOTH_RESULT_API_URL = os.environ['THOTH_RESULT_API_URL']
    THOTH_ADVISER_OUTPUT = THOTH_RESULT_API_URL + '/api/v1/adviser-result'
    THOTH_ANALYZER_OUTPUT = THOTH_RESULT_API_URL + '/api/v1/analysis-result'
    THOTH_SOLVER_OUTPUT = THOTH_RESULT_API_URL + '/api/v1/solver-result'
    THOTH_SECRET = os.environ['THOTH_SECRET']
