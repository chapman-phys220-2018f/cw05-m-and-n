#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fib
import io
import contextlib

"""fib.py Test Module

Verify correct functionality of Fibonacci module.
"""

def test_fib_eighth():
    """Test eight Fibonacci number.
    
    Note that this test highlights the convenience of defining a
    main function in a script file. Normally one would call this
    script from the command line via bash. Here we call it directly
    and redirect the output (stdout) to a string that we can test.
    """
    # First redirect stdout to a string
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        # then run the script with commandline argument "6"
        # note that argument 0 is always the program name itself
        fib.main(["./fib.py", "6"])
    # then check printed output in string, stripping newline characters
    assert out.getvalue().strip() == "8"
