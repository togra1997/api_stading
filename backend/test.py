"""テスト用スクリプト."""

from api.dependency.managemant_csv import ManagedTaskCsv
from api.schema import task

csv = ManagedTaskCsv()
task_data = csv.read_csv_data().execute().to_dict(orient="records")


print([task.GetTask(**t) for t in task_data])
