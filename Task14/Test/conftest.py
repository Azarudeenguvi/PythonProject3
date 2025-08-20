import pytest
import datetime

def pytest_configure(config):
    # Generate timestamp (e.g. 2025-08-19_14-30-45)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Define reports folder + filename
    report_dir = "reports"
    report_file = f"{report_dir}/report_{timestamp}.html"

    # Set the HTML report path dynamically
    config.option.htmlpath = report_file
    config.option.self_contained_html = True