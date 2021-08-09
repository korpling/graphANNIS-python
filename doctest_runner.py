#!/usr/bin/env python3

if __name__ == '__main__':
    import doctest
    from graphannis import graph, cs, errors, util
    import graphannis
    doctest.testmod(graph, verbose=True)
    doctest.testmod(cs, verbose=True)
    doctest.testmod(errors, verbose=True)
    doctest.testmod(util, verbose=True)
