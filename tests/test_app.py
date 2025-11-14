import pytest
from app import app
from dash.testing.application_runners import ThreadedRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def run_app():
    runner = ThreadedRunner()
    runner.start(app)
    yield runner
    runner.stop()


def test_header_present(driver, run_app):
    driver.get(run_app.url)

    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    assert "Pink Morsel Sales Dashboard" in header.text


def test_graph_present(driver, run_app):
    driver.get(run_app.url)

    graph = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sales-graph"))
    )

    assert graph is not None


def test_region_picker_present(driver, run_app):
    driver.get(run_app.url)

    radio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "region-filter"))
    )

    assert radio is not None
