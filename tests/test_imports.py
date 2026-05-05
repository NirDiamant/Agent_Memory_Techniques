"""Smoke test: every notebook's import cell parses as valid Python."""
import ast, glob, json, pathlib, pytest

ROOT = pathlib.Path(__file__).parent.parent
NOTEBOOKS = sorted(glob.glob(str(ROOT / "all_techniques" / "*" / "*.ipynb")))


@pytest.mark.parametrize("nb_path", NOTEBOOKS)
def test_imports_parse(nb_path):
    """Every code cell that looks like imports must be valid Python syntax."""
    nb = json.loads(pathlib.Path(nb_path).read_text())
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        src = cell.get("source", "")
        if isinstance(src, list):
            src = "".join(src)
        # Strip Jupyter magics (%pip, !shell, etc.)
        cleaned = "\n".join(line for line in src.splitlines() if not line.lstrip().startswith(("%", "!")))
        if not cleaned.strip():
            continue
        try:
            ast.parse(cleaned)
        except SyntaxError as e:
            pytest.fail(f"{nb_path} cell #{i}: syntax error {e}")


def test_at_least_30_notebooks():
    assert len(NOTEBOOKS) >= 30, f"expected 30+ notebooks, got {len(NOTEBOOKS)}"
