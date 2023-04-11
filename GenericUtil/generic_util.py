from pathlib import Path
from datetime import datetime
import os


def get_project_root():
    return Path(__file__).parent.parent


def generate_bat_file():
    project_path = get_project_root()
    batch_file_name = f"{project_path}/run.bat"
    html_report_name = datetime.now().strftime('generated_html_report_%H_%M_%d_%m_%Y.html')
    command = f"""cd {project_path}
cd TestScript
pytest -v -s --html=../HtmlReports{html_report_name}"""
    f = open(batch_file_name, "w+")
    f.writelines(command)
    f.close()

    return batch_file_name


def run_batch_file():
    generate_bat_file
    os.system(generate_bat_file())

# cls
