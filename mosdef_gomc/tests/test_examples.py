#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mbuild.examples` module. """

class TestExamples:

    def test_alkane(self):
        import mbuild.examples.alkane.alkane as example
        example.main()

    def test_alkane_monolayer(self):
        import mbuild.examples.alkane_monolayer.alkane_monolayer as example
        example.main()

    def test_bilayer(self):
        import mbuild.examples.bilayer.bilayer as example
        example.main()

    def test_ethane(self):
        import mbuild.examples.ethane.ethane as example
        example.main()

    def test_methane(self):
        import mbuild.examples.methane.methane as example
        example.main()

    def test_pmpc_brush_layer(self):
        import mbuild.examples.pmpc_brush_layer.pmpc_brush_layer as example
        example.main()

    def test_reload(self):
        import mbuild.examples.reload.reload as example
        example.main()

    def test_solvate(self):
        import mbuild.examples.solvate.solvate as example
        example.main()

    def test_tnp(self):
        import mbuild.examples.tnp.tnp as example
        example.main()