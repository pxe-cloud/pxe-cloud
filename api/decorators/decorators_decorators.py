#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def optional_args_decorator(f):
    def wrapped_decorator(*args):
        if len(args) == 1 and callable(args[0]):
            return f(args[0])

        else:
            def _decorator(optional_params):
                return f(optional_params, *args)

            return _decorator

    return wrapped_decorator
