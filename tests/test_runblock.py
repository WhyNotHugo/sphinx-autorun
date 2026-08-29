"""Tests for the runblock directive."""

from __future__ import annotations

import pytest
from docutils.nodes import literal_block
from sphinx.testing.util import SphinxTestApp


def _literal_texts(app: SphinxTestApp) -> list[str]:
    doctree = app.env.get_and_resolve_doctree(
        "index", app.builder, tags=app.builder.tags
    )
    return [node.astext() for node in doctree.findall(literal_block)]


@pytest.mark.sphinx("html", testroot="empty-output", warningiserror=True)
def test_console_runblock_with_empty_output(app: SphinxTestApp) -> None:
    """Commands with no stdout/stderr must not raise UnboundLocalError."""
    app.build()
    assert _literal_texts(app) == ["$ true\n"]


@pytest.mark.sphinx("html", testroot="stdout", warningiserror=True)
def test_console_runblock_with_stdout(app: SphinxTestApp) -> None:
    app.build()
    assert _literal_texts(app) == ["$ echo hello\nhello\n"]
