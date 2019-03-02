#!/bin/bash
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -z "${TRAVIS_BUILD_NUMBER}" ]]; then
  pip install -r "${SCRIPT_DIR}/requirements.txt"
else
  # If in Travis, use the `--user` flag when performing `pip install` of
  # dependencies.
  pip install --user -r "${SCRIPT_DIR}/requirements.txt"
fi

pylint --rcfile="${SCRIPT_DIR}/.pylintrc" ${SCRIPT_DIR}/*.py

for PY_TEST_FILE in ${SCRIPT_DIR}/*_test.py; do
  python ${PY_TEST_FILE}
done
