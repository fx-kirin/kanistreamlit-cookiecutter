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


st.title("{{ cookiecutter.package_name }}")
# st.text("")
# st.image("")
# st.markdown("")
# st.dataframe(df)

with st.echo():
    # Put your code to show here.
    pass
