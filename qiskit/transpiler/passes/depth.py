# -*- coding: utf-8 -*-

# Copyright 2019, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

""" An analysis pass for calculating the depth of a DAG circuit.
"""
from qiskit.transpiler.basepasses import AnalysisPass


class Depth(AnalysisPass):
    """ An analysis pass for calculating the depth of a DAG circuit.
    """

    def run(self, dag):
        self.property_set['depth'] = dag.depth()
