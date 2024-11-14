import subprocess
import json

def test_help():
    result = subprocess.run(['chef-node-management-cli', 'management', 'cohort', 'create-cohort', '--body-file' ,'new_cohart.json'],capture_output=True,text=True)
    assert result.returncode==0
    print(result.stdout)
    try:
        res = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return
    print(res)
    cohort = res["item"]["cohortId"]
    print(cohort)
    pro=subprocess.run(['chef-node-management-cli','management' ,'cohort', 'find-one-cohort' ,'--cohortId',cohort],capture_output=True,text=True)
    print(pro.stdout)
    assert pro.returncode==0