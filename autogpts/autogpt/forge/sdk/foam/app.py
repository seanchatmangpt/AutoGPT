"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"foam v{version('foam')}")  # type: ignore[no-untyped-call]
