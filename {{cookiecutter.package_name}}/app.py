#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
#
# Distributed under terms of the MIT license.

"""

"""

from pathlib import Path

import diskcache
import ring
import streamlit as st


# Initial Configuation
st.set_page_config(layout="wide")


storage = diskcache.Cache(Path(__file__).parent / ".diskcache")


@ring.disk(storage)
def cached_method():
    pass


def view1():
    st.title("{{ cookiecutter.package_name }}")
    # st.text("")
    # st.image("")
    # st.markdown("")
    # st.dataframe(df)

    with st.echo():
        # Put your code to show here.
        pass


def view2():
    pass


def view3():
    pass


PAGES = {"View 1": view1, "View 2": view2, "View 3": view3}
st.sidebar.title("Change view")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page()
